# There's a small fruit shop nearby your house that you like to buy from. Since you buy several fruit at a time, you want to keep track of how much the fruit will cost before you go. Luckily you wrote down what fruits were available and how much one of each fruit costs.

# Write a program that loops through a dictionary of fruits, prompting the user to see how many of each fruit they want to buy, and then prints out the total combined cost of all of the fruits.


fruits = {
    "apple": 10.0,
    "durian": 50.0,
    "jackfruit": 20.0,
    "kiwi": 5.0,
    "rambutan": 15.0,
    "mango": 8.0
}

def main():
    total = 0

    for fruit in fruits:
        quantity = float(int(input(f"How many {fruit} do you want?: ")))
        price = fruits[fruit] * quantity
        total += price
    
    print(f"Your total is ${total}")

main()

