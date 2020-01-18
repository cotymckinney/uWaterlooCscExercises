#Hovercraft Code Coach challenge from SoloLearn
customers = int(input('Input monthly sales please: '))
iCost = 1000000
bCost = 2000000
hPrice = 3000000
hBuiltPM = 10

opCostPM = int((bCost * hBuiltPM) + iCost)
hSales = int(customers * hPrice)

print('You have completed ' + str(customers) + ' sales this month.')

if hSales > opCostPM:
    print('Profit')
elif hSales == opCostPM:
    print('Broke Even')
else:
    print('Loss') 
