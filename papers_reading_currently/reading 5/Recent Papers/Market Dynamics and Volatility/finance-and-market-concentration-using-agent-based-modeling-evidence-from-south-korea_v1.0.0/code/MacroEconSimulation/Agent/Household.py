from SimulationEngine.ClassicDEVS.DEVSAtomicModel import DEVSAtomicModel
from SimulationEngine.Utility.Configurator import Configurator

from MacroEconSimulation.Message.endMCprocess import endMCprocess
from MacroEconSimulation.Message.endBUprocess import endBUprocess


import os
import math
import numpy as np

class Household(DEVSAtomicModel):

    def __init__(self, objConfiguration, objLogHousehold, objMacroEcon):
        super().__init__("Household")
        self.objConfiguration = objConfiguration
        self.objLogHousehold = objLogHousehold
        self.objMacroEcon = objMacroEcon

        N_H = self.objConfiguration.getConfiguration("N_H")
        self.householdNum = N_H

        self.totalLaborDesired = None
        self.totalLaborHired = None
        self.marketCompetitiveness = None
        self.wage = 1

        self.prevLaborProductivity = None
        self.laborProductivity = None

        self.prevEmploymentRate = None
        self.employmentRate = None

        self.totalConsumption = 0
        self.realConsumption = 0
        self.totalInvestment = 0

        self.HHI_capital = 0
        self.HHI_consumption = 0

        self.setStateValue("state", "wait")

    def funcExternalTransition(self, strPort, objEvent):

        if strPort == 'startMCprocess':
            self.setStateValue("state", "MCstep")

        elif strPort == "startBUprocess":

            self.prevLaborProductivity = self.laborProductivity
            self.laborProductivity = self.calcAvgLaborProductivity()
            self.realConsumption = self.getRealConsumption()
            self.totalInvestment = self.getTotalInvestment()

            self.prevEmploymentRate = self.employmentRate
            self.employmentRate = self.totalLaborHired / self.householdNum

            self.HHI_capital = self.getHHI_capital()
            self.HHI_consumption = self.getHHI_consumption()

            ###YK
            self.realWage = self.wage / self.price
            self.hireOverProduction = self.totalWageConsumption / (self.wage * self.totalConsumptionY)

            self.laborShare = self.totalWageConsumption / self.totalY
            self.UnitCostOfProduction = self.laborShare * self.price
            ###YK

            self.setStateValue("state", "BUstep")

    def funcOutput(self):

        if self.getStateValue("state") == "MCstep":

            phi = self.objConfiguration.getConfiguration("phi") # Unemployment subsidy rate

            totalHiredLabor_capital = 0
            for i in range(len(self.objMacroEcon.lstCapitalGoodFirm)):
                tempFirm = self.objMacroEcon.lstCapitalGoodFirm[i]
                totalHiredLabor_capital += tempFirm.hiredLabor

            totalHiredLabor_comsumption = 0
            for j in range(len(self.objMacroEcon.lstConsumptionGoodFirm)):
                tempFirm = self.objMacroEcon.lstConsumptionGoodFirm[j]
                totalHiredLabor_comsumption += tempFirm.hiredLabor


            self.totalLaborHired = totalHiredLabor_capital + totalHiredLabor_comsumption

            self.totalWageConsumption = self.wage * totalHiredLabor_comsumption
            self.totalWage = self.wage * self.totalLaborHired
            self.totalSubsidy = phi * self.wage * (self.householdNum - self.totalLaborHired)
            self.totalConsumption = self.totalWage + self.totalSubsidy

            # calculate market average competitiveness
            lstFirmCompetitiveness = []
            marketShareSum = 0

            for j in range(len(self.objMacroEcon.lstConsumptionGoodFirm)):
                tempFirm = self.objMacroEcon.lstConsumptionGoodFirm[j]
                if tempFirm.newEntrant == False:
                    lstFirmCompetitiveness.append(tempFirm.competitiveness * tempFirm.marketShare[-1])
                    marketShareSum += tempFirm.marketShare[-1]

            self.marketCompetitiveness = np.sum(lstFirmCompetitiveness) / marketShareSum

            # update market share
            chi = self.objConfiguration.getConfiguration("chi")

            lstUpdateMarketShare = []
            updateMarketShareSum = 0
            for j in range(len(self.objMacroEcon.lstConsumptionGoodFirm)):
                tempFirm = self.objMacroEcon.lstConsumptionGoodFirm[j]
                if tempFirm.newEntrant == False:
                    tempMarketShare = tempFirm.marketShare[-1]
                    tempCompetitiveness = tempFirm.competitiveness
                    updateMarketShare = max(tempMarketShare * (1 + chi * (tempCompetitiveness - self.marketCompetitiveness) / abs(self.marketCompetitiveness)), 0)

                    lstUpdateMarketShare.append(updateMarketShare)
                    updateMarketShareSum += updateMarketShare

                elif tempFirm.newEntrant == True:
                    lstUpdateMarketShare.append(0)

            lstUpdateMarketShare = lstUpdateMarketShare / updateMarketShareSum

            for j in range(len(self.objMacroEcon.lstConsumptionGoodFirm)):
                tempFirm = self.objMacroEcon.lstConsumptionGoodFirm[j]
                if tempFirm.newEntrant == False:
                    tempFirm.marketShare.append(lstUpdateMarketShare[j])

            objEvent = endMCprocess(self.objConfiguration.getConfiguration("time"), self.ID)
            self.addOutputEvent("endMCprocess", objEvent)

        elif self.getStateValue("state") == "BUstep":

            psi_1 = self.objConfiguration.getConfiguration("psi_1")
            psi_2 = self.objConfiguration.getConfiguration("psi_2")
            psi_3 = self.objConfiguration.getConfiguration("psi_3")
            g = self.objConfiguration.getConfiguration("g")

            if self.prevLaborProductivity != None and self.prevEmploymentRate != None:
                self.wage = self.wage * (1 + psi_1 * (self.laborProductivity - self.prevLaborProductivity) / self.prevLaborProductivity + psi_2 * (self.employmentRate - self.prevEmploymentRate) / self.prevEmploymentRate)
            else:
                self.wage = self.wage

            # write household log
            self.objLogHousehold.write(str(self.objConfiguration.getConfiguration("time")) + "," + \
                                       str(self.totalConsumptionY) + "," + \
                                       str(self.totalConsumption) + "," + \
                                       str(self.realConsumption) + "," + \
                                       str(self.marketCompetitiveness) + "," + \
                                       str(self.totalCapital) + "," + \
                                       str(self.totalInvestment) + "," + \
                                       str(self.objMacroEcon.objBank.getTotalCredit()) + "," + \
                                       str(self.objMacroEcon.objBank.marketTotalCredit) + "," + \
                                       str(self.estTech) + "," + \
                                       str(self.totalLaborDesired) + "," + \
                                       str(self.totalLaborHired) + "," + \
                                       str(self.totalLaborHired / self.householdNum) + "," + \
                                       str(self.laborProductivity) + "," + \
                                       str(self.wage) + "," + \
                                       str(self.HHI_capital) + "," + \
                                       str(self.HHI_consumption) + "," + \
                                       str(self.laborShare) + "," + \
                                       str(self.hireOverProduction) + "," + \
                                       str(self.realWage) + "," + \
                                       str(self.price) + "," + \
                                       str(self.UnitCostOfProduction) + "," + \
                                       str(self.objMacroEcon.objBank.mtcSoldOut) + "\n")

            self.objLogHousehold.flush()

            self.totalLaborDesired = None
            self.totalLaborHired = None
            self.marketCompetitiveness = None

            self.householdNum = int(round(self.householdNum * (1 + g / 100)))
            self.objConfiguration.addConfiguration("N_H", self.householdNum)

            objEvent = endBUprocess(self.objConfiguration.getConfiguration("time"), self.ID)
            self.addOutputEvent("endBUprocess", objEvent)


    def funcInternalTransition(self):

        if self.getStateValue("state") == "MCstep":
            self.setStateValue("state", "wait")

        elif self.getStateValue("state") == 'BUstep':
            self.setStateValue("state", "wait")


    def funcTimeAdvance(self):
        if self.getStateValue("state") == "wait":
            return math.inf
        elif self.getStateValue("state") == "MCstep":
            return 1
        elif self.getStateValue("state") == "BUstep":
            return 2


    def funcSelect(self):
        pass


    def calcAvgLaborProductivity(self):

        alpha = self.objConfiguration.getConfiguration("alpha")
        totalY = 0
        totalConsumptionY = 0
        totalCapital = 0

        lstCapitalGoodFirm = self.objMacroEcon.lstCapitalGoodFirm
        for i in range(len(lstCapitalGoodFirm)):
            tempCapitalGoodFirm = lstCapitalGoodFirm[i]
            # totalY += tempCapitalGoodFirm.price * tempCapitalGoodFirm.production

        lstConsumptionGoodFirm = self.objMacroEcon.lstConsumptionGoodFirm
        cnt = 0
        for j in range(len(lstConsumptionGoodFirm)):
            tempConsumptionGoodFirm = lstConsumptionGoodFirm[j]
            if tempConsumptionGoodFirm.newEntrant == False and tempConsumptionGoodFirm.price is not None:
                cnt += 1
                totalY += tempConsumptionGoodFirm.price * tempConsumptionGoodFirm.production
                totalConsumptionY += tempConsumptionGoodFirm.production
                totalCapital += tempConsumptionGoodFirm.capital
        if cnt !=0:
            self.price = totalY / totalConsumptionY # price weighted over each firm's production


        totalLabor = self.totalLaborHired

        estTech = totalConsumptionY / (pow(totalCapital, alpha) * pow(totalLabor, 1-alpha))
        avgLaborProductivity = (1-alpha) * estTech * pow(totalCapital/totalLabor, alpha)


        self.totalCapital = totalCapital
        self.totalConsumptionY = totalConsumptionY
        self.estTech = estTech
        self.totalY = totalY

        return avgLaborProductivity

    def getRealConsumption(self):
        lstSale = []
        lstConsumptionGoodFirm = self.objMacroEcon.lstConsumptionGoodFirm

        for j in range(len(lstConsumptionGoodFirm)):
            tempConsumptionGoodFirm = lstConsumptionGoodFirm[j]
            lstSale.append(tempConsumptionGoodFirm.sale)

        realConsumption = np.sum(lstSale)

        return realConsumption

    def getTotalTaxation(self):
        totalSaleTax = 0

        lstCapitalGoodFirm = self.objMacroEcon.lstCapitalGoodFirm
        for i in range(len(lstCapitalGoodFirm)):
            tempCapitalGoodFirm = lstCapitalGoodFirm[i]
            totalSaleTax += tempCapitalGoodFirm.saleTax

        lstConsumptionGoodFirm = self.objMacroEcon.lstConsumptionGoodFirm
        for j in range(len(lstConsumptionGoodFirm)):
            tempConsumptionGoodFirm = lstConsumptionGoodFirm[j]
            totalSaleTax += tempConsumptionGoodFirm.saleTax

        return totalSaleTax

    def getTotalInvestment(self):
        totalInvestment = 0

        lstConsumptionGoodFirm = self.objMacroEcon.lstConsumptionGoodFirm
        for j in range(len(lstConsumptionGoodFirm)):
            tempConsumptionGoodFirm = lstConsumptionGoodFirm[j]
            totalInvestment += tempConsumptionGoodFirm.investment * tempConsumptionGoodFirm.requestMachinePrice

        return totalInvestment


    def getHHI_capital(self):
        lstMarketShare = []

        lstCapitalGoodFirm = self.objMacroEcon.lstCapitalGoodFirm
        for i in range(len(lstCapitalGoodFirm)):
            tempCapitalGoodFirm = lstCapitalGoodFirm[i]
            lstMarketShare.append(tempCapitalGoodFirm.price * tempCapitalGoodFirm.sale)

        HHI_capital = 0
        lstMarketShare = lstMarketShare / sum(lstMarketShare)

        for i in range(len(lstMarketShare)):
            HHI_capital += pow(lstMarketShare[i], 2)

        return HHI_capital


    def getHHI_consumption(self):
        lstMarketShare = []

        lstConsumptionGoodFirm = self.objMacroEcon.lstConsumptionGoodFirm
        for j in range(len(lstConsumptionGoodFirm)):
            tempConsumptionGoodFirm = lstConsumptionGoodFirm[j]
            if tempConsumptionGoodFirm.newEntrant == False:
                lstMarketShare.append(tempConsumptionGoodFirm.marketShare[-1])

        HHI_consumption = 0
        lstMarketShare = lstMarketShare / np.sum(lstMarketShare)

        for j in range(len(lstMarketShare)):
            HHI_consumption += pow(lstMarketShare[j], 2)

        return HHI_consumption