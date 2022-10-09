def main():
    while True:
        given = input("Write something (quit ends): ")
        if given == "quit":
            break
        tester(given)

def tester(given):
    givenstring = "Too short"
    if len(given) < 10:
        print(givenstring)
    else:
        print(given)

if __name__=="__main__":
    main()