money=int(input("Сумма вклада:"))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
values = list(per_cent.values())

deposit0 = ([i * money for i in values])
deposit = [int(x) for x in deposit0]

print("Депозит:", deposit)

depositmax=max(deposit)
print("Максимальная сумма вклада:",depositmax)
