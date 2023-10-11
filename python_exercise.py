# twinkle = """Twinkle, twinkle, little star,
# 	How I wonder what you are! 
# 		Up above the world so high,   		
# 		Like a diamond in the sky. 
# Twinkle, twinkle, little star, 
# 	How I wonder what you are
# """

# print(twinkle)

# user_input = input("Enter a series of numbers seperated by commas: ")
# a = user_input.split(',')
# List = [int(item) for item in a]
# Tuple = tuple(int(item) for item in a)
# print("List: " + str(List))
# print("Tuple: " + str(Tuple))

# common1 = input("Enter the numbers for your first list: ")
# common2 = input("Enter the numbers for your second list: ")
# common = []
# for i in common1:
# 	if i in common2 and i in common1:
# 		common.append([i])

# print(common)

letter = input("Enter a letter: ")
vowels = ["a", "e", "i", "o", "u"]
for i in letter:
    if i in vowels and i in letter:
        print("Your letter is a vowel")


