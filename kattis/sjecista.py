print((lambda mx:(lambda t:t[0]if[[t.__setitem__(0,t[0]+j*i)for j in range(mx-i+1,0,-1)]for i in range(1, mx+1)]else 0)([0]))(int(input())-3))