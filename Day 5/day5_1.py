import re

input = open('input').read()
_, order = input.split('\n\n')
order = order.split('\n')

temp = []
for job in order:
    temp_job = re.findall(r'\d+', job)
    temp.append(temp_job)
order = temp

# Hard coded as couldn't figure out a way to read input
crates = [['D', 'T', 'W', 'N', 'L'], 
          ['H', 'P', 'C'], 
          ['J', 'M', 'G', 'D', 'N', 'H', 'P', 'W'],
          ['L', 'Q', 'T', 'N', 'S', 'W', 'C'], 
          ['N', 'C', 'H', 'P'], 
          ['B', 'Q', 'W', 'M', 'D', 'N', 'H', 'T'],
          ['L', 'S', 'G', 'J', 'R', 'B', 'M'], 
          ['T', 'R', 'B', 'V', 'G', 'W', 'N', 'Z'], 
          ['L', 'P', 'N', 'D', 'G', 'W']]
#crates = [['N', 'Z'], ['D', 'C', 'M'], ['P']]

for job in order:
    n_crates, start, dest = int(job[0]), int(job[1]), int(job[2])
    for i in range(n_crates):
        crates[dest-1].insert(0, crates[start-1].pop(0))

rearrengement_seq = ''
for crate in crates:
    rearrengement_seq += crate.pop(0)
print(rearrengement_seq)