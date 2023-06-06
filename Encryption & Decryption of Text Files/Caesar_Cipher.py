def Caesar_Cipher():
    X=input("Enter 'E' if you want to encrypt the file or enter 'D' to decrypt the file : ")
    if X=="E" :
       file_name=input("Enter the name of the file that has to be encrypted : ")
       f=open(file_name+".txt","r")
       plain_message=f.read()

       key=int(input("Enter the key: "))
       
       encrypted_message=""
       #Traversing plain_message
       for i in range(len(plain_message)):
           char=plain_message[i]

           #Encrypting uppercase characters
           if (char.isupper()):
               encrypted_message += chr((ord(char) + key-65) % 26 + 65)
               
           #Encrypting lowercase characters
           elif (char.islower()):
               encrypted_message += chr((ord(char) + key - 97) % 26 + 97)
               
           else:
               encrypted_message=encrypted_message+char
               
       encrypted_file_name=input("Enter the name of the file that stores the encrypted data : ")
       encry_file=open(encrypted_file_name+".txt","w")
       encry_file.write(encrypted_message)
       encry_file.close()

    elif X=="D" :
       key=int(input("Enter key : "))
       decrypted_text = ""

       file_name=input("Enter the name of the file that has to be decrypted : ")
       f=open(file_name+".txt","r")
       encrypted_text=f.read()
       for c in encrypted_text:
           #Checking if character is an uppercase letter
           if c.isupper():
               #Finding the position in 0-25
               c_index = ord(c) - ord("A")
               #Perform the reverse shift
               new_index = (c_index - key) % 26
               #Converting to new character
               new_uni=new_index + ord("A")
               new_ch=chr(new_uni)
               #Append it to plain string
               decrypted_text=decrypted_text + new_ch
               
           #Checking if character is an uppercase letter  
           elif c.islower():
               #Finding the position in 0-25
               c_index = ord(c) - ord("a")
               #Perform the reverse shift
               new_index = (c_index - key) % 26
               #Converting to new character
               new_uni = new_index + ord("a")
               new_ch = chr(new_uni)
               #Append it to plain string
               decrypted_text=decrypted_text + new_ch
               
           #Since character is not uppercase or lowercase concatenate it    
           else:
               decrypted_text += c
               
       encrypted_file_name=input("Enter the name of the file that stores the decrypted data : ")
       encry_file=open(encrypted_file_name+".txt","w")
       encry_file.write(decrypted_text)
       encry_file.close()

    else:
         print("Entered option is wrong")


if __name__ == "__main__":
    caesar_cipher()