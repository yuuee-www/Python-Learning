from coin import Coin


def main():
    
    for i in range(99) :
        coin = Coin()
        print(coin, end=", ")
    coin = Coin()
    print(coin, end="." )
                
    print("\n\nHeads so far: ", Coin.get_heads_so_far())
    print("Tails so far: ", Coin.get_tails_so_far())
    
    print("\nBye, Bye!\n")
        

if __name__ == "__main__":
    main()

