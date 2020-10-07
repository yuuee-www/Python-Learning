def break_cipher():
    message = input("Please enter a text:")
    Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = message.upper()

    for k in range(26):
        Text = ''

        for i in message:
            if i in Alphabet:
                n = Alphabet.index(i)
                n += k

                Text += Alphabet[n%26]
            else:
                Text += i
        
        print(f"key {k}:{Text}.")

if __name__ =="__main__":
    break_cipher()
