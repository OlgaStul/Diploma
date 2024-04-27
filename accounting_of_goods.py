result = {}

for i in range(int(input("Введите количество клиентов: "))):
    name, surname, product, count = input(
        "Введите через пробелы имя, фамилию, товар и количество: ").split()
    fio = (name, surname)
    result.setdefault(fio, {})
    result[fio][product] = result[fio].get(product, 0)+int(count)
print()

for key, value in sorted(result.items()):
    print(f'{" ".join(key)}:')
    for i in sorted(value):
        print(i, value[i])
    print()







