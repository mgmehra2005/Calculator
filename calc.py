import math
from typing import Text

para = "\nThis Calculater is build by Matang Mehra. This Calculator is for general purpose use. This Calculator is under construction. \n\nVersion = v.1.1.1"

d1 = {"1250" : "Pankaj", "2500" : "Aaryan"}

d1 ["5045"] = "Matang"
d1.update({"4585" : "Rishabh"})

p = "Enter Your ID : "
r = d1[input(p)]

print(f"\nWelcome {r}")

ls = "\n\n1. Calculator \n2. Info"
print(ls)

t1 = "\nSelect one of them : "
take = int(input(t1))

if take == 1 :
    print("\nCALCULATOR")
    print("\n\tBuild By Matang Mehra")

    print("\n1. Addition \n2. Division \n3. Multiplication \n4. Substriction \n5. Percentage \n6. Discount Checker \n7. Square Root")

    first = "\nChoose one of them : "
    choosen_number = input(first)

#Addition
    if choosen_number == "1":
        print("\nYou have choosed Addition.")
        fa = "\nValue 1 : "
        sa = "\nValue 2 : "
        value1a = input(fa) 
        value2a = input(sa)
        total_a = int(value1a)+int(value2a)
        print(f"\nTotal : {total_a}")

    #Division
    elif choosen_number == "2":
        print("\nYou have choosed Division.")
        fd = "\nNumerator : "
        value1d = input(fd)
        sd = "\nDenominator : "
        Value2d = input(sd)
        total_d = int(value1d)/int(Value2d)
        print(f"\nTotal : {total_d}")

#Multiplication
    elif choosen_number == "3":
        print("\nYou have choosed Multiplication.")
        fm = "\nValue 1 : "
        value1m = input(fm)
        sm = "\nValue 2 : "
        Value2m = input(sm)
        total_m = int(value1m)*int(Value2m)
        print(f"\nTotal : {total_m}")

#Substriction
    elif choosen_number == "4":
        print("\nYou have choosed Substriction.")
        fs = "\nValue 1 : "
        value1s = input(fs)
        ss = "\nValue 2 : "
        Value2s = input(ss)
        total_s = int(value1s)-int(Value2s)
        print(f"\nTotal : {total_s}")

#Percentage Calculator
    elif choosen_number == "5":
        print("\nYou have choosed Percentage.")
        fp = "\nValue :"
        value1p = input(fp)
        sp = "\nTotal :"
        Value2p = input(sp)
        total_p = int(value1p)/int(Value2p)*100
        print(f"\nYour Answer : {total_p} %")

#Discount Checker
    elif choosen_number == "6":
        print("\nYou have choosed Discount Checker.")
        fd = "\nValue : "
        value1dc = input(fd)
        sd = "\nTotal : "
        Value2dc = input(sd)
        total_dc = 100-int(value1dc)/int(Value2dc)*100
        print(f"\nDiscount : {total_dc} %")
    
#Squre Root
    elif choosen_number == "7":
        print("\nYou have choosen Square Root.")
        fr = "\nValue : "
        text = int(input(fr))
        value1sq = math.sqrt(text)
        print(f"\nSquare Root : {value1sq}")
    
    else:
        print("You have entered worng value.")

elif take == 2:
    print(para)

else :
    print("You have selected wrong number.")
