from functools import cmp_to_key
import collections

def compare_pages(page1, page2):
    count1 = 0
    count2 = 0
    
    for order in rules[page1]:
        if order in pages:
            count1 += 1

    for order in rules[page2]:
        if order in pages:
            count2 += 1

    score1 = -count1
    score2 = -count2

    if score1 < score2:
        return -1
    elif score1 > score2:
        return 1
    else:
        return 0


input = open("small.in").read().split("\n\n")
rules = collections.defaultdict(list)
for row in input[0].split("\n"):
    first, second = map(int, row.split("|"))
    rules[first].append(second)
updates = [[int(update) for update in upd.split(",")] for upd in input[1].split("\n")]

sum = 0
for pages in updates:
    sorted_pages = sorted(pages, key=cmp_to_key(compare_pages))
    if pages == sorted_pages:
        sum += pages[len(pages) // 2]

print(sum)