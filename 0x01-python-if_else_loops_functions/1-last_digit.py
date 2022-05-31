#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = (-1 * number if number < 0 else number) % 10
if last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is {last_digit}")
elif last_digit > 5:
    if number > 0:
        print(f"Last digit of {number} is {last_digit} and is greater that 5")
    else:
         print(f"Last digit of {number} is {last_digit * -1} and is greater that 5")
elif last_digit < 6 and last_digit != 0:
    if number > 0:
        print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")
    else:
         print(f"Last digit of {number} is {-1 * last_digit} and is less than 6 and not 0")
