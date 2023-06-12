class Account:
    def __init__(self,name,accno,balance):
        self.name=name
        self.accno=accno
        self.balance=balance
        
    #creating deposit method
    def deposit(self,d):
        self.balance=self.balance+d
        
    #witdrawn method
    def withdrawn(self,w):
        if(self.balance<w):
            print("Insuuficent balace.")
        else:
            self.balance=self.balance-w
            
   #bank fees
    def bankfee(self):
        self.balance=(5/100)*self.balance
       
   
    #display method
    def display(self):
        print("Name :",self.name)
        print("AccountNumber :",self.accno)
        print("Balance :","$",self.balance)


AccNumber=Account("kurama",9983748648,786)
AccNumber.deposit(68564)
AccNumber.withdrawn(786)
AccNumber.display()

        
        