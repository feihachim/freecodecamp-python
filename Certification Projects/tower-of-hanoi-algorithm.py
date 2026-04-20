"""
In this lab, you will solve the mathematical puzzle known as the Tower of Hanoi.
The puzzle consists of three rods and a number of disks of different diameters.
"""


def hanoi_solver(n):
    src = "A"
    aux = "C"
    des = "B"

    # 1 << n == 2**n
    total_moves = 1 << n - 1
    if n % 2 == 0:
        des, aux = aux, des

    rods: dict[str, list[int]] = {"A": list(range(n, 0, -1)), "B": [], "C": []}
    result = f"{rods[src]} {rods[aux]} {rods[des]}\n"
    for move in range(1, total_moves + 1):
        if move % 3 == 1:
            from_rod, to_rod = (
                ("A", "B")
                if (rods["A"] and (not rods["B"] or rods["A"][-1] < rods["B"][-1]))
                else ("B", "A")
            )
        elif move % 3 == 2:
            from_rod, to_rod = (
                ("A", "C")
                if (rods["A"] and (not rods["C"] or rods["A"][-1] < rods["C"][-1]))
                else ("C", "A")
            )
        else:
            from_rod, to_rod = (
                ("B", "C")
                if (rods["B"] and (not rods["C"] or rods["B"][-1] < rods["C"][-1]))
                else ("C", "B")
            )

        disk = rods[from_rod].pop()
        rods[to_rod].append(disk)
        # print(f"Move disk {disk} from {from_rod} to {to_rod}")
        result += f"{rods[src]} {rods[aux]} {rods[des]}\n"
    print(result)
    return result[:-1]


hanoi_solver(1)
hanoi_solver(2)
hanoi_solver(3)
