class endPHprocess:

    def __init__(self, currentTime, strID):
        self.currentTime = currentTime
        self.strID = strID

    def __str__(self):
        return "< " + self.strID +  " End Production and Hiring process of time "+str(self.currentTime)+">"