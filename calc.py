print("\nCALCULATOR")
print("\n\tMADE BY : Matang Mehra")

print("\n1. Addition \n2. Division \n3. Multiplication \n4. Substriction \n5. Percentage \n6. Discount Checker")

print("\n\nChoose one of them : ")
choosen_number = input()

#Addition
if choosen_number == "1":    
    print("\nYou have choosed Addition.")
    print("\nValue 1 :")
    value1a = input()
    print("\nValue 2 :")
    value2a = input()
    total_a = int(value1a)+int(value2a)
    print(f"\nTotal : {total_a}")

#Division
elif choosen_number == "2":
    print("\nYou have choosed Division.")
    print("\nNumerator :")
    value1d = input()
    print("\nDenominator :")
    Value2d = input()
    total_d = int(value1d)/int(Value2d)
    print(f"\nTotal : {total_d}")

#Multiplication
elif choosen_number == "3":
    print("\nYou have choosed Multiplication.")
    print("\nValue 1 :")
    value1m = input()
    print("\nValue 2 :")
    Value2m = input()
    total_m = int(value1m)*int(Value2m)
    print(f"\nTotal : {total_m}")

#Substriction
elif choosen_number == "4":
    print("\nYou have choosed Substriction.")
    print("\nValue 1 :")
    value1s = input()
    print("\nValue 2 :")
    Value2s = input()
    total_s = int(value1s)-int(Value2s)
    print(f"\nTotal : {total_s}")

#Percentage Calculator
elif choosen_number == "5":
    print("\nYou have choosed Percentage.")
    print("\nValue :")
    value1p = input()
    print("\nTotal :")
    Value2p = input()
    total_p = int(value1p)/int(Value2p)*100
    print(f"\nYour Answer : {total_p} %")

#Discount Checker
elif choosen_number == "6":
    print("\nYou have choosed Discount Checker.")
    print("\nValue :")
    value1dc = input()
    print("\nTotal :")
    Value2dc = input()
    total_dc = 100-int(value1dc)/int(Value2dc)*100
    print(f"\nDiscount : {total_dc} %")
    
else:
    print("You have entered worng value.")
