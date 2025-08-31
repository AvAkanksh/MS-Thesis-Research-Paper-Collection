import numpy as np

class Machine:

    def __init__(self, ojbConfiguration, techA, age, cost):
        self.techA = techA
        self.age = age
        self.lifeSpan = ojbConfiguration.getConfiguration("eta")
        self.cost = cost / self.lifeSpan
        self.machineScrapDummy = False

    def machineAging(self):
        self.age = self.age + 1
    def machineScrap(self):
        self.machineScrapDummy= True
