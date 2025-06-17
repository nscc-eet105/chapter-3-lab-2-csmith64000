print("Dane's Stuff Store")

try:
    num_item = int(input("How many items would you like to purchase : "))
except ValueError:
    print("Invalid input. try again")
    exit()

if num_item <=0:
    print(" Must be greater than zero")
    exit()

total_price = 0
for i in range(num_item):
    try:
        price = float(input(f" Enter price of the item {i+1} : "))
        total_price += price
    except ValueError:
        print("Invalid input try again")

average_price = total_price / num_item
print("Total cost of your items is" , f"${total_price:.2f}")
print(f"The avergage cost is : {average_price:.2f}")

print("Chris Smith")
print ("Chapter 3 Lab 2")
print("6/17/2025")


