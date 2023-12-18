import math

def TD_measurement(t, td): # max time, current time trial
    # if time presse == 0, return 0
    # time pressed - max time = how many seconds it will move
    # distance = time pressed * (time pressed - max time)
    if td == 0:
        return 0

    time_pressed = t - td
    distance = abs(time_pressed * (time_pressed - t))
    #print("Time: ", t, ", Current time trail: ", td, ", Time pressed: ", time_pressed, ", Distance: ", distance)

    return distance


def prepare_data():
    data_sheet = open('input', 'r').read().split()
    dgs = [int(digit) for digit in data_sheet if digit.isdigit()]
    time, distance = dgs[:len(dgs)//2], dgs[len(dgs)//2:]
    return time, distance

def calc_races(time,distance, p1=True):
    if p1:
        data = zip(time,distance)
    else:
        data = zip([time], [distance])

    race_counter = []
    for t,d in data:
        counter = 0
        for td in range(t+1):
            rd = TD_measurement(t, td)
            if rd > d:
                counter += 1

        race_counter.append(counter)

    return race_counter


time,distance = prepare_data()
print(math.prod(calc_races(time, distance))) # p1

time_2, distance_2 = int(''.join(map(str, time))), int(''.join(map(str, distance)))
print(math.prod(calc_races(time_2, distance_2, p1=False)))