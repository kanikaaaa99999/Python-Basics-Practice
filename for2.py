import time

my_time = int(input("Enter time in seconds: "))

for x in range(my_time , 0 , -1):
    seconds = x % 60
    print(x)
    time.sleep(1)

print("time's up!")