while n := int(input()):
    match n:
        case 1:
            print('один')
        case 2:
            print('два')
        case 3:
            print('три')
        case var if var % 2 == 0:
            if n % 2 == 0:
                print('четное')
        case _:
            print('нечет')
