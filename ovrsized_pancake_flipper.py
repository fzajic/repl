def read_pancakes(line):
    fin = open("pancakes.txt", "r")
    for i in range(line):
        pancakes_string = fin.readline()
        pancakes_list = []
        for f in range(len(pancakes_string)-1):
            pancakes_list.append(pancakes_string[f])
    fin.close()
    return pancakes_list

def are_all_happy(pancakes):
    sample = []
    for i in range(len(pancakes)):
        sample.append("+")
    if sample == pancakes:
        return True
    else:
        return False

def swap(element): #swap - for +, or vice versa
    if element == "+": return "-"
    else: return"+"

def flip_pancakes(pancakes, start_index):
    for index in range(start_index, start_index + flipper_size):
        pancakes[index] = swap(pancakes[index])
    return pancakes

flipper_size = 3#input("what is size of the flipper? \n")

pancakes = read_pancakes(2)

print(are_all_happy(pancakes))
