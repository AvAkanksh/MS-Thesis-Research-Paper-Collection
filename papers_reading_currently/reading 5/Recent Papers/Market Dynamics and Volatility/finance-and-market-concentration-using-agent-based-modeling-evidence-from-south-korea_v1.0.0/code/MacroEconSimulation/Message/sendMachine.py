class sendMachine:

    def __init__(self, sellerID, machineAmount, techA, price):
        self.sellerID = sellerID
        self.machineAmount = machineAmount
        self.techA = techA
        self.price = price


    def __str__(self):
        return  "< Machine sending >"