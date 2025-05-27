"""
You work for a retail store that wants to increase sales on Tuesday
and Wednesday, which are the store's slowest sales days. On Tuesday
and Wednesday, if a customer's subtotal is greater than $50, the
store will discount the customer's purchase by 10%.
"""

import datetime
today = datetime.datetime.now()
day = (today.strftime('%A'))

subtotal = float(input('Please enter the subtotal: '))
if subtotal >= 50 and (day == 'Tuesday' or day == 'Wednesday'):   
    discount = subtotal * .10 
    subtotal -= discount
    sales_tax = subtotal * .06
    subtotal += sales_tax
    print(f'Sales tax amount: {sales_tax:.2f}')
    print(f'Total {subtotal:.2f}')
else:
    sales_tax = subtotal * .06
    subtotal += sales_tax
    print(f'Sales tax amount: {sales_tax:.2f}')
    print(f'Total {subtotal:.2f}')


    
