#Substitution Encryption for Capital letters ONLY !!


def Sub_Enc(text,key,StartingString):  
    n=len(StartingString)
    i=0
    ct=""
    newch=''
    for it in StartingString:
        j=0
        pos=0
        for it2 in text:
            if(it==it2):
                pos=j
                break
            j=j+1

        newch = key[pos]
        ct=ct+newch
        n=n-1   
    return ct



def Sub_Dec(text,key,StartingString):  
    n=len(StartingString)
    i=0
    ct=""
    newch=''
    for it in StartingString:
        j=0
        pos=0
        for it2 in key:
            if(it==it2):
                pos=j
                break
            j=j+1

        newch = text[pos]
        ct=ct+newch
        n=n-1   
    return ct

# def printText():
#     n=65
#     text=[]
#     # i=0
#     while(n<=90):
#         text.append(chr(n))
#         n=n+1
        
#     print(text)

# printText()

text=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
key=['B', 'G', 'D', 'L', 'F', 'C', 'H', 'Z', 'J', 'K', 'E', 'N', 'M', 'O', 'W', 'Q', 'R', 'S', 'T', 'U', 'V', 'A', 'X', 'Y', 'I', 'P']


StartingString = "ABCZBCDEAFJA"
print("OriginalString \t\t= \t",StartingString)

EncryptedString = Sub_Enc(text,key,StartingString)
print("EncryptedString \t= \t",EncryptedString)
DecryptedString = Sub_Dec(text,key,EncryptedString)
print("DencryptedString \t= \t",DecryptedString)