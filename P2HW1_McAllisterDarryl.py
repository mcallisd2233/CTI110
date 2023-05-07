#A basic calculator for travel expenses
#4/10/23
#CTI-110 P2HW1 - Travel Expense
#Darryl McAllister
#Input approximate expenses then allow program to calculate


print('This program calculates and displays travel expenses')
trvl_bdgt = float(input('Enter Budget: '))
trvl_loc = input('Enter your travel destination: ')
trvl_gas = float(input('How much do you think you will spend on gas? '))
trvl_htl = float(input('Approximately, how much will you need for accomodation/hotel? '))
trvl_food = float(input('Last, how much do you need for food? '))

trvl_exp = {Location: (trvl_loc), Budget: (trvl_bdgt), Fuel: {trvl_gas}, Accomodation: {trvl_htl}, Food: {trvl_food}}

print('------------Travel Expenses------------')
for cost in trvl_exp:
    print(f'{trvl_exp} : ${cost}'.format(6), end = " ")
print('---------------------------------------')
print('Remaining Balance:', trvl_bdgt - trvl_gas - trvl_htl - trvl_food)
