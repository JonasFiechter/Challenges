'''
Calculated Bonus

A financial institution provides professional services to banks and claims 
charges from the customers based on the number of man-days provided. 
Internally, it has set a scheme to motivate and reward staff to meet and 
exceed targeted billable utilization and revenues by paying a bonus for 
each day claimed from customers in excess of a threshold target.

This quarterly scheme is calculated with a threshold target of 32 days per 
quarter, and the incentive payment for each billable day in excess of such 
threshold target is shown as follows:
Days	Bonus
0 to 32 days	Zero
33 to 40 days	SGD$325 per billable day
41 to 48 days	SGD$550 per billable day
Greater than 48 days	SGD$600 per billable day

Please note that incentive payment is calculated progressively. As an example, 
if an employee reached total billable days of 45 in a quarter, his/her 
incentive payment is computed as follows:

32*0 + 8*325 + 5*550 = 5350

Write a function to read the billable days of an employee and return the 
bonus he/she has obtained in that quarter.
Examples

bonus(15) ➞ 0

bonus(37) ➞ 1625

bonus(50) ➞ 8200
'''

def bonus(days):
    bonus = 0
    for i in range(days + 1):
        if i >= 33 and i <= 40:
            bonus += 325
        elif i >= 41 and i <= 48:
            bonus += 550
        elif i > 48:
            bonus += 600
    return bonus


if __name__ == '__main__':
    print(bonus(50))

