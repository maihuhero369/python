n = 10
count = 0 
for j in range(2 , n):
        for i in range( 2, j//2 +1 ) :     
            if j % i == 0 :
             count += 1
             break 
            else :
             continue 
        if count == 0 :    
         print("Prime Number", j)
        else :
         count = 0
         print("Not a Prime Number")