# Fermat Prime Divisibility

import re

file_name = "even_sp.txt"
file = open(file_name, "r")
text = file.read()

fermat_primes = [3, 5, 17, 257, 65537]

for num in re.findall(r"Number:\s*(\d+)", text):
    num = int(num)
    divisible = False
    for fermat_num in fermat_primes:
        if num % fermat_num == 0:
            print(num, "%", fermat_num, "= 0")
            divisible = True
    if divisible == False:
        print(num, ": None", sep="")
    print()


file.close()
