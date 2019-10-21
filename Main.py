#Tyler Strom
#Plant Inventory Program

file = open("plant inventory.txt", 'r+')
lines = file.readlines()
while(True):
    choice = int(input("1. Buy Item \n2. View Items \n3. Exit \n"))
    if choice == 1:
        print("Plant\tPrice\tAvailability")
        items = []
        for line in lines:
            Plant, Price, Availability = line.split(',')
            print(Plant,"\t",Price,"\t", Availability)
            items.append(Plant)
        print("Which plant do you want to buy:", items)
        item_choice = input()
        if item_choice not in items:
            print("Plant is not available. . Sorry!\n")
            break
        else:
            for l in range(len(lines)):
                if lines[l].split(',')[0] == item_choice:
                    Plant,Price,Availability = lines[1].split(',')
                    Availability = int(Availability)-1
                    lines[1]= ','.join(Plant)
            print("Thank you for your business!")
    elif choice == 2:
                    print("Plant\tPrice\tAvailabilty")
                    for line in lines:
                        Plant, Price, Availability = line.split(',')
                        print(Plant, "\t", Price, "\t", Availability)
    else:
        file.seek(0)
        for line in lines:
            file.close()
            break





