from british_coin_module import BritishCoin    

def main():
    
    theBritishCoin = BritishCoin()

    selection = 'a';
    while selection != 'q':
        print("\nq\tType: ")
        print("\t\tf - to flip the coin")
        print("\t\tq - to quit\n")

        selection = input("\tEnter selection: ")
        if selection[0] == 'f':
            theBritishCoin.flip()
            print("\n\tThe result is: " + str(theBritishCoin))
 

    print("\tPROGRAM ENDED\n")

if __name__ == "__main__":
    main()

