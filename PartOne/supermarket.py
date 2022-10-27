superMarket = [10,14,22,33,44,13,22,55,66,77]

def main():
    sum = 0
    print("Supermarket")
    print("===========")
    while(True):
        userInput = int(input("Please select product (1-10) 0 to Quit: "))
        if userInput in range(1,11):
            sum = sum + superMarket[userInput-1]
            print("Product: " + str(userInput) + " Price: " + str(superMarket[userInput-1]))
        elif userInput == 0:
            print("Total: " + str(sum))
            userIn = int(input("Payment: "))
            print("Change: " + str(userIn-sum))
            break
        else:
            print("Incorrect selection.")

if __name__=="__main__":
    main()