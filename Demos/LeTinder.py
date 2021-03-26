def interest():
    print("Enter your interest, one after the other, and enter \"STOP\" to end.")
    set1 = set()
    activity = ""
    while True:
        activity = input()
        if activity == "stop":
            break
        set1.add(activity)
    return set1


def tinderTheSecond():
    print("First Person: ")
    P1set = interest()
    print("Second Person: ")
    P2set = interest()
    common = P1set.intersection(P2set)
    if len(common) > 4:
        print(f"Yay - you are a match! you have {len(common)} interest in common!")
    else:
        print(f"Well, don't think it will work out :(, you have {len(common)} interest in common")


tinderTheSecond()