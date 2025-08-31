from SimulationEngine.ClassicDEVS.DEVSCoupledModel import DEVSCoupledModel
from MacroEconSimulation.Agent.CapitalGoodFirm import CapitalGoodFirm
from MacroEconSimulation.Agent.ConsumptionGoodFirm import ConsumptionGoodFirm
from MacroEconSimulation.Agent.Bank import Bank
from MacroEconSimulation.Agent.Household import Household

import os

class MacroEcon(DEVSCoupledModel):
    def __init__(self, objConfiguration):
        super().__init__("MacroEcon")
        self.objConfiguration = objConfiguration

        self.lstCapitalGoodFirm = []
        self.lstConsumptionGoodFirm = []
        self.lstSurvivedKfirm = set()

        N_Fk = self.objConfiguration.getConfiguration("N_Fk")
        N_Fc = self.objConfiguration.getConfiguration("N_Fc")
        itrNum = self.objConfiguration.getConfiguration("itrNum")
        saveDir = self.objConfiguration.getConfiguration("saveDir")

        # Logging

        logDir = os.path.join(saveDir, str(itrNum))
        if not os.path.isdir(logDir):
            os.mkdir(logDir)

        objLogCapitalFirm = open(os.path.join(logDir, 'CapitalFirmLog.csv'), 'w')
        objLogCapitalFirm.write(
            'Time,NumID,LiquidAsset,TechA,TechB,Inventory,DesiredProduction,Production,Investment,DesiredLabor,HiredLabor,Price,Sale,SaleTax,StartUp\n')

        objLogConsumptionFirm = open(os.path.join(logDir, 'ConsumptionFirmLog.csv'), 'w')
        objLogConsumptionFirm.write(
            'Time,NumID,LiquidAsset,Debt,DebtRepayment,Capital,DesiredCapital,AvgTech,MarketShare,Competitiveness,Demand,Inventory,DesiredProduction,Production,Investment,MachinePrice,MachineTech,MachineRequest,DesiredLabor,HiredLabor,MarkUp,Price,Sale,UnfilledDemand,StartUp, Exit, MPL, orderedOverNeededCapital, inventory_record, liquidityToSale, orderedCapital\n')

        objLogBank = open(os.path.join(logDir, 'BankLog.csv'), 'w')
        objLogBank.write('Time,ClientID,Type,Amount\n')

        objLogHousehold = open(os.path.join(logDir, 'Household.csv'), 'w')
        objLogHousehold.write(
            'Time,TotalProduction,NominalConsumption,RealConsumption,MarketCompetitiveness,TotalCapital,Investment,TotalCredit,AffordCredit,AverageTech,TotalDesiredLabor,TotalHiredLabor,EmploymentRate,LaborProductivity,Wage,HHI_capital,HHI_consumption,AvgLaborShare\n')

        for i in range (0, N_Fk):
            genCapitalGoodFirm = CapitalGoodFirm("CapitalGoodFirm"+str(i), i, self.objConfiguration, objLogCapitalFirm, self)
            self.lstCapitalGoodFirm.append(genCapitalGoodFirm)
            self.addModel(genCapitalGoodFirm)

        for j in range (0, N_Fc):
            genConsumptionGoodFirm = ConsumptionGoodFirm("ConsumptionGoodFirm"+str(j), j, self.objConfiguration, objLogConsumptionFirm, self)
            self.lstConsumptionGoodFirm.append(genConsumptionGoodFirm)
            self.addModel(genConsumptionGoodFirm)

        self.objBank = Bank(self.objConfiguration, objLogBank, self)
        self.addModel(self.objBank)

        self.objHousehold = Household(self.objConfiguration, objLogHousehold, self)
        self.addModel(self.objHousehold)

        T = self.objConfiguration.getConfiguration("T")

        self.marketAverageCapital = [None for x in range(T)]
        self.marketAverageLiquidAsset = [None for x in range(T)]
        self.frontierTech = [[None, None] for x in range(T)]

        # add External Coupling
        for i in range(len(self.lstCapitalGoodFirm)):
            self.addExternalInputCoupling("startRDprocess", self.lstCapitalGoodFirm[i], "startRDprocess")
            self.addExternalOutputCoupling(self.lstCapitalGoodFirm[i],"endRDprocess","endRDprocess")

            self.addExternalInputCoupling("startPHprocess", self.lstCapitalGoodFirm[i], "startPHprocess")
            self.addExternalOutputCoupling(self.lstCapitalGoodFirm[i], "endPHprocess", "endPHprocess")

            self.addExternalInputCoupling("startBUprocess", self.lstCapitalGoodFirm[i], "startBUprocess")
            self.addExternalOutputCoupling(self.lstCapitalGoodFirm[i], "endBUprocess", "endBUprocess")

        for j in range(len(self.lstConsumptionGoodFirm)):
            self.addExternalInputCoupling("startPIprocess", self.lstConsumptionGoodFirm[j], "startPIprocess")
            self.addExternalOutputCoupling(self.lstConsumptionGoodFirm[j], "endPIprocess", "endPIprocess")

            self.addExternalInputCoupling("startPHprocess", self.lstConsumptionGoodFirm[j], "startPHprocess")
            self.addExternalOutputCoupling(self.lstConsumptionGoodFirm[j], "endPHprocess", "endPHprocess")

            self.addExternalInputCoupling("startMCprocess", self.lstConsumptionGoodFirm[j], "startMCprocess")
            self.addExternalOutputCoupling(self.lstConsumptionGoodFirm[j], "endMCprocess", "endMCprocess")

            self.addExternalInputCoupling("startBUprocess", self.lstConsumptionGoodFirm[j], "startBUprocess")
            self.addExternalOutputCoupling(self.lstConsumptionGoodFirm[j], "endBUprocess", "endBUprocess")

        self.addExternalInputCoupling("startPIprocess", self.objBank, "startPIprocess")
        self.addExternalOutputCoupling(self.objBank, "endPIprocess", "endPIprocess")

        self.addExternalInputCoupling("startBUprocess", self.objBank, "startBUprocess")
        self.addExternalOutputCoupling(self.objBank, "endBUprocess", "endBUprocess")

        self.addExternalInputCoupling("startMCprocess", self.objHousehold, "startMCprocess")
        self.addExternalOutputCoupling(self.objHousehold, "endMCprocess", "endMCprocess")

        self.addExternalInputCoupling("startBUprocess", self.objHousehold, "startBUprocess")
        self.addExternalOutputCoupling(self.objHousehold, "endBUprocess", "endBUprocess")

        # add Internal Coupling
        for i in range(len(self.lstCapitalGoodFirm)):
            for j in range(len(self.lstConsumptionGoodFirm)):
                self.addInternalCoupling(self.lstCapitalGoodFirm[i], "sendBrochure_" + str(j), self.lstConsumptionGoodFirm[j], "sendBrochure")
                self.addInternalCoupling(self.lstCapitalGoodFirm[i], "sendMachine_" + str(j), self.lstConsumptionGoodFirm[j], "sendMachine")

        for j in range(len(self.lstConsumptionGoodFirm)):
            for i in range(len(self.lstCapitalGoodFirm)):
                self.addInternalCoupling(self.lstConsumptionGoodFirm[j], "requestMachine_" + str(i), self.lstCapitalGoodFirm[i], "requestMachine")

            self.addInternalCoupling(self.lstConsumptionGoodFirm[j], "requestLoan", self.objBank, "requestLoan")
            self.addInternalCoupling(self.objBank, "provideLoan_" + str(j), self.lstConsumptionGoodFirm[j], "provideLoan")
