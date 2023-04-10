#A basic calculator for travel expenses
#4/10/23
#CTI-110 P1HW1 - Travel Expense
#Darryl McAllister
#Input approximate expenses then allow program to calculate


print('This program calculates and displays travel expenses')
trvl_bdgt = int(input('Enter Budget: '))
trvl_loc = input('Enter your travel destination: ')
trvl_gas = int(input('How much do you think you will spend on gas? '))
trvl_htl = int(input('Approximately, how much will you need for accomodation/hotel? '))
trvl_food = int(input('Last, how much do you need for food? '))

print('------------Travel Expenses------------')
print('Location: ', trvl_loc)
print('Initial Budget: ', trvl_bdgt)

print('Fuel:', trvl_gas)
print('Accomodation:', trvl_htl)
print('Food:', trvl_food)

print('Remaining Balance:', trvl_bdgt - trvl_gas - trvl_htl - trvl_food)
