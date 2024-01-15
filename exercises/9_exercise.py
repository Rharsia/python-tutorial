# palindrome checker
import math

cislo1 = "123321"
# cislo2 = "98789"

len(cislo1)

def palindrome_checker(cislo):

    cislo = str(cislo)

    if len(cislo) % 2 == 0:
        stav = "sudy"
    else:
        stav = "lichy"

    if stav == "sudy":
        polovina = len(cislo)/2
        polovina = int(polovina)

        prvni_cast = cislo[0:polovina]
        prvni_cast

        druha_cast = cislo[polovina:]
        druha_cast
    else: 
        polovina = math.floor(len(cislo)/2)

        prvni_cast = cislo[:polovina]


    predek = []
    zadek = []

    for pismeno in prvni_cast:
        predek.append(pismeno)
    predek

    for pismeno in druha_cast:
        zadek.insert(0, pismeno)
    zadek

    if predek == zadek:
        print("Je to palindrom")
    else:
        print("Neni to palindrom")

palindrome_checker()


math.floor(2.5)