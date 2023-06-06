def Brute_Force():
    file_name=input("Enter the name of the file that has to be decrypted : ")
    f=open(file_name+".txt","r")
    encrypted_text=f.read()
    decrypted_text=''
    plain_text = ""

    plain_text = ""

    for shift in range(0,26):
        print("Decrypted text:",plain_text)
        plain_text=''
        print("Key",shift,end=':')
        for c in encrypted_text:

    #Checking if character is an uppercase letter
            if c.isupper():
            #Finding the position in 0-25
                c_index = ord(c) - ord("A")
                #Perform the reverse shift
                new_index = (c_index - shift) % 26
                #Converting to new character
                new_unicode = new_index + ord("A")
                new_character = chr(new_unicode)
                #Append it to plain string
                plain_text = plain_text + new_character

            elif c.islower():
                #Finding the position in 0-25
                c_index = ord(c) - ord("a")
                #Perform the reverse shift
                new_index = (c_index - shift) % 26
                #Converting to new character
                new_unicode = new_index + ord("a")
                new_character = chr(new_unicode)
                #Append it to plain string
                plain_text = plain_text + new_character
                
            #Since character is not uppercase or lowercase concatenate it
            else:
                plain_text += c

    print("Encrypted text : ",encrypted_text)

if __name__ == "__main__":
    brute_force()