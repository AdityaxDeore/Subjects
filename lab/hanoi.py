# TOWER OF HANOI

def solve_hanoi(n, source, aux, dest):
    if n == 1:
        print("Move disk 1 from", source, "to", dest)
        return
    solve_hanoi(n - 1, source, dest, aux)
    print("Move disk", n, "from", source, "to", dest)
    solve_hanoi(n - 1, aux, source, dest)


def solve_hanoi_collect(n, source, aux, dest, moves=None):
    if moves is None:
        moves = []
    if n == 1:
        moves.append((1, source, dest))
        return moves
    solve_hanoi_collect(n - 1, source, dest, aux, moves)
    moves.append((n, source, dest))
    solve_hanoi_collect(n - 1, aux, source, dest, moves)
    return moves


def main():
    n = int(input("Enter the number of disks: "))
    solve_hanoi(n, "A", "B", "C")


if __name__ == "__main__":
    main()