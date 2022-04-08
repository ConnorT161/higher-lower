import random

number = random.randint(1,50)

response = input("Enter a number 1-50: ")

def guess(a):
  if a > number:
    print ("Too high.")
    response = input("Try again: ")
    response = int(response)
    guess(response)
  elif a < number:
    print ("Too low.")
    response = input("Try again: ")
    response = int(response)
    guess(response)
  else:
    print ("Correct!")

response = int(response)

guess(response)



