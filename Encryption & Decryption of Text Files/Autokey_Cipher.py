def Autokey_Cipher():
    X=input("To encrypt Then enter alphabet E or To decrypt Then enter alphabet D : ")
    if X=="E" :
        #Program for encryption using autokey cipher
        alpha=[]
        for i in range(32,127):
            alpha.append(chr(i))
        alpha.append(chr(10))

        file_name=input("Enter the name of file that need to be encrypted : ")
        f=open(file_name+".txt","r")
        F=f.read()

        text_encrypt=""

        key=input("Enter the autokey : ")
        A_K=key+F[0:len(F)-len(key)]
        #save the autokey for decryption
        Autokey=input("Enter the file where Autokey need to be saved : ")
        Auto_key_file=open(Autokey+".txt","w")
        Auto_key_file.write(A_K)
        Auto_key_file.close()

        #encrypting:

        for i in range(len(A_K)):
            s=(alpha.index(F[i])+alpha.index(A_K[i]))%96
            text_encrypt+=alpha[s]

        encrypt_file=input("Enter the file where encrypted text need to be saved : ")
        encry_file=open(encrypt_file+".txt","w")
        encry_file.write(text_encrypt)
        encry_file.close()
        print()
        print()
    
    elif X=="D":
        #Program for decryption using autokey cipher

        alpha=[]
        for i in range(32,127):
            alpha.append(chr(i))
        alpha.append(chr(10))
        
        file_name=input("Enter the name of file that need to be decrypted : ")
        a=open(file_name+".txt","r")
        A=a.read()

        text_decrypt=""
        file_name=input("Enter the name of file that has Autokey : ")
        x=open(file_name+".txt","r")
        A_K=x.read()

        for i in range(len(A_K)):
            s=(alpha.index(A[i])-alpha.index(A_K[i]))%96
            text_decrypt+=alpha[s]

        decrypt_file=input("Enter the file where decrypted text need to be saved : ")
        decry_file=open(decrypt_file+".txt","w")
        decry_file.write(text_decrypt)
        decry_file.close()

    else:
        print("Entered option is wrong")


if __name__ == "__main__":
    autokey_cipher()

