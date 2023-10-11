twinkle = """Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are
"""

print(twinkle)

user_input = input("Enter a series of numbers seperated by commas: ")
a = user_input.split(',')
List = [int(item) for item in a]
Tuple = tuple(int(item) for item in a)
print("List: " + str(List))
print("Tuple: " + str(Tuple))

