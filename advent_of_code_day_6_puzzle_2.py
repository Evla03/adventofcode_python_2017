import copy as c
memory = [14, 0, 15, 12, 11, 11, 3, 5, 1, 6, 8, 4, 9, 1, 8, 4]
stop = None
memory_history = ()
memory_new = []
result = 0
while stop < True:
    memory_history += (c.copy(memory),) 
    max_i = memory.index(max(memory)) # max index
    max_x = memory[max_i] # max nummer
    memory[max_i] = 0
    for i in range(max_x):
        max_i = (max_i + 1) % len(memory)
        memory[max_i] += 1
    if memory in memory_history:
        stop = True
        result = len(memory_history) - memory_history.index(memory)
print(result)
