
file = open("input2","r").read().splitlines()

digit_word = [
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine'
]

digits = [
    '1', '2', '3', '4', '5', '6', '7', '8', '9'
]

sum = 0
for line in file:
    n_1, n_2 = "", ""
    for n, w in zip(digits, digit_word):
        line = line.replace(w, w + n + w)

    for ch in line:
        if ch.isdigit():
            if not n_1:
                n_1 = ch
            else:
                n_2 = ch

    if not n_2:
        n_2 = n_1

    sum += int(n_1 + n_2)

print(sum)
