# 1. TASK: print "Hello World"
print("Hello World")
# 2. print "Hello Noelle!" with the name in a variable
name = "Noelle"
print("Hello ", name)	# with a comma
print("Hello " + name)	# with a +
# 3. print "Hello 42!" with the number in a variable
name = 42
print("Hello ", name)	# with a comma
print("Hello" + name)	# with a +	-- this one should give us an error!
fave_food1 = "sushi"
fave_food2 = "pizza"
print("I love to eat {} {}". format(fave_food1, fave_food2))
print(f"I love to eat {fave_food1} and {fave_food2}")