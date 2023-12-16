hodnoty = ["C", "O", ".", "J", "E", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."]

result = []

def FA():
    a = input("Zadej hodnotu: ")

    if a == ".":
        pass
    else:
        FA()
        FA()

    result.append(a)

FA()

result


muj_list = [1,2,3,4]

muj_list

muj_list.append(1)