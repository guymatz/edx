#!/usr/bin/env python

def calc_monthly_payment(bal, mpr):
  return bal * mpr

def calc_remaining_balance(bal, payment, apr):
  return ( (bal - payment) * ( 1 + apr/12) )

def main(bal, apr, mpr):

  remaining_balance = bal
  total_paid = 0

  for month in range(1,13):
    monthly_payment = calc_monthly_payment(remaining_balance, mpr)
    total_paid += monthly_payment

    remaining_balance = calc_remaining_balance(remaining_balance, monthly_payment, apr)
    print("Month: %i" % month)
    print("Minimum montly payment: %0.2f" % monthly_payment)
    print("Remaining balance: %0.2f" % remaining_balance)

  print("Total paid: %0.2f" % total_paid)
  print("Remaining balance: %0.2f" % remaining_balance)
    
balance=4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
main(balance, annualInterestRate, monthlyPaymentRate)
