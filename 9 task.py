king_v = int(input())
king_g = int(input())

next_v = int(input())
next_g = int(input())


def check_input(king_v, king_g, next_v, next_g):
    if king_v in range(1, 9) and king_g in range(1, 9) and next_v in range(1, 9) and next_g in range(1, 9):
        return True
    else:
        return False

def move_king(king_v, king_g, next_v, next_g):
    if(check_input(king_v, king_g, next_v, next_g)):
        if(abs(next_v - king_v) <= 1 and abs(next_g - king_g) <= 1):
            print("Yes")
        else:
            print("No")
    else:
        print("no")
move_king(king_v, king_g, next_v, next_g)
