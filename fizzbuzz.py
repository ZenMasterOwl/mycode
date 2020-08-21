#!/usr/bin/python3

for number in range(1,100):
    if number%3 != 0 and number%5 !=0:
        print(number)
    if number%3 == 0:
       
       if number%5 == 0:
         print("FizzBuzz")
    else:
        print("Fizz")
    if number%15==0:
        print("FizzBuzz")
