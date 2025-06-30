print("Dane's Stuff Store")


num_item = int(input("How many items would you like to purchase : "))

if num_item <=0:
    print(" Must be greater than zero")
    exit()

total_price = 0

for i in range(num_item):
        price = float(input(f"Enter price of item {i+1}: "))
        total_price += price

average_price = total_price / num_item
print("Total cost of your items is" , f"${total_price:.2f}")
print(f"The avergage cost is", f"${average_price:.2f}" )

#Chris Smih
#Chapter 3 Lab 2
#6/30/2025


