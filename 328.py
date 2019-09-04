#print out all of the items and their prices.
#Double the price of everything
#Print out again


pricedproduce = {"apple":.75,"banana":.25,}
pricedproduce["cucumber"] = .75

for x in pricedproduce:
    print((x), pricedproduce[x])
    pricedproduce[x] = pricedproduce[x] * 2
    print(x, pricedproduce[x])



