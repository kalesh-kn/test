# -*- coding: utf-8 -*-
"""day2

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10NgYYoMD4NzHzWgERqbbdCshxrrAbMzh
"""

class Sample:
  def __init__(self):
    pass
  def disp(self):
    print("jo")
ob1=Sample()
ob2=Sample()
print(id(ob1.disp()))
print(id(ob2.disp()))

class Student:
  def __init__(self,name,age):
    self.name=name
    self.age=age
  def display(self):
    print(self.name,self.age)
s1=Student(name="vk",age=18)
s2=Student(name="abd",age=17)
s1.display()
s2.display()

class BankAccount:
  def __init__(self,accountNumber,name,balance):
    self.accountNumber=accountNumber
    self.name=name
    self.balance=balance
  def Deposit(self,amount):
    self.balance+=amount
  def Withdrawal(self,amount):
    if self.balance>=amount:
      self.balance-=amount
    else:
      print("not enough balance")
  def bankFees(self):
    print("bank fees=",self.balance*0.05)
    self.balance-=self.balance*0.05
  def display(self):
    print("accountNumber:",self.accountNumber,"\nname:",self.name,"\nbalance=",self.balance)
user=BankAccount(accountNumber=18,name="vk",balance=18000)
user.Deposit(100)
user.Withdrawal(1)
user.bankFees()
user.display()

