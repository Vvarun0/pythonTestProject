# working of while loop using contimnue and break
o = 4
while o < 9:
    if o == 7:
        o = o + 1
        continue
    if o == 8:
        break
    print(o)
    o = o + 1
print("while loop execution is done")
print("******************************")