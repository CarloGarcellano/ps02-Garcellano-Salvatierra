# += method
import time

start = time.time()
result = ""
for y in range(1,100001):
    result += str(y)
print(result)
print("+= Timer:", time.time() - start)


#join method
import time

start2 = time.time()
result2 = ",".join(str(y) for y in range(1, 10001)) #",".join(str(list(range(5)))) #galing kay maam
print(result2)
print("using join method:", time.time() - start2)



