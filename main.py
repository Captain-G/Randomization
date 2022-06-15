# Exercise 5
# Generate a random string of length 5
# The word must be a combination of both uppercase and lowercase letters

import random

uppercase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lowercase = []
for i in range(len(uppercase)):
    low = uppercase[i].lower()
    lowercase.append(low)

upper_lower = uppercase + lowercase

word = random.sample(upper_lower, 5)
print(f"{word[0]}{word[1]}{word[2]}{word[3]}{word[4]}")




# Exercise 1
# generate 3 random integers between 100 and 999 which is divisible by 5


# import random
#
# div_by_5 = []
# for i in range(100, 999):
#     if i % 5 == 0:
#         div_by_5.append(i)
#
# for j in range(3):
#     number = random.choice(div_by_5)
#     print(f"{j + 1} is {number}")



# Exercise 2
# Random lottery pick
# Generate 100 random lottery tickets and pick two lucky tickets from it as the lucky winners
# The lottery number must be 10 digits long and all 100 tickets numbers must be unique


# import random
# tickets = []
# chosen = []
# random_number = 0
# for a in range(100):
#     random_number = random.randint(1000000000, 9999999999)
#     if random_number in tickets:
#         continue
#     tickets.append(random_number)
#
# chosen = random.sample(tickets, 2)
# print(f"The first winner is ticket number {chosen[0]}")
# print(f"The second winner is ticket number {chosen[1]}")



# Exercise 3
# Generate a 6 digit random secure OTP

# import secrets
#
# # getting SystemRandom class instance of the secrets module
# secretsGenerator = secrets.SystemRandom()
#
# # secure random integer numbers
# random_number = secretsGenerator.randint(100000, 999999)
#
# print(random_number)




# Exercise 4
# Pick a random character from a given string
# import random
#
# myWord = input("Please input any word here : ")
# letters_in_word = []
# for i in myWord:
#     letters_in_word.append(i)
# length_of_word = len(myWord)
# print(random.choice(letters_in_word))






# Exercise 6
# Generate a random password which meets the following conditions
# password length must be 10 characters long
# it must contain atleast 2 uppercase letters, 1 digit and 1 special symbol

# import random
#
# password = []
# uppercase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
# lowercase = []
# upper2 = []
# for i in range(len(uppercase)):
#     low = uppercase[i].lower()
#     lowercase.append(low)
# digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# characters = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "=", "[", "{", "]", "}", ";", ":", "'", "|", "<", ">"]
# upper2 = random.sample(uppercase, 2)
# digit1 = random.choice(digits)
# char1 = random.choice(characters)
# string_index = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# random_index = random.choice(string_index)
#
# #
# # INCOMPLETE
#
