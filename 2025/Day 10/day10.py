from itertools import combinations

ans = 0
lines = open("test.in").read().splitlines()

for line in lines:
    parts = line.split()

    lights_raw = parts[0][1:-1]
    buttons_raw = parts[1:-1]

    lights = []
    for c in lights_raw:
        lights.append(c == "#")

    buttons = []
    for button in buttons_raw:
        buttons.append(eval(button[:-1] + ",)"))
    
    it_done = False
    for n in range(len(buttons) + 1):
        for pressed in combinations(buttons, n):
            state = []

            for i in range(len(lights)):
                count = 0
                for p in pressed:
                    if i in p:
                        count += 1
                state.append(count % 2)

            if state == lights:
                ans += n
                it_done = True
                break
        
        if it_done:
            break

print(ans)