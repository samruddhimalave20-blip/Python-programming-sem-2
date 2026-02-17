# code for EMI calculation 
"""
Created on Tue Feb 17 11:05:09 2026

@author: samruddhi malave 
"""
principal=float(input("Entere principal amount:"))
monthlyinterest=float(input("Enter monthly interest rate(in %):"))
year=float(input("enter loan tenure(in years):"))

months = year * 12 
monthlyinterest = monthlyinterest / 100

EMI=(principal * monthlyinterest * (1 + monthlyinterest) ** months / ((1 + monthlyinterest) 
    ** months - 1))
print("your EMI is:", round(EMI, 2))
