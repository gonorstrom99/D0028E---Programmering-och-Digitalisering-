
import math
def logStar(x):
    if math.log(x,2)<1:
        return 1
    elif math.log(x,2)==1:
        return 1
    else:
        return logStar(math.log(x,2))+1
    

print(logStar(1024))