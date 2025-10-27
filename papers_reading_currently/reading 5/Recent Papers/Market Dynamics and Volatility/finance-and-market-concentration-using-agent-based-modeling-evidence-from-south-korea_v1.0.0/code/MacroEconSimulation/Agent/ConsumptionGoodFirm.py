from SimulationEngine.ClassicDEVS.DEVSAtomicModel import DEVSAtomicModel
from SimulationEngine.Utility.Configurator import Configurator
from MacroEconSimulation.Agent.Machine import Machine

from MacroEconSimulation.Message.requestMachine import requestMachine
from MacroEconSimulation.Message.requestLoan import requestLoan
from MacroEconSimulation.Message.endPIprocess import endPIprocess
from MacroEconSimulation.Message.endPHprocess import endPHprocess
from MacroEconSimulation.Message.endMCprocess import endMCprocess
from MacroEconSimulation.Message.endBUprocess import endBUprocess

import os
import math
import numpy as np


class ConsumptionGoodFirm(DEVSAtomicModel):
    def __init__(self, strID, numID, objConfiguration, objLogConsumptionFirm, objMacroEcon):
        super().__init__(strID)

        self.strID = strID
        self.numID = numID
        self.objConfiguration = objConfiguration
        self.objLogConsumptionFirm = objLogConsumptionFirm
        self.objMacroEcon = objMacroEcon
        self.startUpTime = 0
        self.newEntrant = False

        # about balance sheet
        initCashAvg = 50
        initCashStd = 0.2 * initCashAvg

        self.liquidAsset = np.random.uniform(initCashAvg - initCashStd, initCashAvg + initCashStd, 1)[0]
        self.debt = 0
        self.debtRepayment = 0

        # about capital
        N_Fc = self.objConfiguration.getConfiguration("N_Fc")
        N_H = self.objConfiguration.getConfiguration("N_H")
        iota = self.objConfiguration.getConfiguration("iota")  # Desired inventory level
        initEmploy = self.objConfiguration.getConfiguration("initEmploy")
        eta = self.objConfiguration.getConfiguration("eta")  # Physical scrapping age
        self.surplusCost = self.objConfiguration.getConfiguration("surplusCost")

        initCapitalAvg = initEmploy * N_H / N_Fc
        initCapitalStd = 0.2 * initCapitalAvg

        self.capital = int(round(np.random.uniform(initCapitalAvg - initCapitalStd, initCapitalAvg + initCapitalStd, 1)[0]))
        self.desiredCapital = 0
        self.lstCapital = []
        lstCapitalGoodFirm = self.objMacroEcon.lstCapitalGoodFirm
        for k in range (0, self.capital):
            sampledFirm = lstCapitalGoodFirm[np.random.random_integers(0, len(lstCapitalGoodFirm)-1, 1)[0]]
            sampledTech = sampledFirm.techA
            sampledAge = np.random.random_integers(1, 20, 1)[0]
            self.lstCapital.append(Machine(self.objConfiguration, sampledTech, sampledAge, 0))

        # about market share
        self.marketShare = [None, self.capital / (N_H * initEmploy)]
        self.competitiveness = None

        # about production
        self.demand = initEmploy * N_H * self.marketShare[-1]
        self.inventory = round(self.demand * iota)
        self.desiredProduction = 0
        self.production = 0

        # about investment
        self.lstBrochure = []
        self.requestMachineCnt = 0
        self.requestMachinePrice = 0
        self.requestMachineTech = 0
        self.investment = 0

        # about labor
        self.desiredLabor = 0
        self.hiredLabor = 0

        # about sale
        mu0 = self.objConfiguration.getConfiguration("mu0")

        self.markUp = mu0
        self.price = None
        self.sale = 0
        self.saleTax = 0
        self.unfilledDemand = 0

        self.approveAmount = 0
        self.sales = 0
        self.prevSales = 0

        self.setStateValue("state", "wait")

    def funcExternalTransition(self, strPort, objEvent):

        # Get brochure
        if strPort == "sendBrochure":
            self.lstBrochure.append([objEvent.sellerID, objEvent.techA, objEvent.price])

        elif strPort == "startPIprocess":
            self.setStateValue("state", "PIstep")

        elif strPort == "provideLoan":
            self.approveAmount = objEvent.approveAmount
            self.liquidAsset += self.approveAmount
            self.debt += self.approveAmount
            self.debtRepayment = self.calcDebtRepayment()

            self.setStateValue("state", "PIstep2")


        elif strPort == "startPHprocess":
            if self.newEntrant == False:
                alpha = self.objConfiguration.getConfiguration("alpha")
                wage = self.objMacroEcon.objHousehold.wage

                investmentCost = self.requestMachinePrice * self.requestMachineCnt
                avgTechA = self.calcAverageTechA()

                if len(self.lstCapital) > 0:
                    tempLaborNeed = math.ceil(math.pow(self.desiredProduction / (avgTechA * math.pow(len(self.lstCapital), alpha)), 1 / (1 - alpha)))
                else:
                    tempLaborNeed = 0

                tempLaborAfford = max(math.floor((self.liquidAsset - investmentCost) / wage), 0)

                self.desiredLabor = min(tempLaborNeed, tempLaborAfford)

                self.setStateValue("state", "PHstep")

            elif self.newEntrant == True:
                self.setStateValue("state", "PHstep")

        elif strPort == "sendMachine":
            for i in range (0, objEvent.machineAmount):
                self.lstCapital.append(Machine(self.objConfiguration, objEvent.techA, 0, self.requestMachinePrice))

            if self.newEntrant == False:
                self.investment += objEvent.machineAmount
                sellerFirm = self.objMacroEcon.lstCapitalGoodFirm[objEvent.sellerID]
                sellerFirm.sale += objEvent.machineAmount
            elif self.newEntrant == True:
                sellerFirm = self.objMacroEcon.lstCapitalGoodFirm[objEvent.sellerID]
                sellerFirm.sale += objEvent.machineAmount

        elif strPort == 'startMCprocess':
            self.setStateValue("state", "MCstep")

        elif strPort == "startBUprocess":
            self.setStateValue("state", "BUstep")

    def funcOutput(self):

        # Consumption good firm PI step
        if self.getStateValue("state") == "PIstep":

            if self.newEntrant == False:
                b = self.objConfiguration.getConfiguration("b")  # Payback period
                iota = self.objConfiguration.getConfiguration("iota")  # Desired inventory level
                eta = self.objConfiguration.getConfiguration("eta")  # Physical scrapping age
                alpha = self.objConfiguration.getConfiguration("alpha") # Cobb douglas alpha
                delta = self.objConfiguration.getConfiguration("delta")  # Maximum capital expansion rate
                wage = self.objMacroEcon.objHousehold.wage

                if len(self.lstBrochure) == 0:
                    lstCapitalGoodFirm = self.objMacroEcon.lstCapitalGoodFirm
                    sampledFirm = lstCapitalGoodFirm[np.random.random_integers(0, len(lstCapitalGoodFirm) - 1, 1)[0]]
                    self.lstBrochure.append([sampledFirm.numID, sampledFirm.techA, sampledFirm.price])

                techScore_min = math.inf   # smaller is better!
                for k in range (len(self.lstBrochure)):
                    tempBrochure = self.lstBrochure[k]
                    techScore_Temp = tempBrochure[2] + b * (wage / tempBrochure[1])
                    if techScore_Temp <= techScore_min:
                        techScore_min = techScore_Temp
                        aStar = tempBrochure[1]
                        pStar = tempBrochure[2]
                        cStar = wage / aStar
                        sellerID = tempBrochure[0]

                # investment (expansion)
                avgTechA = self.calcAverageTechA()
                self.desiredProduction = max(round(self.demand + iota * self.demand - self.inventory), 0)

                if len(self.lstCapital) > 0:
                    self.desiredLabor = math.ceil(math.pow(self.desiredProduction / (avgTechA * math.pow(len(self.lstCapital), alpha)), 1 / (1 - alpha)))
                    self.desiredCapital = (alpha * aStar * self.desiredLabor * eta * wage) / (pStar * (1 - alpha) * avgTechA)

                else:
                    if self.liquidAsset > pStar:
                        self.desiredLabor = 0
                        self.desiredCapital = 1
                    else:
                        self.desiredLabor = 0
                        self.desiredCapital = 0

                EIcnt = min(max(round(self.desiredCapital - self.capital), 0), max(round(self.capital*delta), 1))

                # investment (replacement)
                RScnt = 0
                for k in range (len(self.lstCapital)):
                    tempMachine = self.lstCapital[k]
                    tempUnitCost = wage / tempMachine.techA
                    if tempMachine.age == 20:
                        tempMachine.machineScrap()
                        RScnt += 1
                    elif tempUnitCost > cStar:
                        replacementScore = pStar / (tempUnitCost - cStar)
                        if replacementScore <= b:
                            tempMachine.machineScrap()
                            RScnt += 1

                if self.capital > self.desiredCapital:
                    RScnt = max(RScnt - round(self.capital - self.desiredCapital), 0)

                # request machine & loan
                self.requestMachineCnt = int(round(RScnt + EIcnt))
                self.requestMachinePrice = pStar
                self.requestMachineTech = aStar

                self.loanDesired = max(wage * self.desiredLabor + (RScnt + EIcnt) * pStar - self.liquidAsset, 0)
                if self.loanDesired > 0:
                    objEvent2 = requestLoan(self.numID, self.loanDesired)
                    self.addOutputEvent("requestLoan", objEvent2)

                elif self.loanDesired == 0:
                    if self.requestMachineCnt > 0:
                        objEvent1 = requestMachine(self.numID, self.requestMachineCnt)
                        self.addOutputEvent("requestMachine_" + str(sellerID), objEvent1)

                    objEvent = endPIprocess(self.objConfiguration.getConfiguration("time"), self.strID)
                    self.addOutputEvent("endPIprocess", objEvent)

            elif self.newEntrant == True:

                t = self.objConfiguration.getConfiguration("time")
                self.startUpTime = t

                # about balance sheet
                pi3 = 0.1  # uniform distribution support lower for entrant liquid Asset
                pi4 = 0.9  # uniform distribution support upper for entrant liquid Asset
                averageLiquidAsset = self.getMarketLiquidAsset()

                self.liquidAsset = np.random.uniform(pi3 * averageLiquidAsset, pi4 * averageLiquidAsset, 1)[0]
                self.debt = 0
                self.debtRepayment = 0

                self.objMacroEcon.objBank.lstDebtAccount[self.numID] = 0

                # about capital
                N_H = self.objConfiguration.getConfiguration("N_H")
                t = self.objConfiguration.getConfiguration("time")
                b = self.objConfiguration.getConfiguration("b")  # Payback period
                wage = self.objMacroEcon.objHousehold.wage
                initEmploy = self.objConfiguration.getConfiguration("initEmploy")
                alpha = self.objConfiguration.getConfiguration("alpha")

                pi1 = 0.1  # uniform distribution support lower for entrant capital
                pi2 = 0.9  # uniform distribution support upper for entrant capital
                averageCapital = self.getMarketAverageCapital()

                self.capital = 0
                self.desiredCapital = max(int(round(np.random.uniform(pi1 * averageCapital, pi2 * averageCapital, 1)[0])), 1)
                self.lstCapital = []
                if len(self.lstBrochure) == 0:
                    lstCapitalGoodFirm = self.objMacroEcon.lstCapitalGoodFirm
                    sampledFirm = lstCapitalGoodFirm[np.random.random_integers(0, len(lstCapitalGoodFirm) - 1, 1)[0]]
                    self.lstBrochure.append([sampledFirm.numID, sampledFirm.techA, sampledFirm.price])

                techScore_min = math.inf  # smaller is better!
                for k in range(len(self.lstBrochure)):
                    tempBrochure = self.lstBrochure[k]
                    techScore_Temp = tempBrochure[2] + b * (wage / tempBrochure[1])
                    if techScore_Temp <= techScore_min:
                        techScore_min = techScore_Temp
                        aStar = tempBrochure[1]
                        pStar = tempBrochure[2]
                        cStar = wage / aStar
                        sellerID = tempBrochure[0]

                # request machine & loan
                self.requestMachineCnt = self.desiredCapital

                self.requestMachinePrice = pStar
                self.requestMachineTech = aStar
                if self.requestMachineCnt > 0:
                    objEvent1 = requestMachine(self.numID, self.requestMachineCnt)
                    self.addOutputEvent("requestMachine_" + str(sellerID), objEvent1)

                # about market share
                totalMarketCapital = self.objMacroEcon.objHousehold.totalCapital
                self.marketShare = [None, self.desiredCapital / totalMarketCapital]
                self.competitiveness = None

                # about production
                self.demand = aStar * pow(self.desiredCapital, alpha) * pow(initEmploy * N_H * self.marketShare[-1], 1 - alpha)
                self.inventory =  0
                self.desiredProduction = 0
                self.production = 0

                # about investment
                self.investment = 0

                # about labor
                self.desiredLabor = 0
                self.hiredLabor = 0

                # about sale
                mu0 = self.objConfiguration.getConfiguration("mu0")

                self.markUp = mu0
                self.price = None
                self.sale = 0
                self.saleTax = 0
                self.unfilledDemand = 0

                objEvent = endPIprocess(self.objConfiguration.getConfiguration("time"), self.strID)
                self.addOutputEvent("endPIprocess", objEvent)


        # Consumption good firm PI step - 2
        elif self.getStateValue("state") == "PIstep2":
            b = self.objConfiguration.getConfiguration("b")  # Payback period
            wage = self.objMacroEcon.objHousehold.wage

            if self.requestMachineCnt > 0:

                techScore_min = math.inf  # smaller is better!
                for k in range(len(self.lstBrochure)):
                    tempBrochure = self.lstBrochure[k]
                    techScore_Temp = tempBrochure[2] + b * (wage / tempBrochure[1])
                    if techScore_Temp <= techScore_min:
                        techScore_min = techScore_Temp
                        aStar = tempBrochure[1]
                        pStar = tempBrochure[2]
                        cStar = wage / aStar
                        sellerID = tempBrochure[0]

                self.requestMachineCnt = max(min(self.requestMachineCnt, int(math.floor((self.liquidAsset - self.desiredLabor * wage) / pStar))), 0)
                objEvent1 = requestMachine(self.numID, self.requestMachineCnt)
                self.addOutputEvent("requestMachine_" + str(sellerID), objEvent1)

            objEvent = endPIprocess(self.objConfiguration.getConfiguration("time"), self.strID)
            self.addOutputEvent("endPIprocess", objEvent)

        # Consumption good firm PH step
        elif self.getStateValue("state") == "PHstep":
            if self.newEntrant == False:
                N_H = self.objConfiguration.getConfiguration("N_H")
                alpha = self.objConfiguration.getConfiguration("alpha")  # Cobb douglas alpha
                omega_1 = self.objConfiguration.getConfiguration("omega_1")
                omega_2 = self.objConfiguration.getConfiguration("omega_2")
                v = self.objConfiguration.getConfiguration("v")
                wage = self.objMacroEcon.objHousehold.wage

                totalLaborDemand = self.getTotalLaborDesired()
                if totalLaborDemand > N_H:
                    self.hiredLabor = math.floor(self.desiredLabor * N_H / totalLaborDemand)
                else:
                    self.hiredLabor = self.desiredLabor

                self.production = round(self.calcAverageTechA() * pow(self.capital, alpha) * pow(self.hiredLabor, 1-alpha))

                prevMarketShare = self.marketShare[-2]
                currMarketShare = self.marketShare[-1]
                if prevMarketShare != None:
                    self.markUp = self.markUp * (1 + v * (currMarketShare - prevMarketShare) / prevMarketShare)

                if self.production != 0 and self.hiredLabor != 0:
                    productionCost = (self.hiredLabor * wage) / self.production
                    currPrice = (1 + self.markUp) * productionCost
                    if self.price is None:
                        self.price = currPrice
                    else:
                        self.price = (currPrice * self.production + self.price * self.inventory) / (self.production + self.inventory)
                else:
                    self.price = self.price

                if self.price is not None:
                    self.competitiveness = - 1 * (omega_1 * self.price + omega_2 * self.unfilledDemand)
                else:
                    self.competitiveness = 0

                self.inventory += self.production

                objEvent = endPHprocess(self.objConfiguration.getConfiguration("time"), self.strID)
                self.addOutputEvent("endPHprocess", objEvent)

            elif self.newEntrant == True:
                objEvent = endPHprocess(self.objConfiguration.getConfiguration("time"), self.strID)
                self.addOutputEvent("endPHprocess", objEvent)

        elif self.getStateValue("state") == "MCstep":
            if self.newEntrant == False:

                totalConsumption = self.objMacroEcon.objHousehold.totalConsumption
                if self.price is not None:
                    self.demand = int(round(totalConsumption * self.marketShare[-1] / self.price))
                else:
                    self.demand = self.demand

                self.prevSales = self.sales
                self.sale = min(self.demand, self.inventory)
                self.unfilledDemand = max(0, self.demand - self.inventory)
                self.inventory = self.inventory - self.sale

                objEvent = endMCprocess(self.objConfiguration.getConfiguration("time"), self.strID)
                self.addOutputEvent("endMCprocess", objEvent)

            elif self.newEntrant == True:
                objEvent = endMCprocess(self.objConfiguration.getConfiguration("time"), self.strID)
                self.addOutputEvent("endMCprocess", objEvent)

        elif self.getStateValue("state") == 'BUstep':

            if self.newEntrant == False:
                r = self.objConfiguration.getConfiguration("r")
                pr = self.objConfiguration.getConfiguration("pr")
                psi_u = self.objConfiguration.getConfiguration("psi_u")
                psi_d = self.objConfiguration.getConfiguration("psi_d")
                tr = self.objConfiguration.getConfiguration("tr")

                r_loan = ( 1 + psi_u ) * r / 4
                r_deposit = ( 1 - psi_d ) * r / 4
                wage = self.objMacroEcon.objHousehold.wage

                loanRepayAmount = self.debtRepayment
                self.debt = self.debt * (1 + r_loan) - loanRepayAmount
                if self.debt < 0.0001 and self.debtRepayment != 0:
                    self.debt = 0
                    self.debtRepayment = 0

                self.objMacroEcon.objBank.lstDebtAccount[self.numID] = self.debt

                if self.price is not None:
                    self.sales = self.price * self.sale
                    netSale = self.price * self.sale - wage * self.hiredLabor - self.investment * self.requestMachinePrice
                else:
                    netSale = 0 - wage * self.hiredLabor - self.investment * self.requestMachinePrice

                if netSale > 0:
                    self.saleTax = netSale * tr
                else:
                    self.saleTax = 0

                if self.liquidAsset > 0:
                    interest = self.liquidAsset * r_deposit
                else:
                    interest = 0


                if self.price is not None:
                    self.surplus = self.price * self.sale - wage * self.hiredLabor
                else:
                    self.surplus = 0

                self.liquidAsset = self.liquidAsset + netSale + interest - self.saleTax - loanRepayAmount

                lstCapitalTemp = []
                for k in range(len(self.lstCapital)):
                    tempMachine = self.lstCapital[k]
                    if tempMachine.machineScrapDummy == False:
                        tempMachine.age += 1
                        lstCapitalTemp.append(tempMachine)

                self.lstCapital = lstCapitalTemp
                self.capital = len(lstCapitalTemp)

                # write consumption firm log
                self.objLogConsumptionFirm.write(str(self.objConfiguration.getConfiguration("time")) + "," + \
                                                 str(self.numID) + "," + \
                                                 str(self.liquidAsset) + "," + \
                                                 str(self.debt) + "," + \
                                                 str(self.debtRepayment) + "," + \
                                                 str(self.capital) + "," + \
                                                 str(self.desiredCapital) + "," + \
                                                 str(self.calcAverageTechA()) + "," + \
                                                 str(self.marketShare[-1]) + "," + \
                                                 str(self.competitiveness) + "," + \
                                                 str(self.demand) + "," + \
                                                 str(self.inventory) + "," + \
                                                 str(self.desiredProduction) + "," + \
                                                 str(self.production) + "," + \
                                                 str(self.investment) + "," + \
                                                 str(self.requestMachinePrice) + "," + \
                                                 str(self.requestMachineTech) + "," + \
                                                 str(self.requestMachineCnt) + "," + \
                                                 str(self.desiredLabor) + "," + \
                                                 str(self.hiredLabor) + "," + \
                                                 str(self.markUp) + "," + \
                                                 str(self.price) + "," + \
                                                 str(self.sale) + "," + \
                                                 str(self.unfilledDemand) + "," + \
                                                 str(self.startUpTime) + "," + \
                                                 str(self.approveAmount) + "," + \
                                                 str(self.loanDesired) + "," + \
                                                 str(self.prevSales)+ "\n")
                self.objLogConsumptionFirm.flush()

                self.investment = 0

                # new consumption good company
                if self.liquidAsset < 0 or self.demand < 1 or self.capital == 0:
                    self.newEntrant = True
                    self.prevSurplus, self.surplus = 0, 0
                objEvent = endBUprocess(self.objConfiguration.getConfiguration("time"), self.ID)
                self.addOutputEvent("endBUprocess", objEvent)

            elif self.newEntrant == True:
                lstCapitalTemp = []
                for k in range(len(self.lstCapital)):
                    tempMachine = self.lstCapital[k]
                    if tempMachine.machineScrapDummy == False:
                        tempMachine.age += 1
                        lstCapitalTemp.append(tempMachine)

                self.lstCapital = lstCapitalTemp
                self.capital = len(lstCapitalTemp)

                '''Here'''
                self.approveAmount = 0
                self.exit = 0
                if self.liquidAsset < 0 or self.demand < 1 or self.capital == 0:
                    self.exit = 1

                self.QminusD = self.production - self.demand  # YK
                # write consumption firm log
                self.expenditureRatio = 0
                self.orderedCapitalOverProduction = 0
                self.prevSurplus = 0
                self.surplus = 0
                self.unfilledDemand = 0
                '''Here'''

                # write consumption firm log
                self.objLogConsumptionFirm.write(str(self.objConfiguration.getConfiguration("time")) + "," + \
                                                 str(self.numID) + "," + \
                                                 str(self.liquidAsset) + "," + \
                                                 str(self.debt) + "," + \
                                                 str(self.debtRepayment) + "," + \
                                                 str(self.capital) + "," + \
                                                 str(self.desiredCapital) + "," + \
                                                 str(self.calcAverageTechA()) + "," + \
                                                 str(self.marketShare[-1]) + "," + \
                                                 str(self.competitiveness) + "," + \
                                                 str(self.demand) + "," + \
                                                 str(self.inventory) + "," + \
                                                 str(self.desiredProduction) + "," + \
                                                 str(self.production) + "," + \
                                                 str(self.investment) + "," + \
                                                 str(self.requestMachinePrice) + "," + \
                                                 str(self.requestMachineTech) + "," + \
                                                 str(self.requestMachineCnt) + "," + \
                                                 str(self.desiredLabor) + "," + \
                                                 str(self.hiredLabor) + "," + \
                                                 str(self.markUp) + "," + \
                                                 str(self.price) + "," + \
                                                 str(self.sale) + "," + \
                                                 str(self.unfilledDemand) + "," + \
                                                 str(self.startUpTime) + "," + \
                                                 str(self.approveAmount) + "," + \
                                                 str(self.loanDesired) + "," + \
                                                 str(self.prevSales)+ "\n")
                self.objLogConsumptionFirm.flush()

                if self.capital > 0:
                    self.newEntrant = False

                objEvent = endBUprocess(self.objConfiguration.getConfiguration("time"), self.ID)
                self.addOutputEvent("endBUprocess", objEvent)


    def funcInternalTransition(self):

        if self.getStateValue("state") == "PIstep":
            self.setStateValue("state", "wait")

        elif self.getStateValue("state") == "PIstep2":
            self.setStateValue("state", "wait")

        elif self.getStateValue("state") == "PHstep":
            self.setStateValue("state", "wait")

        elif self.getStateValue("state") == "MCstep":
            self.setStateValue("state", "wait")

        elif self.getStateValue("state") == 'BUstep':
            self.setStateValue("state", "wait")

    def funcTimeAdvance(self):

        if self.getStateValue("state") == "wait":
            return math.inf
        elif self.getStateValue("state") == "PIstep":
            return 1
        elif self.getStateValue("state") == "PIstep2":
            return 1
        elif self.getStateValue("state") == "PHstep":
            return 1
        elif self.getStateValue("state") == "MCstep":
            return 2
        elif self.getStateValue("state") == "BUstep":
            return 1



    def funcSelect(self):
        pass

    def calcAverageTechA(self):

        if len(self.lstCapital) > 0:
            techSum = 0
            for k in range (len(self.lstCapital)):
                tempMachine = self.lstCapital[k]
                techSum += tempMachine.techA

            return techSum / len(self.lstCapital)

        else:
            return 0

    def calcDebtRepayment(self):
        r = self.objConfiguration.getConfiguration("r")
        psi_u = self.objConfiguration.getConfiguration("psi_u")
        pr = self.objConfiguration.getConfiguration("pr")
        r_loan = (1 + psi_u) * r / 4

        monthlyRepayment = self.debt * r_loan * math.pow( 1 + r_loan, pr ) / ( math.pow( 1 + r_loan, pr ) - 1 )

        return monthlyRepayment

    def getTotalLaborDesired(self):
        if self.objMacroEcon.objHousehold.totalLaborDesired != None:
            return self.objMacroEcon.objHousehold.totalLaborDesired

        else:
            totalDesiredLabor = 0
            for i in range(len(self.objMacroEcon.lstCapitalGoodFirm)):
                tempFirm = self.objMacroEcon.lstCapitalGoodFirm[i]
                totalDesiredLabor += tempFirm.desiredLabor

            for j in range(len(self.objMacroEcon.lstConsumptionGoodFirm)):
                tempFirm = self.objMacroEcon.lstConsumptionGoodFirm[j]
                totalDesiredLabor += tempFirm.desiredLabor

            self.objMacroEcon.objHousehold.totalLaborDesired = totalDesiredLabor
            return totalDesiredLabor


    def getTotalLaborHired(self):
        if self.objMacroEcon.objHousehold.totalLaborHired != None:
            return self.objMacroEcon.objHousehold.totalLaborHired

        else:
            totalHiredLabor = 0
            for i in range(len(self.objMacroEcon.lstCapitalGoodFirm)):
                tempFirm = self.objMacroEcon.lstCapitalGoodFirm[i]
                totalHiredLabor += tempFirm.hiredLabor

            for j in range(len(self.objMacroEcon.lstConsumptionGoodFirm)):
                tempFirm = self.objMacroEcon.lstConsumptionGoodFirm[j]
                totalHiredLabor += tempFirm.hiredLabor

            self.objMacroEcon.objHousehold.totalLaborHired = totalHiredLabor
            return totalHiredLabor

    def getMarketAverageCapital(self):
        currentTime = self.objConfiguration.getConfiguration("time") - 1
        if self.objMacroEcon.marketAverageCapital[currentTime] != None:
            return self.objMacroEcon.marketAverageCapital[currentTime]

        else:
            totalCapitalSum = 0
            totalLiquidAssetSum = 0
            totalCnt = 0

            for j in range(len(self.objMacroEcon.lstConsumptionGoodFirm)):
                tempFirm = self.objMacroEcon.lstConsumptionGoodFirm[j]

                if tempFirm.newEntrant == False:
                    totalCapitalSum += tempFirm.capital
                    totalLiquidAssetSum += tempFirm.liquidAsset
                    totalCnt += 1

            averageCapital = totalCapitalSum / totalCnt
            self.objMacroEcon.marketAverageCapital[currentTime] = averageCapital

            averageLiquidAsset = totalLiquidAssetSum / totalCnt
            self.objMacroEcon.marketAverageLiquidAsset[currentTime] = averageLiquidAsset

            return averageCapital

    def getMarketLiquidAsset(self):
        currentTime = self.objConfiguration.getConfiguration("time") - 1
        if self.objMacroEcon.marketAverageLiquidAsset[currentTime] != None:
            return self.objMacroEcon.marketAverageLiquidAsset[currentTime]

        else:
            totalCapitalSum = 0
            totalLiquidAssetSum = 0
            totalCnt = 0

            for j in range(len(self.objMacroEcon.lstConsumptionGoodFirm)):
                tempFirm = self.objMacroEcon.lstConsumptionGoodFirm[j]

                if tempFirm.newEntrant == False:
                    totalCapitalSum += tempFirm.capital
                    totalLiquidAssetSum += tempFirm.liquidAsset
                    totalCnt += 1

            averageCapital = totalCapitalSum / totalCnt
            self.objMacroEcon.marketAverageCapital[currentTime] = averageCapital

            averageLiquidAsset = totalLiquidAssetSum / totalCnt
            self.objMacroEcon.marketAverageLiquidAsset[currentTime] = averageLiquidAsset

            return averageLiquidAsset


