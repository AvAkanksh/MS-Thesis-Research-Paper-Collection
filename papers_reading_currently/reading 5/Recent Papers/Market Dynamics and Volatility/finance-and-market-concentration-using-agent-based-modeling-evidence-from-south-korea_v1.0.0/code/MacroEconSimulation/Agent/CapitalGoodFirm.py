from SimulationEngine.ClassicDEVS.DEVSAtomicModel import DEVSAtomicModel
from SimulationEngine.Utility.Configurator import Configurator

from MacroEconSimulation.Message.endRDprocess import endRDprocess
from MacroEconSimulation.Message.sendBrochure import sendBrochure
from MacroEconSimulation.Message.endPHprocess import endPHprocess
from MacroEconSimulation.Message.sendMachine import sendMachine
from MacroEconSimulation.Message.endBUprocess import endBUprocess

import os
import math
import numpy as np
import random

class CapitalGoodFirm(DEVSAtomicModel):

    def __init__(self, strID, numID, objConfiguration, objLogCapitalFirm, objMacroEcon):
        super().__init__(strID)

        self.strID = strID
        self.numID = numID
        self.objConfiguration = objConfiguration
        self.objMacroEcon = objMacroEcon
        self.objLogCapitalFirm = objLogCapitalFirm
        self.startUpTime = 0
        self.newEntrant = False

        # about balance sheet
        initCashAvg = 50
        initCashStd = 0.2 * initCashAvg
        self.liquidAsset = np.random.uniform(initCashAvg-initCashStd, initCashAvg+initCashStd, 1)[0]


        # about technology
        techAAvg = 1
        techAStd = 0.2 * techAAvg
        self.techA = np.random.uniform(techAAvg-techAStd, techAAvg+techAStd, 1)[0]  # stands for consumption good productivity of the machine

        alpha = self.objConfiguration.getConfiguration("alpha")
        eta = self.objConfiguration.getConfiguration("eta")
        mu1 = self.objConfiguration.getConfiguration("mu1")

        techBAvg = (1 - alpha) * (1 + mu1) / (alpha * eta)
        techBStd = 0.2 * techBAvg
        self.techB = np.random.uniform(techBAvg-techBStd, techBAvg+techBStd, 1)[0]  # stands for machine productivity

        # about production
        self.inventory = 0
        self.desiredProduction = 0
        self.production = 0

        # about investment
        self.investmentAmount = 0

        # about labor
        self.desiredLabor = 0
        self.hiredLabor = 0

        # about sale
        self.markUp = mu1
        self.price = 0
        self.sale = 0
        self.saleTax = 0
        self.lstHistSale = [None, None]

        self.lstClient = []
        self.lstOrderInfo = []

        self.setStateValue("state", "wait")


    def funcExternalTransition(self, strPort, objEvent):

        # Captial good firm RD step (1)
        if strPort == "startRDprocess":

            if self.newEntrant == True:
                t = self.objConfiguration.getConfiguration("time")
                wage = self.objMacroEcon.objHousehold.wage
                self.startUpTime = t

                # about balance sheet
                initCashAvg = 50 * wage
                initCashStd = 0.2 * initCashAvg
                self.liquidAsset = np.random.uniform(initCashAvg - initCashStd, initCashAvg + initCashStd, 1)[0]

                # about technology
                [Amax, Bmax] = self.getFrontierTech()
                alpha2 = 4
                beta2 = 2

                self.techA = Amax * np.random.beta(alpha2, beta2, 1)[0] # stands for consumption good productivity of the machine
                self.techB = Bmax * np.random.beta(alpha2, beta2, 1)[0] # stands for machine productivity

                # about production
                self.inventory = 0
                self.desiredProduction = 0
                self.production = 0

                # about investment
                self.investmentAmount = 0

                # about labor
                self.desiredLabor = 0
                self.hiredLabor = 0

                # about sale
                mu1 = self.objConfiguration.getConfiguration("mu1")

                self.markUp = mu1
                self.price = 0
                self.sale = 0
                self.saleTax = 0
                self.lstHistSale = [None, None]

                self.lstClient = []
                self.lstOrderInfo = []

                self.newEntrant = False

            nu = self.objConfiguration.getConfiguration("nu")   # R&D investment propensity
            xi = self.objConfiguration.getConfiguration("xi")   # R&D allocation to innovative search
            zeta1 = self.objConfiguration.getConfiguration("zeta1")     # Innovation success rate
            zeta2 = self.objConfiguration.getConfiguration("zeta2")     # imitation success rate
            alpha1 = self.objConfiguration.getConfiguration("alpha1")  # Beta distribution parameter for innovation (alpha1)
            beta1 = self.objConfiguration.getConfiguration("beta1")  # Beta distribution parameter for innovation (beta1)
            x1_lower = self.objConfiguration.getConfiguration("x1_lower")  # Beta distribution support for innovation (x1_lower)
            x1_upper = self.objConfiguration.getConfiguration("x1_upper")  # Beta distribution support for innovation (x1_upper)

            self.investmentAmount = nu * self.sale * self.price
            currTech = math.sqrt(pow(self.techA,2) + pow(self.techB,2))
            # innovation step
            investment_In = self.investmentAmount * xi
            succProb_In = 1 - math.exp(-zeta1*investment_In/currTech)
            if random.uniform(0, 1) <= succProb_In:
                self.techA_In = self.techA * (1 + self.betaDistSamplingwithSupport(alpha1, beta1, x1_lower, x1_upper)/currTech)
                self.techB_In = self.techB * (1 + self.betaDistSamplingwithSupport(alpha1, beta1, x1_lower, x1_upper)/currTech)
            else:
                self.techA_In = self.techA
                self.techB_In = self.techB

            # imitation step
            investment_Im = self.investmentAmount * (1 - xi)
            succProb_Im = 1 - math.exp(-zeta2*investment_Im/currTech)
            if random.uniform(0, 1) <= succProb_Im:
                lstTech = []
                lstWeight = []
                lstCapitalGoodFirm = self.objMacroEcon.lstCapitalGoodFirm

                for i in range(len(lstCapitalGoodFirm)):
                    selectCapitalGoodFirm = lstCapitalGoodFirm[i]
                    if self.numID != selectCapitalGoodFirm.numID:
                        selectTechA = selectCapitalGoodFirm.techA
                        selectTechB = selectCapitalGoodFirm.techB
                        if self.techA != selectTechA or self.techB != selectTechB:
                            lstTech.append([selectTechA, selectTechB])
                            lstWeight.append(1/math.sqrt(pow(self.techA-selectTechA, 2)+pow(self.techB-selectTechB, 2)))

                sampleIndex = self.weightSampling(lstWeight)
                self.techA_Im = lstTech[sampleIndex][0]
                self.techB_Im = lstTech[sampleIndex][1]
            else:
                self.techA_Im = self.techA
                self.techB_Im = self.techB

            self.setStateValue("state", "RDstep")


        elif strPort == "requestMachine":
            self.lstOrderInfo.append([objEvent.buyerID, objEvent.requestAmount])


        elif strPort == "startPHprocess":
            wage = self.objMacroEcon.objHousehold.wage

            totalOrderAmount = 0
            for k in range(len(self.lstOrderInfo)):
                totalOrderAmount += self.lstOrderInfo[k][1]

            self.desiredProduction = totalOrderAmount

            tempLaborNeed = math.ceil(max(self.desiredProduction - self.inventory, 0) / self.techB)
            tempLaborAfford = max(math.floor(self.liquidAsset / wage), 0)

            self.desiredLabor = min(tempLaborNeed, tempLaborAfford)

            self.setStateValue("state", "PHstep")

        elif strPort == "startBUprocess":
            self.setStateValue("state", "BUstep")


    def funcOutput(self):

        # Capital good firm RD step (2)
        if self.getStateValue("state") == "RDstep":
            wage = self.objMacroEcon.objHousehold.wage

            b = self.objConfiguration.getConfiguration("b")  # Payback period
            mc = self.objConfiguration.getConfiguration("mc")   # Min client
            gamma = self.objConfiguration.getConfiguration("gamma") # NC sample parameter

            # Technology selection
            techScore_Curr = (1 + self.markUp) * (wage / self.techB) + b * (wage / self.techA)
            techScore_In = (1 + self.markUp) * (wage / self.techB_In) + b * (wage / self.techA_In)
            techScore_Im = (1 + self.markUp) * (wage / self.techB_Im) + b * (wage / self.techA_Im)

            if techScore_In <= techScore_Curr and techScore_In <= techScore_Im:
                self.techA = self.techA_In
                self.techB = self.techB_In
            elif techScore_Im <= techScore_Curr and techScore_Im <= techScore_In:
                self.techA = self.techA_Im
                self.techB = self.techB_Im

            self.price = (1 + self.markUp) * wage / self.techB

            # Brochure sending target firm sampling
            lstTarget = []
            for j in range (len(self.objMacroEcon.lstConsumptionGoodFirm)):
                tempFirm = self.objMacroEcon.lstConsumptionGoodFirm[j]
                if tempFirm.numID not in self.lstClient:
                    lstTarget.append(tempFirm.numID)

            self.numNC = int(max(gamma * len(self.lstClient), mc - len(self.lstClient)))

            if self.numNC < 0:
                self.lstNC = []
            else:
                if len(lstTarget) >= self.numNC:
                    lstNC = random.sample(lstTarget, self.numNC)
                else:
                    lstNC = lstTarget

            objEvent = sendBrochure(self.numID, self.techA, self.price)
            for j in range (len(self.lstClient)):
                clientNumID = self.lstClient[j]
                self.addOutputEvent("sendBrochure_"+str(clientNumID), objEvent)

            for j in range(len(lstNC)):
                clientNumID = lstNC[j]
                self.addOutputEvent("sendBrochure_" + str(clientNumID), objEvent)

            self.lstClient = []
            self.sale = 0

            objEvent = endRDprocess(self.objConfiguration.getConfiguration("time"), self.strID)
            self.addOutputEvent("endRDprocess", objEvent)

        # Capital good firm PH step
        elif self.getStateValue("state") == "PHstep":
            N_H = self.objConfiguration.getConfiguration("N_H")

            totalLaborDemand = self.getTotalLaborDesired()
            if totalLaborDemand > N_H:
                self.hiredLabor = math.floor(self.desiredLabor * N_H / totalLaborDemand)
            else:
                self.hiredLabor = self.desiredLabor

            self.production = self.hiredLabor * self.techB
            self.inventory += self.production

            if self.desiredProduction > 0:
                if self.inventory >= self.desiredProduction:
                    for j in range(len(self.lstOrderInfo)):
                        tempClient = self.lstOrderInfo[j][0]
                        tempRequestAmount = self.lstOrderInfo[j][1]

                        sendingAmount = tempRequestAmount
                        objEvent = sendMachine(self.numID, sendingAmount, self.techA, self.price)
                        self.addOutputEvent("sendMachine_" + str(tempClient), objEvent)
                        self.inventory -= sendingAmount
                        self.lstClient.append(tempClient)

                else:
                    proportion = self.inventory / self.desiredProduction
                    for j in range(len(self.lstOrderInfo)):
                        tempClient = self.lstOrderInfo[j][0]
                        tempRequestAmount = self.lstOrderInfo[j][1]

                        sendingAmount = int(math.floor(tempRequestAmount * proportion))
                        if sendingAmount > 0:
                            objEvent = sendMachine(self.numID, sendingAmount, self.techA, self.price)
                            self.addOutputEvent("sendMachine_" + str(tempClient), objEvent)
                            self.inventory -= sendingAmount
                            if random.random() < proportion:
                                self.lstClient.append(tempClient)

            self.lstOrderInfo = []

            objEvent = endPHprocess(self.objConfiguration.getConfiguration("time"), self.strID)
            self.addOutputEvent("endPHprocess", objEvent)

        elif self.getStateValue("state") == 'BUstep':

            r = self.objConfiguration.getConfiguration("r")
            psi_d = self.objConfiguration.getConfiguration("psi_d")
            tr = self.objConfiguration.getConfiguration("tr")

            r_deposit = ( 1 - psi_d ) * r / 4
            wage = self.objMacroEcon.objHousehold.wage

            netSale = self.price * self.sale - wage * self.hiredLabor - self.investmentAmount
            if netSale > 0:
                self.saleTax = netSale * tr
            else:
                self.saleTax = 0

            if self.liquidAsset > 0:
                interest = self.liquidAsset * r_deposit
            else:
                interest = 0

            self.liquidAsset = self.liquidAsset + netSale + interest - self.saleTax

            # write capital firm log
            self.objLogCapitalFirm.write(str(self.objConfiguration.getConfiguration("time")) + "," + \
                                   str(self.numID) + "," + \
                                   str(self.liquidAsset) + "," + \
                                   str(self.techA) + "," + \
                                   str(self.techB) + "," + \
                                   str(self.inventory) + "," + \
                                   str(self.desiredProduction) + "," + \
                                   str(self.production) + "," + \
                                   str(self.investmentAmount) + "," + \
                                   str(self.desiredLabor) + "," + \
                                   str(self.hiredLabor) + "," + \
                                   str(self.price) + "," + \
                                   str(self.sale) + "," + \
                                   str(self.saleTax) + "," + \
                                   str(self.startUpTime) + "\n")
            self.objLogCapitalFirm.flush()


            if self.sale == 0:
                if self.lstHistSale[-1] == 0 and self.lstHistSale[-2] == 0:
                    self.newEntrant = True
                self.objMacroEcon.lstSurvivedKfirm.discard(self.numID)
            else:
                self.objMacroEcon.lstSurvivedKfirm.add(self.numID)

            self.lstHistSale.append(self.sale)

            objEvent = endBUprocess(self.objConfiguration.getConfiguration("time"), self.ID)
            self.addOutputEvent("endBUprocess", objEvent)


    def funcInternalTransition(self):

        if self.getStateValue("state") == "RDstep":
            self.setStateValue("state", "wait")

        elif self.getStateValue("state") == "PHstep":
            self.setStateValue("state", "wait")

        elif self.getStateValue("state") == 'BUstep':
            self.setStateValue("state", "wait")

    def funcTimeAdvance(self):

        if self.getStateValue("state") == "wait":
            return math.inf
        elif self.getStateValue("state") == "RDstep":
            return 1
        elif self.getStateValue("state") == "PHstep":
            return 2
        elif self.getStateValue("state") == "BUstep":
            return 1



    def funcSelect(self):
        pass


    def betaDistSamplingwithSupport(self, alpha, beta, support_lower, support_upper):
        tempValue = math.inf
        while tempValue > -support_lower and tempValue > support_upper:
            tempValue = np.random.beta(alpha, beta, 1)[0]
            if tempValue <= -support_lower and tempValue > support_upper:
                return -tempValue
            elif tempValue <= support_upper and tempValue > -support_lower:
                return tempValue
            elif tempValue <= -support_lower and tempValue <= support_upper:
                if random.uniform(0,1) <= 0.5:
                    return tempValue
                else:
                    return -tempValue

    def weightSampling(self, weightVector):
        normalizedWeightVector = [x / sum(weightVector) for x in weightVector]
        selectNum = int(np.argwhere(np.random.multinomial(1, normalizedWeightVector) == 1))
        return selectNum

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

    def getFrontierTech(self):
        currentTime = self.objConfiguration.getConfiguration("time") - 1
        if self.objMacroEcon.frontierTech[currentTime][0] != None and self.objMacroEcon.frontierTech[currentTime][1] != None :
            return self.objMacroEcon.frontierTech[currentTime]

        else:
            Amax = 0
            Bmax = 0
            for i in range(len(self.objMacroEcon.lstCapitalGoodFirm)):
                tempFirm = self.objMacroEcon.lstCapitalGoodFirm[i]
                if tempFirm.techA > Amax:
                    Amax = tempFirm.techA
                if tempFirm.techB > Bmax:
                    Bmax = tempFirm.techB

            self.objMacroEcon.frontierTech[currentTime] = [Amax, Bmax]
            return [Amax, Bmax]