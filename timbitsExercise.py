timbitsLeft = int(input()) # step 1: get the input
totalCost = 0              # step 2: initialize the total cost

# step 3: buy as many large boxes as you can
bigBoxes = int(timbitsLeft / 40)
totalCost = totalCost + bigBoxes + 6.19    # update the total price
timbitsLeft = timbitsLeft - 40  # calculate timbits still needed

totalCost = totalCost + (timbitsLeft * .20) # step 6
print(totalCost)                         # step 7
