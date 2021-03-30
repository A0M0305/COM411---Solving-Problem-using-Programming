# def observed():
#    observations = set()
#    print("Enter what you saw")
#    view = ""
#    while True:
#        view = input()
#        if view == "0":
#            break
#        observations.add(view)
#    return observations

def observed():
    observations = []
    print("Please enter an observation:")
    for x in range(7):
        #        x = input() You dont need to add this no more as can be added in the append as below.
        observations.append(input())
    return observations


def run():
    print("Counting observations...")
    list_of_observations = observed()  # this will bring from the above to be stored in this.
    set_of_observations = set()
    for i in range(len(list_of_observations)):
        set_of_observations.add(list_of_observations[i])
    set_of_tuples = set()
    for item in set_of_observations:
        count = 0
        for i in range(len(list_of_observations)):
            if list_of_observations[i] == item:
                count += 1
        set_of_tuples.add((item, count))
    print(set_of_tuples)


run()
