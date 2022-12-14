#Object Oriented Programming!
#Write a script that contains multiple classes:
#- a "Fruit" class
#- an "Apple" class that inherits from "Fruit"
#- a "Grape" class that inherits from "Fruit"

#Instances of the Fruit class should have an attribute that contains information regarding whether it's ripe. There should also be a method that changes this so that a fruit can ripen.

#Instances of the Apple class have to be initialized with a color (e.g. "red" or "green").

#Instances of the Grape class have to be initialized with information regarding their variant (e.g. "seedless" or "seedy").
#Also they should be special regarding their ripening: When ripe() is called on a instance of a grape the grape should turn into a raisin (is_raisin = False -> True)

#At the end, create an red-apple-object, a green-apple-object and a seedless-raisin-object and print their properties.


#Advice:
#Make sure you understand the importance of "__init__".
#Also be careful to implement the things above so that instances of a class don't share their attributes (one fruit is ripe while another one isn't) by using "self" when assigning values

#Challenge:
#Make sure that despite having to rewrite the __init__ function for Apples you still have a "is_ripe" attribute in Apple-instances
