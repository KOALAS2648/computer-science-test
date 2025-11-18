from deneraytobinary import *
def BinaryTODenary(number:str) -> int:
    sum = 0
    start_power = len(number)
    for idx, digit in enumerate(number):
        sum += int(digit)*(2**(start_power-idx))
    return sum//2

def main():
    for i in range(0,256):
        number = denearytobinary(i)
        print(f"i: binary:{number} denary:{BinaryTODenary(number)}")

if __name__ == "__main__":
    main()