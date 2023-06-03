n = int(input("Введите длину множества n: "))
m = int(input("Введите длину множества m: "))
first = set()
second = set()
while len(first) != n:
    first.add(int(input("Введите число: ")))

while len(second) != m:
    second.add(int(input("Введите число: ")))

list_1 = []

for elem in first:
    if elem in first and elem in second:
        list_1.append(elem)
for elem in second:
    if elem in first and elem in second and elem not in list_1:
        list_1.append(elem)
print(sorted(list_1))


