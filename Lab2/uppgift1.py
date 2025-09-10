
import math
def logStar(x):
    ans=0
    while x>1:
        x=math.log(x,2)
        ans=ans+1
    return ans

    # if math.log(x,2)<1:
    #     return 1
    # elif math.log(x,2)==1:
    #     return 1
    # else:
    #     return logStar(math.log(x,2))+1
    

print(logStar(60))
import d0028e_lab2_logStarTest
