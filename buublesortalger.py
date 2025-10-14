import random

def bubblesort(list):
    
    maxidx = len(list)-1
    sorted_list = list
    count = 1
    while True:
        #print(f"count:{count}")
        swapped = False
        for idx, number in enumerate(list):
            if idx != maxidx:
                compare = [list[idx], list[idx+1]]
            if compare[1] < compare[0]: # value at idx is smaller than the value at idx + 1
                sorted_list[idx]= compare[1]
                if idx != maxidx:
                    sorted_list[idx+1] = compare[0]
                    swapped = True
                else:
                    sorted_list[-1] = compare[0]
                    swapped = True
        count += 1
        if not swapped:
            break
    return sorted_list

def random_test_cases():
    nlist = [random.randint(0, 100) for _ in range(0, random.randint(2, 10))]
    print(f"unsorted :{nlist}")
    sortIt = bubblesort(nlist)
    print(f"sorted list:{sortIt}")
    print()
for i in range(0, 10):
    random_test_cases()

# hellp me now, i'n testing out the bracnhes.