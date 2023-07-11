#Before walrus operator
food = list()

while True:
    foods = input("What is your favourite veggie : ")
    if foods == "karela":
        break
    food.append(foods)

#After walrus operator
foodie = list()
while (foodies := input("What is your favourite veggie : ")) != "karela":
    foodie.append(foodies)