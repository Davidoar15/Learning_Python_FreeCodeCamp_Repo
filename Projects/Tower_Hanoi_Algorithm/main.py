def hanoi_solver(n):
    source_rod = list(range(n, 0, -1))
    auxiliary_rod = []
    target_rod = []

    result = []

    def move(disks, source, auxiliary, target):
        if disks == 0: return

        move(disks - 1, source, target, auxiliary)

        target.append(source.pop())

        result.append(f"{source_rod} {auxiliary_rod} {target_rod}")

        move(disks - 1, auxiliary, source, target)

    result.append(f"{source_rod} {auxiliary_rod} {target_rod}")
    move(n, source_rod, auxiliary_rod, target_rod)

    return "\n".join(result)
  
print(hanoi_solver(3))
