print(int((lambda x:((lambda y,n:y[0]if len(y)>0 else n-1)(list(filter(lambda x:x!='',[x-x/i if x%i==0 else""for i in range(2,int(x**0.5)+1)])),x)))(int(input()))))