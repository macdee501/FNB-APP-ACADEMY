print("Welcome to the shopping cart program!")

foods=[]
prices=[]
total=0

while True:
    food=input("Enter the food you want to buy or q to quit: ")
    if food.lower()=="q":
        break
    else:
        price=float(input(f"Enter the price of the {food}: R"))
        foods.append(food)
        prices.append(price)

print("---------------YOUR CART-----------------")

for food in foods:
    print(food,end=" ")

for price in prices:
    total+=price

print("\n")
print(f"Total price: R{total}")







