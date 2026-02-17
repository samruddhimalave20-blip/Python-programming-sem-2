# program to compute simple intrest using function with parameter
"""
Created on Tue Feb 17 10:21:49 2026

@author: samruddhi malave
"""

def simple_interest(principal,rate,time):
    
    si = (principal * rate * time)/100
    return si
    
# Taking input from the user 

p = float(input("Enter principal amount:"))

r = float(input("Enter rate of interest:"))

t = float(input("Enter time (in years):"))

# Function call 

interest = simple_interest(p,r,t)  

print("Simple Interest is:",interest)        
      
