sequence = open('input', 'r').read().split(',')

boxes = [dict() for _ in range(256)]

for seq in sequence:
    current_value = 0
    remain = ""
    box_name = ""
    for i,ch in enumerate(seq):
        if ch == "=" or ch == "-":
            remain = seq[i:]
            break
        current_value += ord(ch)
        current_value *= 17
        current_value = current_value % 256
        box_name += ch

    if remain[0] == "=":
        exist = False
        for box in boxes[current_value]:
            if box_name in box:
                exist = True
        
        if not exist:
            boxes[current_value][box_name] = int(remain[-1])
        else:
            for box in boxes[current_value]:
                if box_name in box:
                    if int(remain[-1]) == boxes[current_value][box]:
                        break
                    else:
                        boxes[current_value][box_name] = int(remain[-1])
                        break

    elif remain[0] == "-":
        if box_name in boxes[current_value]:
            boxes[current_value].pop(box_name)
    else:
        print("Why is this happening?")


focusing_power = 0
for box_id, box in enumerate(boxes):
    for i, (key, value) in enumerate(box.items()):
        focusing_power += ((box_id + 1) * (i + 1) * int(value))

print(focusing_power)
print(focusing_power - 286097)
# 286097

