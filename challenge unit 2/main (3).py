class Bankaccount:
  def __init__(self,account_holderName,account_num,account_bal):
    self.__account_holderName = account_holderName
    self.__account_num = account_num
    self.__account_bal = account_bal
  def deposit(self,amount):
    if amount > 0:
      self.__account_bal += amount
      print("deposited :")
      print("Successfully deposited = $",amount)
    else:
      print("unable to deposit")
  def withdraw(self,amount):
    if amount > 0 and amount <= self.__account_bal:
      self.__account_bal -= amount
      print("Withdrawn :")
      print("You have successfully withdrawn = $",amount)
    else:
      print("insufficient balance")
  def display(self):
    print("Account details:")
    print("account Holder Name = ",self.__account_holderName)
    print("account Number = ",self.__account_num)
    print("account Balance = ",self.__account_bal)


obj=Bankaccount(account_holderName="Nandhitha",account_num="12345",account_bal=5000)

obj.display()
obj.deposit(2000)
obj.withdraw(4000)
obj.display()
