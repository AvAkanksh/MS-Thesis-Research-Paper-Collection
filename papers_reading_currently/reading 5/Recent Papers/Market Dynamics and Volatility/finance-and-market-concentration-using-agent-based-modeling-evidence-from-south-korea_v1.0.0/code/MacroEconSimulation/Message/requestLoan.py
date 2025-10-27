class requestLoan:

    def __init__(self, borrowerID, requestAmount):
        self.borrowerID = borrowerID
        self.requestAmount = requestAmount

    def __str__(self):
        return "< Consumption good firm " + str(self.borrowerID) +  " requests " + str(self.requestAmount)+ " loan amount >"