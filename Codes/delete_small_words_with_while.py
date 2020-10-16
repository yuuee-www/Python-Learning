def main():
    words = ["Welcome", "to", "the", "island!"]

    print("\n", words)
    i = 0
    print()
    while i < len(words): #dont use for loop
        print("\ti: {}, {}".format(i, words[i]))
        word = words[i]
        if len(word) < 4 :      
            words.pop(i) 
        else :
            i = i + 1

    print("\n", words)

if __name__ == "__main__":
    main()