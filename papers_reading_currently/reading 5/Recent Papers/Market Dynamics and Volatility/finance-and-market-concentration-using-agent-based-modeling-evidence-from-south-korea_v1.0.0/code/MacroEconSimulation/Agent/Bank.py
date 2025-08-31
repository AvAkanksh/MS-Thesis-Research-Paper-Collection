from SimulationEngine.ClassicDEVS.DEVSAtomicModel import DEVSAtomicModel
from SimulationEngine.Utility.Configurator import Configurator

from MacroEconSimulation.Message.provideLoan import provideLoan
from MacroEconSimulation.Message.endPIprocess import endPIprocess
from MacroEconSimulation.Message.endBUprocess import endBUprocess

import os
import math
import numpy as np

class Bank(DEVSAtomicModel):

    def __init__(self, objConfiguration, objLogBank, objMacroEcon):
        super().__init__("Bank")
        self.objConfiguration = objConfiguration
        self.objLogBank = objLogBank
        self.objMacroEcon = objMacroEcon

        self.lstDebtAccount = np.zeros((self.objConfiguration.getConfiguration("N_Fc")))
        self.lstOrderInfo = []
        self.totalCredit = 0
        self.mtcSoldOut = False

        self.setStateValue("state", "wait")

    def funcExternalTransition(self, strPort, objEvent):

        if strPort == "requestLoan":
            self.lstOrderInfo.append([objEvent.borrowerID, objEvent.requestAmount])

            # write bank log
            self.objLogBank.write(str(self.objConfiguration.getConfiguration("time")) + "," + \
                                  str(objEvent.borrowerID) + "," + \
                                  "request" + "," + \
                                  str(objEvent.requestAmount) + "\n")

            self.continueTimeAdvance()


        elif strPort == "startPIprocess":
            self.setStateValue("state", "PIstep")

        elif strPort == "startBUprocess":
            self.setStateValue("state", "BUstep")

    def funcOutput(self):

        # Bank credit loan providing step
        if self.getStateValue("state") == "PIstep":
            k = self.objConfiguration.getConfiguration("k")
            DSR = self.objConfiguration.getConfiguration("DSR")

            capitalGoodFirmTotalAccount = 0
            for i in range(len(self.objMacroEcon.lstCapitalGoodFirm)):
                tempFirm = self.objMacroEcon.lstCapitalGoodFirm[i]
                capitalGoodFirmTotalAccount += max(tempFirm.liquidAsset, 0)

            consumptionGoodFirmTotalAccount = 0
            for j in range(len(self.objMacroEcon.lstConsumptionGoodFirm)):
                tempFirm = self.objMacroEcon.lstConsumptionGoodFirm[j]
                consumptionGoodFirmTotalAccount += max(tempFirm.liquidAsset - tempFirm.debt, 0)

            self.marketTotalCredit = k * (capitalGoodFirmTotalAccount + consumptionGoodFirmTotalAccount)

            if len(self.lstOrderInfo) > 0:
                lstOrderPriority = []
                for k in range(len(self.lstOrderInfo)):
                    tempClientID = self.lstOrderInfo[k][0]
                    tempClient = self.objMacroEcon.lstConsumptionGoodFirm[tempClientID]
                    if tempClient.sale > 0:
                        lsrPriority = tempClient.sale#tempClient.liquidAsset / tempClient.sale
                    else:
                        lsrPriority = 0

                    lstOrderPriority.append(lsrPriority)

                lstOrderIndex = np.argsort(lstOrderPriority)[::-1]
                mtcLimit = 0
                for k in range(len(lstOrderIndex)):
                    tempClientID = self.lstOrderInfo[lstOrderIndex[k]][0]
                    requestAmount = self.lstOrderInfo[lstOrderIndex[k]][1]
                    tempClient = self.objMacroEcon.lstConsumptionGoodFirm[tempClientID]

                    DSRType = self.objConfiguration.getConfiguration('DSRType')
                    dsrLimit = 0

                    if tempClient.sale > 0 and tempClient.price is not None:
                       dsrLimit = max(DSR * tempClient.sale * tempClient.price - self.lstDebtAccount[tempClientID], 0)
                    else:
                        dsrLimit = 0
                    mtcLimit = max(self.marketTotalCredit - sum(self.lstDebtAccount), 0)
                    if mtcLimit == 0:
                        print("################ Over Market total credit!!!##########################")
                        self.mtcSoldOut = True

                    approveAmount = min(min(requestAmount, dsrLimit), mtcLimit)

                    objEvent = provideLoan(tempClientID, approveAmount)
                    self.addOutputEvent("provideLoan_" + str(tempClientID), objEvent)
                    self.lstDebtAccount[tempClientID] = self.lstDebtAccount[tempClientID] + approveAmount

                    # write bank log
                    self.objLogBank.write(str(self.objConfiguration.getConfiguration("time")) + "," + \
                                          str(tempClientID) + "," + \
                                          "approval" + "," + \
                                          str(approveAmount) + "\n")

                self.objLogBank.flush()
                self.lstOrderInfo = []

                objEvent = endPIprocess(self.objConfiguration.getConfiguration("time"), self.ID)
                self.addOutputEvent("endPIprocess", objEvent)

            else:
                objEvent = endPIprocess(self.objConfiguration.getConfiguration("time"), self.ID)
                self.addOutputEvent("endPIprocess", objEvent)


        elif self.getStateValue("state") == 'BUstep':
            self.currentDebtApproval = 0

            objEvent = endBUprocess(self.objConfiguration.getConfiguration("time"), self.ID)
            self.addOutputEvent("endBUprocess", objEvent)

    def funcInternalTransition(self):

        if self.getStateValue("state") == "PIstep":
            self.setStateValue("state", "wait")

        elif self.getStateValue("state") == 'BUstep':
            self.setStateValue("state", "wait")

    def funcTimeAdvance(self):
        if self.getStateValue("state") == "wait":
            return math.inf
        elif self.getStateValue("state") == "PIstep":
            return 2
        elif self.getStateValue("state") == "BUstep":
            return 3


    def funcSelect(self):
        pass


    def getTotalCredit(self):
        totalCredit = sum(self.lstDebtAccount)

        return totalCredit

    def DebtRepaymentConstant(self):
        r = self.objConfiguration.getConfiguration("r")
        psi_u = self.objConfiguration.getConfiguration("psi_u")
        pr = self.objConfiguration.getConfiguration("pr")
        r_loan = (1 + psi_u) * r / 4

        return r_loan * math.pow(1 + r_loan, pr) / (math.pow(1 + r_loan, pr) - 1)

