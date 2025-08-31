from SimulationEngine.ClassicDEVS.DEVSAtomicModel import DEVSAtomicModel
from SimulationEngine.Utility.Configurator import Configurator

from MacroEconSimulation.Message.startRDprocess import startRDprocess
from MacroEconSimulation.Message.startPIprocess import startPIprocess
from MacroEconSimulation.Message.startPHprocess import startPHprocess
from MacroEconSimulation.Message.startMCprocess import startMCprocess
from MacroEconSimulation.Message.startBUprocess import startBUprocess

import math

class Operator(DEVSAtomicModel):

    def __init__(self, objConfiguration, objMacroEcon):
        super().__init__("Operator")
        self.objConfiguration = objConfiguration
        self.objMacroEcon = objMacroEcon

        self.setStateValue("operate", True)
        self.setStateValue("time", 1)   # simulation time 1 ~ T
        self.setStateValue("state", "start")  # simulation state
        self.setStateValue("numEnd", 0)  # end signal counting for each state

        self.numCapitalGoodFirm = self.objConfiguration.getConfiguration("N_Fk")
        self.numConsumptionGoodFirm = self.objConfiguration.getConfiguration("N_Fc")
        self.numBank = self.objConfiguration.getConfiguration("N_B")

        self.simTime = self.objConfiguration.getConfiguration("T")


    def funcExternalTransition(self, strPort, objEvent):
        if strPort == "endRDprocess":
            self.setStateValue("numEnd", self.getStateValue("numEnd")+1)

        elif strPort == "endPIprocess":
            self.setStateValue("numEnd", self.getStateValue("numEnd")+1)

        elif strPort == "endPHprocess":
            self.setStateValue("numEnd", self.getStateValue("numEnd")+1)

        elif strPort == "endMCprocess":
            self.setStateValue("numEnd", self.getStateValue("numEnd")+1)

        elif strPort == "endBUprocess":
            self.setStateValue("numEnd", self.getStateValue("numEnd")+1)


    def funcOutput(self):
        if self.getStateValue("state") == "start":
            objEvent = startRDprocess(self.getStateValue("time"))
            self.addOutputEvent("startRDprocess", objEvent)

        elif self.getStateValue("state") == "RDprocess" and self.getStateValue("numEnd") == self.numCapitalGoodFirm:
            objEvent = startPIprocess(self.getStateValue("time"))
            self.addOutputEvent("startPIprocess", objEvent)


        elif self.getStateValue("state") == "PIprocess" and self.getStateValue("numEnd") == self.numConsumptionGoodFirm + 1:
            objEvent = startPHprocess(self.getStateValue("time"))
            self.addOutputEvent("startPHprocess", objEvent)

        elif self.getStateValue("state") == "PHprocess" and self.getStateValue("numEnd") == self.numCapitalGoodFirm + self.numConsumptionGoodFirm:
            objEvent = startMCprocess(self.getStateValue("time"))
            self.addOutputEvent("startMCprocess", objEvent)

        elif self.getStateValue("state") == "MCprocess" and self.getStateValue("numEnd") == self.numConsumptionGoodFirm + 1:
            objEvent = startBUprocess(self.getStateValue("time"))
            self.addOutputEvent("startBUprocess", objEvent)

        elif self.getStateValue("state") == "BUprocess" and self.getStateValue("numEnd") == self.numCapitalGoodFirm + self.numConsumptionGoodFirm + 2:
            if self.getStateValue("time") != self.simTime:
                objEvent = startRDprocess(self.getStateValue("time") + 1)
                self.addOutputEvent("startRDprocess", objEvent)

    def funcInternalTransition(self):
        if self.getStateValue("state") == "start":
            self.setStateValue("state", "RDprocess")    # start Research and Development process
            self.setStateValue("numEnd", 0)

        elif self.getStateValue("state") == "RDprocess" and self.getStateValue("numEnd") == self.numCapitalGoodFirm:
            self.setStateValue("state", "PIprocess")    # start Production planning and Investment process
            self.setStateValue("numEnd", 0)

        elif self.getStateValue("state") == "PIprocess" and self.getStateValue("numEnd") == self.numConsumptionGoodFirm + 1:
            self.setStateValue("state", "PHprocess")    # start Production and Hiring process
            self.setStateValue("numEnd", 0)

        elif self.getStateValue("state") == "PHprocess" and self.getStateValue("numEnd") == self.numCapitalGoodFirm + self.numConsumptionGoodFirm:
            self.setStateValue("state", "MCprocess")
            self.setStateValue("numEnd", 0)

        elif self.getStateValue("state") == "MCprocess" and self.getStateValue("numEnd") == self.numConsumptionGoodFirm + 1:
            self.setStateValue("state", "BUprocess")
            self.setStateValue("numEnd", 0)

        elif self.getStateValue("state") == "BUprocess" and self.getStateValue("numEnd") == self.numCapitalGoodFirm + self.numConsumptionGoodFirm + 2:

            if self.getStateValue("time") == self.simTime:
                self.setStateValue("operate", False)

            else:
                self.setStateValue("time", self.getStateValue("time") + 1)
                self.objConfiguration.addConfiguration("time", self.getStateValue("time"))
                self.setStateValue("state", "RDprocess")
                self.setStateValue("numEnd", 0)


    def funcTimeAdvance(self):
        if self.getStateValue("operate"):
            if self.getStateValue("state") == "start":     # simulation start (start RD process)
                return 1
            elif self.getStateValue("state") == "RDprocess" and self.getStateValue("numEnd") == self.numCapitalGoodFirm:   # end R&D process
                return 1
            elif self.getStateValue("state") == "PIprocess" and self.getStateValue("numEnd") == self.numConsumptionGoodFirm + 1:   # end Production planning and Investment process
                return 1
            elif self.getStateValue("state") == "PHprocess" and self.getStateValue("numEnd") == self.numCapitalGoodFirm + self.numConsumptionGoodFirm:  # end Production and Hiring process
                return 1
            elif self.getStateValue("state") == "MCprocess" and self.getStateValue("numEnd") == self.numConsumptionGoodFirm + 1:    # end Market Clearing process
                return 1
            elif self.getStateValue("state") == "BUprocess" and self.getStateValue("numEnd") == self.numCapitalGoodFirm + self.numConsumptionGoodFirm + 2:    # end Balance sheet Update process
                return 1
            else:
                return math.inf
        else:
            return math.inf


    def funcSelect(self):
        pass