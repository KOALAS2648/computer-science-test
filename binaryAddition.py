# assuming both binary digits are the same length
"""
0 + 0 + 0 = 0 carry 0
0 + 1 + 0 = 1 carry 0
1 + 0 + 0 = 1 carry 0
1 + 1 + 0 = 0 carry 1
1 + 1 + 1 = 1 carry 1
"""
import binarytodenary as BD

def add_binary(num1, num2):
    if len(num1) != len(num2):
        return -1
    res = []
    carry = "0"
    c = ""
    #print(num1)
    #print(num2)
    
    for i in range(len(num1)-1, -1, -1):
        val1 = num1[i]
        val2 = num2[i]
        if val1 == "0" and val2 == "0":
            if carry == "0":
                res.insert(0, "0")
            elif carry == "1":
                res.insert(0,"1")
                carry = "0"
        elif val1 == "0" and val2 == "1":
            if carry == "0":
                res.insert(0,"1")
            elif carry == "1":
                res.insert(0,"1")
                carry = "0"
        elif val1 == "1" and val2 == "0":
            if carry == "0":
                res.insert(0,"1")
            elif carry == "1":
                res.insert(0,"0")
                carry = "1"
        elif val1 == "1" and val2 == "1":
            if carry == "0":
                res.insert(0,"0")
                carry="1"
            elif carry == "1":
                res.insert(0, "1")
                carry = "1"
    for i in res:
        c +=i
    return c

            

a = add_binary("00110010","00011001")
print(a)
print(BD.BinaryTODenary(a))
#00110010 denary:50
#00011001 denary:25
