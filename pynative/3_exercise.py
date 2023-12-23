str = "pynative"


# reseni Michal
for i in range(len(str)):

    if i % 2 == 0:
        print(str[i])

# jine reseni
for i in range(0, len(str), 2):
    print(str[i])

# slicing
print(str)

str[:]

str[2:6]

str[:5]

str[3:]

for pismeno in str[0::2]:
    print(pismeno)