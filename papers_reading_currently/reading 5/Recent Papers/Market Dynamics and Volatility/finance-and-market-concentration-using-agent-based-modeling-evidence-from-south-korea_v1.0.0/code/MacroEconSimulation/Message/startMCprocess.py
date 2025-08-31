class startMCprocess:

    def __init__(self, currentTime):
        self.currentTime = currentTime

    def __str__(self):
        return "< Start Market Clearing process of time "+str(self.currentTime)+">"