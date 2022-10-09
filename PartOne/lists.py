groceryList = []

def main():
    while(True):
        userInput = int(input("Would you like to\n(1)Add or\n(2)Remove items or\n(3)Quit?: "))
        if userInput == 1:
            adder()
        elif userInput == 2:
            remover()
        elif userInput == 3:
            print("The following items remain in the list:")
            for x in range(len(groceryList)):
                print(groceryList[x])
            break
        else:
            print("Incorrect selection.")

def adder():
    addItem = str(input("What will be added?: "))
    groceryList.append(addItem)

def remover():
    listLength = len(groceryList)
    print("There are ", listLength, " items in the list.")
    remove = int(input("Which item is deleted?: "))
    if remove < len(groceryList):
        del groceryList[remove]
    else:
        print("Incorrect selection.\n")

if __name__=="__main__":
    main()