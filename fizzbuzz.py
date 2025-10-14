def fizzbuzz(number):
    if number % 15 == 0:
        return "fizzBuzz"
    elif number % 3==0:
        return "fizz"
    elif number %5==0:
        return "buzz"
    
    else:
        return number
x = 0
while x != 100:
    ask =  input(f"enter if {x} is fizz, buzz or fizzbuzz: "))
    if ask != fizzbuzz(x):
        print("inncorrect")
        print(f"you neededto answer {fizzbuzz(x)}")
    x  += 1