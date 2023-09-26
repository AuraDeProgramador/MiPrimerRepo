point = (2, 5)
match point:
    case (x, y):    
        print(f"({x},{y}) is in plane" )
    case (x, y, z):
        print(f"({x},{y},{z}) is in space" )
