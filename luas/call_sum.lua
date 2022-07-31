function sum2(bil1, bil2)
    return(bil1 + bil2)
end 

b = {10, 5, 6, -7, -8}

r = sum2(b[1], b[2])
print(r)

r = sum2(r, b[3])
print(r)


r = sum2(r, b[4])
print(r)


r = sum2(r, b[5])
print(r)
