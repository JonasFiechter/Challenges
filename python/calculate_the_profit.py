'''
Calculate the Profit
You work for a manufacturer, and have been asked to calculate the total profit 
made on the sales of a product. You are given a dictionary containing the cost 
price per unit (in dollars), sell price per unit (in dollars), and the starting 
inventory. Return the total profit made, rounded to the nearest dollar.

Examples
profit({
  "cost_price": 32.67,
  "sell_price": 45.00,
  "inventory": 1200
}) ➞ 14796

profit({
  "cost_price": 225.89,
  "sell_price": 550.00,
  "inventory": 100
}) ➞ 32411

profit({
  "cost_price": 2.77,
  "sell_price": 7.95,
  "inventory": 8500
}) ➞ 44030
'''

# Solution 1

d_1 = {
  "cost_price": 32.67,
  "sell_price": 45.00,
  "inventory": 1200
}

d_2 = {
  "cost_price": 225.89,
  "sell_price": 550.00,
  "inventory": 100
}

d_3 = {
  "cost_price": 2.77,
  "sell_price": 7.95,
  "inventory": 8500
}

def profit(dict):
    return round((dict['sell_price'] - dict['cost_price']) * dict['inventory'])

print(profit(d_1))
print(profit(d_2))
print(profit(d_3))


# Solution 2

list_dicts = [{
  "cost_price": 32.67,
  "sell_price": 45.00,
  "inventory": 1200
}, {
  "cost_price": 225.89,
  "sell_price": 550.00,
  "inventory": 100
}, {
  "cost_price": 2.77,
  "sell_price": 7.95,
  "inventory": 8500
}]

def profit(sell_price, cost_price, inventory):
    return f"$ {((sell_price - cost_price) * inventory):.2f}"

for i in list_dicts:
    print(profit(
        sell_price=i['sell_price'], 
        cost_price=i['cost_price'],
        inventory=i['inventory']))

