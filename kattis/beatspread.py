[((lambda x:print(*sorted(map(int,(x[0],x[1])),reverse=True))if x[0]>=0 and x[1]>=0 and not x[0]%1 else print("impossible")))((lambda x:((x[0]-x[1])/2,(x[0]-x[1])/2+x[1]))(list(map(int,input().split()))))for _ in range(int(input()))]