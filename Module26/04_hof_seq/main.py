def q_gen(q: list, n: int) -> list:
    if q != [1, 1]:
        return

    for i in range(n-2):
        q.append(q[i - q[-1]] + q[i - q[-2]])

    yield q


number = int(input('Enter the number: '))
for lst in q_gen(q=[1, 1], n=number):
    print(lst)

