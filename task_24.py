import random

n = int(input("Сколько кустов? "))
bushes = []
while len(bushes) != n:
    i = random.randint(1, n)
    if i not in bushes:
        bushes.append(i)
max_berries = 0
for i in range(len(bushes)):
    if bushes[i] + bushes[i - 1] + bushes[i - 2] > max_berries:
        max_berries = bushes[i] + bushes[i - 1] + bushes[i - 2]

print(bushes)
print(max_berries)
