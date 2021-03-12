print("How many bars should be charged?")
charge = int(input())

bars_charged = 0
print()

while (bars_charged < charge):
    bars_charged = bars_charged + 1
    print("Charging:", "█" * bars_charged)
    
print("The battery is fully charged.")