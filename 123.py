import time
time0 = time.time()
for i in range(200):
    print(i*10)

print((time.time() - time0)*100)