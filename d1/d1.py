f = open("input", "r")

dial = 50
zero_count = 0 
for i in f:
    num = int(i[1:])

    if i[0] == "L":
        dial = (dial - num)%100
    if i[0] == "R":
        dial = (dial + num)%100
    # if i[0] == 'L':
    #     num*=-1

    # dial += num
    # if dial < 0:
    #     dial = 100+dial
    # if dial > 99:
    #     dial = dial%100
    if dial == 0:
        zero_count+=1
    print(num,dial)
print (zero_count)