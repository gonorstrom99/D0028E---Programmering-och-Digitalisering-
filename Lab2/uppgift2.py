def tvarsumman(x):
    if x<10:
        return x
    else:
        return x//10+tvarsumman(x%10)
    
print(tvarsumman(12))