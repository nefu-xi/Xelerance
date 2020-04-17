def Fibo_max(max_num):
    if max_num > 0:
        #initialization of ist, 2nd sum and sum
        x,y,sum=0,1,0
        print(x)
        while y<max_num:
            print(y)
            if y%2: 
                sum += y
            x,y = y,x+y
        print("sum of odd-values:",sum)
    else:
        print("please use a positive Integer!")
Fibo_max(22)