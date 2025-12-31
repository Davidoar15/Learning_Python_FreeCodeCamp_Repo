def fibonacci(n:int) -> int:
    sequence = [0, 1]

    if n < 2: return sequence[n]

    for i in range(2, n + 1):
        next_value = sequence[i - 1] + sequence[i - 2]
        sequence.append(next_value)

    return sequence[n]
  
print(fibonacci(3)) # 2
print(fibonacci(1)) # 1
