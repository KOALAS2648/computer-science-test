from deneraytobinary import denearytobinary as db
enterd =  False
while not enterd:
    ask = int(input("enter a number 0-255: "))
    if number >= 0 and number <= 255:
        enterd=True
        print(db(number))
        break
    print("enter a correct number please: ") 