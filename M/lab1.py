import itertools

# 1 task
numbers = [4, 6, 2, 4, 3, 6, 4, 2, 1, 3, 2]
frequency = {}

for number in numbers:
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1

sorted_frequency = sorted(frequency.items())

for element, count in sorted_frequency:
    print(f"{element}: {count}")

print("......................................................")

# 2 task

print("......................................................")
# 3 task
places = [1, 2, 3, 4]

for perm in itertools.permutations(places):
    O, L, A, I = perm

    nina = (O == 1, L == 2)
    tanya = (O == 2, A == 3)
    dasha = (A == 4, I == 2)

    if sum(nina) == 1 and sum(tanya) == 1 and sum(dasha) == 1:
        print(f"Олег занял {O} место.")
        print(f"Леша занял {L} место.")
        print(f"Андрей занял {A} место.")
        print(f"Игорь занял {I} место.")
        break
print("......................................................")