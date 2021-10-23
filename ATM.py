class atm:
    def __init__(self, cardNum, pinNum):
        self.cardNum = cardNum
        self.pinNum = pinNum

    def enterInfo(self):
        card = input('Enter Card Number: ')
        pin = input('Enter Pin Number: ')
    
    def balanceEnquiry(self, balance):
        print('Your account balance is ', balance)
     
    def cashWithdrawl(self, cash):
        print(cash, ' has been withdrawn from your account')

account = atm(1234567812345678, 1234,)
account.balanceEnquiry(1000000)
account.cashWithdrawl(100)