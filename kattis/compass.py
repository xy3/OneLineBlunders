print((lambda xy:xy[0]if xy[0]<=xy[1]else-xy[1])((lambda x,y:((y-x)%360,(x-y)%360))(int(input()),int(input()))))