name = str(input())
cost = int(input())
weight = int(input())
money = int(input())

print("================Чек================")
print(f"Товар:{name:>29}")
print(f"Цена:{ str(weight) + 'кг * ' + str(cost) + 'руб/кг':>30}")
print(f"Итого:{weight * cost:>26}руб")
print(f"Внесено:{money:>24}руб")
print(f"Сдача:{money - (weight * cost):>26}руб")
print("===================================")
