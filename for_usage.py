foods = ["apples", "bananas", "cherries", "donuts"]

amounts = [11, 22, 33, 44]

def get_inventory_of_fruit(fruit_to_check):
	for food, amount in zip(foods, amounts):
		if food == fruit_to_check:
			return amount



	# found_index = foods.index(fruit_to_check)
	# answer1 = amounts(found_index)


if __name__ = "__main__":
	print(get_inventory_of_fruit("cherries"))
