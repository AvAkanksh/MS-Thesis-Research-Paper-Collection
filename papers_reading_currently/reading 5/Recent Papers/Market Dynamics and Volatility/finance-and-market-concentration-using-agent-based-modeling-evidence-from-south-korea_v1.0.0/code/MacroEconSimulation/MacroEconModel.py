from SimulationEngine.ClassicDEVS.DEVSCoupledModel import DEVSCoupledModel
from MacroEconSimulation.Agent.Operator import Operator
from MacroEconSimulation.MacroEcon import MacroEcon

class MacroEconModel(DEVSCoupledModel):
    def __init__(self, objConfiguration):
        super().__init__("MacroEconModel")

        self.objMacroEcon = MacroEcon(objConfiguration)
        self.addModel(self.objMacroEcon)  # Simulation Engine registered

        self.objOperator = Operator(objConfiguration, self.objMacroEcon)
        self.addModel(self.objOperator)  # Simulation Engine registered

        self.addInternalCoupling(self.objOperator, "startRDprocess", self.objMacroEcon, "startRDprocess")
        self.addInternalCoupling(self.objMacroEcon, "endRDprocess", self.objOperator, "endRDprocess")

        self.addInternalCoupling(self.objOperator, "startPIprocess", self.objMacroEcon, "startPIprocess")
        self.addInternalCoupling(self.objMacroEcon, "endPIprocess", self.objOperator, "endPIprocess")

        self.addInternalCoupling(self.objOperator, "startPHprocess", self.objMacroEcon, "startPHprocess")
        self.addInternalCoupling(self.objMacroEcon, "endPHprocess", self.objOperator, "endPHprocess")

        self.addInternalCoupling(self.objOperator, "startMCprocess", self.objMacroEcon, "startMCprocess")
        self.addInternalCoupling(self.objMacroEcon, "endMCprocess", self.objOperator, "endMCprocess")

        self.addInternalCoupling(self.objOperator, "startBUprocess", self.objMacroEcon, "startBUprocess")
        self.addInternalCoupling(self.objMacroEcon, "endBUprocess", self.objOperator, "endBUprocess")

        self.lstSurvivedKfirm = self.objMacroEcon.lstSurvivedKfirm