class requestMachine:

    def __init__(self, buyerID, requestAmount):
        self.buyerID = buyerID
        self.requestAmount = requestAmount

    def __str__(self):
        return "< Consumption good firm " + str(self.buyerID) +  " requests " + str(self.requestAmount)+ " machine(s) >"