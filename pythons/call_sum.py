def sum2 (bil1, bil2) :
    return (bil1 +bil2)
    
    
if __name__ == "__main__":
    b = [10, 5 , 6 , -7, -8]
    
    r = sum2(b[0], b[1])
    
    print(r)
    
    r = sum2(r, b[2])
    
    print(r)
    
    r = sum2(r,b[3])
    
    print(r)
    
    r = sum2(r,b[4])
    
    print(r)
    
