class endCLprocess:

    def __init__(self, currentTime, strID):
        self.currentTime = currentTime
        self.strID = strID

    def __str__(self):
        return "< " + self.strID +  " end Credit Loan process of time "+str(self.currentTime)+">"