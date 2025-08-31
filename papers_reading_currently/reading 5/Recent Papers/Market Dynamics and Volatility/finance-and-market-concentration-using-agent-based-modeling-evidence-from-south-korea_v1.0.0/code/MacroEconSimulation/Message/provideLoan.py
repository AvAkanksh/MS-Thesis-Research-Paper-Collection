class provideLoan:

    def __init__(self, borrowerID, approveAmount):
        self.borrowerID = borrowerID
        self.approveAmount = approveAmount

    def __str__(self):
        return "< Bank approves " + str(self.approveAmount) +  " credit loan amount to consumption good firm " + str(self.borrowerID)+ " >"