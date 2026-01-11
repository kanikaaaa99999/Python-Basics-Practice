
#default arguments = a default value for certain patameters 
#                    default values are used if no argument is passed
#                    make your functions felexible , reduces # of arguemts
#                 1. positional arguments
#                 2. keyword arguments
#                 3. default arguments
#                 4. arbitrary arguments

import time
def count(end, start=0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)

    print("done!")

count(5)