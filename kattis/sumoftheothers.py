[print(sorted({x if x == sum(xx) - x else None for x in xx}, key=(lambda x: 1 if x == None else 0))[0]) for xx in [list(map(int, x.split())) for x in (__import__("sys")).stdin.readlines()]]