shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]
summ, count = 0, 0
detail = input('Enter detail name: ')

for lst in shop:
        if lst[0] == detail.lower():
                summ += lst[1]
                count += 1

print('Number of details:', count, '\nTotal cost:', summ)
