snack_name= "sandwitch"
price= 10.7
quantity= 5
is_available= True

print("Snack Name:", snack_name)
print("Price:", price)
print("In Stock:", quantity)
print("Available?", is_available)

print(type(snack_name))
print(type(price))
print(type(quantity))
print(type(is_available))

total = price * quantity
print("Total value:", total)
print("Sales Price:", price - 0.9)
print("Double Stock:", quantity * 4)

print("Is my price less than 20?:", price < 20)
print("Is my quantity greater than 10?:", quantity > 10)
print("Is my price exactly 10.9?:", price == 10.9)

shop_name="Snack"+"fun"
print("Shop Name:", shop_name)
print("letters of the snack name:", len(snack_name))
print("5th letter:", snack_name[4])

price_a= 4.09
price_b= 6.04
print("before:", price_a, "and", price_b)

temp= price_a
price_a= price_b
price_b= temp
print("after:", price_a, "and", price_b)