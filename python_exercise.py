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

common1 = input("Enter the numbers for your first list: ")
common2 = input("Enter the numbers for your second list: ")
common = []
for i in common1:
	if i in common2 and i in common1:
		common.append([i])

print(common)

letter = input("Enter a letter: ")
vowels = ["a", "e", "i", "o", "u"]
for i in letter:
    if i in vowels and i in letter:
        print("Your letter is a vowel")
    else:
        print("Your letter is not a vowel")

numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]
n2 = []

for i in numbers:
    if i in numbers:
        n2.append([i])
        if i == 237:
            print(n2)
            break
            
