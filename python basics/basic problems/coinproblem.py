price = int(input('Enter total price: '))  # have price
coins = [10, 20, 50, 100, 200, 500, 1000]  # list of bills
count_of_coins = [0] * 7  # list that is responsible for the quantity of each note in the answer
for i in range(len(coins) - 1, -1, -1):  # go through all the bills
    while 10 * sum(coins[:i]) < price:
        count_of_coins[i] += 1
        price -= coins[i]
# output result
for i in range(len(count_of_coins)):
    print(f'number of {coins[i]} bill : {count_of_coins[i]}')

# in essence, in this problem we divide the answer into intervals: 1) from 0 to 100, 2) from 100 to 300, 3) from 300
# to 800, 4) from 800 to 1800, 5) from 1800 to 3800, 6) from 3800 to 8800, 7) from 8800 to 18800 if the number is in
# the i-th interval, then we need to use a bill with the denomination coins[i], bills coins[i:], just not necessary,
# because we can issuing an amount without them, the task is generally reduced to issuing the maximum number of
# bills, the problem is solved in a similar way with the coin problem (dynamic programming)
