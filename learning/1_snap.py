def prumer():
    s = 0
    a = 1
    c = 0 
    while a != 0:
        uin = int(input("Zadej cislo: "))
        a = uin
        s += a
        c += 1

        print(f"a = {a}, s = {s}, c = {c}")

    # d
    # return s/c

    # e
    c -= 1
    if c != 0:
        return s/c

prumer()


def funkce_6():
    limit = 0
    c = 0
    a = 5
    while a != 0:
        uin = int(input("Zadej cislo: "))
        a = uin
        if limit == 0:
            # a = limit
            limit = a
        else: 
            if a > limit:
                c += 1
        print(f"limit = {limit}, a = {a}, c = {c}")

    return c

funkce_6()


def funkce(x):
    if x > 1:
        return funkce(x-1)*x
    else:
        return 1

def funkce_7():
    return funkce(4) + funkce(3)

funkce_7()



for i in range(100):
    if i**2 + (i+1)**2 == 61:
        print(f"Nase cisla jsou {i} a {i+1}")
        break
    else:
        print(f"{i} a {i+1} to nejsou")
