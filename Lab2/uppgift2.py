def tvarsumman(x):
    ans=0
    while x>0:
        
        ans=ans+x%10
        x=x//10
    
    return ans

    # if x<10:
    #     return x
    # else:
    #     return x//10+tvarsumman(x%10)
    
print(tvarsumman(253))
import d0028e_lab2_sumTest
