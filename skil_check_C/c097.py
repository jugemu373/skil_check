answer = input()
tmp = answer.split()
n = int(tmp[0])
x = int(tmp[1])
y = int(tmp[2])
winners = []
for i in range(n+1):
    if i == 0:
         continue
    if i % x == 0 and i % y == 0:
        winners.append("AB")
    elif i % x == 0:
        winners.append("A")
    elif i % y == 0:
        winners.append("B")
    else:
        winners.append("N")

for winner in winners:
    print(winner)