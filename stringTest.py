theString = input()
#print(theString[len(theString) - 1]  + theString[1 : len(theString) -1] + theString[0])
#print(theString * 3)
if ord(theString) == 90:
    print('A')
else:
    print(chr(ord(theString)+1))
