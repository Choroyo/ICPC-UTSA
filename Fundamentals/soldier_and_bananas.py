#Bryan Chora 9/24/2024 Codeforces: soldier and bananas

'''
This function will calculate the bananas total cost
param: (int) the cost of the first banana, (int) the amount of desire bananas
return: (int) cost: The total cost to buy all the bananas
'''
def calculate_cost(initial_cost,amount_bananas):
    cost = 0 #initialize cost

    #loop to add the cost of every banana
    for num in range(1,amount_bananas+1):
        cost += num * initial_cost
    
    #this will return the total cost 
    return cost

'''
This function will calculate the total amount of borrow money to be able to buy the bananas
param:(int) the total cost to buy all the bananas, (int) the amount of money that the soldier have
return: (int) borrow: the total borrowed dollar needed it to buy all the bananas
'''
def calculate_borrow(total_cost, money):
    borrow = abs(money - total_cost)
    return borrow

#This function will run the main program
def main():
    #Enter the price of the first banana,dollars available, desire bananas
    price, dollars, bananas = map(int,input().split())

    cost = calculate_cost(price,bananas)

    if dollars > cost:
        print(0)
    else:
        print(calculate_borrow(cost,dollars))

#Execute the main program
main()