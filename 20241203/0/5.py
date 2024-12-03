while s := input():
    tokens = s.split()
    match tokens:
        case ["mov", x, y]:
            print(f"moving {y} to {x}")
        case ["push", x, y]:
            print(f"pushing {x} {y}")
        case ["cmd", x, y]:
            print("ccccccmd")
        case _:
            print("#")
            
