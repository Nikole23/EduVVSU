# 1 задание

def arrangements_of_n_by_3(n):
    arrangements = []
    count = 0
    for i in range(n):
        for j in range(n):
            if j != i:
                for k in range(n):
                    if k != i and k != j:
                        arrangements.append((i, j, k))
                        count += 1
    formula_count = n * (n - 1) * (n - 2)  # Подсчет по формуле A(n, 3) = n * (n-1) * (n-2)
    return (arrangements, count, formula_count)

print (arrangements_of_n_by_3(5))