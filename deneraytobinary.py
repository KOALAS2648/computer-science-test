def denearytobinary(number):
    binNumber = ""
    for i in range(7,-1,-1):
        if number-(2**i) >= 0:
            binNumber += "1"
            number -=2**i
        else:
            binNumber +="0"
    return binNumber
def main():
    correct = False
    while not correct:
        ask = int(input("enter a number 1-255: "))
        if ask >= 1 and ask <= 255:
            print(denearytobinary(ask))
            correct = not correct
        else:
            print("enter a number between 1-255 please")
            continue
if __name__ =="__main__":
    main()