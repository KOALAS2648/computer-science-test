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
    for i in range(0, 256):
        print(f"{i} in binary is {denearytobinary(i)}")

if __name__ =="__main__":
    main()