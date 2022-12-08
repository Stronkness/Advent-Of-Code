commands = open('testinput').read().split('\n')

upper_limit = 10000

path = []
directories = {}
directories["/"] = {}
set_current = ''
path.append(set_current)
for command in commands:
    if(command[0] == '$'):
        command = command.split(' ')
        if(command[1] == 'cd'):
            if(command[2] in directories.keys()):
                print("hej")
            else:
                directories[set_current] += command[3]
print(directories)