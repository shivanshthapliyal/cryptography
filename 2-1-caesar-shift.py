__author__ = "Shivansh Thapliyal"

#Shift Encryption for Capital letters ONLY !!

def Shift_Enc(pt,k):  
    n=len(pt)
    i=0
    ct=""
    newch=''
    while(n>0):
        ch = pt[i]
        n=n-1
        i=i+1
        newval=ord(ch)+k
        if(newval>90):
            newval=newval-90
            newch=chr(ord('A') + newval-1)
        else:
            newch=chr(ord(ch) + k)
        ct=ct+newch

    return ct


def Shift_Dec(pt,k):  
    n=len(pt)
    i=0
    ct=""
    newch=''
    while(n>0):
        ch = pt[i]
        n=n-1
        i=i+1
        newval=ord(ch)-k
        if(newval<65):
            newval=newval-65
            newch=chr(ord('Z') - newval-1) 
        else:
            newch=chr(ord(ch) - k)
        ct=ct+newch

    return ct


StartingString = "ABCZBCDEAFJA"
print("OriginalString \t\t= \t",StartingString)

EncryptedString = Shift_Enc(StartingString,2)
print("EncryptedString \t= \t",EncryptedString)
DecryptedString = Shift_Dec(EncryptedString,2)
print("DencryptedString \t= \t",DecryptedString)