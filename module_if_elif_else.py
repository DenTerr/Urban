first = int(input()) #123 #1

second = int(input()) #456 #1

third = int(input()) #789 #3



if first == second == third :
    print(3)

elif first == second != third or first != second == third or first == third != second or first != third == second:
    print(2)