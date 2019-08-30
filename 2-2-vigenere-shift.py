
def genKey(str1,n):
    n1 = len(str1)
    str2=""
    c=0
    for i in range(0,n):
        if(c>=n1):
            c=0
        str2=str2 + str1[c]  # as strings are immutable, so you can't change their characters in-place.
        c=c+1
    return str2


def genCipherText(k, str):
    cipherText=""
    for i in range(0,len(k)):
        n1 = ord(str[i])-64
        n2 = ord(k[i])-64

        n3 = n1+n2-1
        if n3>26:
            n3 = n3-26

        cipherText = cipherText+chr(n3+64)
    return cipherText

def genOriginalText(k, str):
    originalText=""
    for i in range(0,len(k)):
        n1 = ord(str[i])-64
        n2 = ord(k[i])-64

        n3 = n1-n2+1
        if n3<0:
            n3 = 26+n3

        originalText = originalText+chr(n3+64)
    return originalText


#     A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
#     ---------------------------------------------------
# A   A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# B   B C D E F G H I J K L M N O P Q R S T U V W X Y Z A
# C   C D E F G H I J K L M N O P Q R S T U V W X Y Z A B
# D   D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
# E   E F G H I J K L M N O P Q R S T U V W X Y Z A B C D
# F   F G H I J K L M N O P Q R S T U V W X Y Z A B C D E
# G   G H I J K L M N O P Q R S T U V W X Y Z A B C D E F
# H   H I J K L M N O P Q R S T U V W X Y Z A B C D E F G
# I   I J K L M N O P Q R S T U V W X Y Z A B C D E F G H
# J   J K L M N O P Q R S T U V W X Y Z A B C D E F G H I
# K   K L M N O P Q R S T U V W X Y Z A B C D E F G H I J
# L   L M N O P Q R S T U V W X Y Z A B C D E F G H I J K
# M   M N O P Q R S T U V W X Y Z A B C D E F G H I J K L
# N   N O P Q R S T U V W X Y Z A B C D E F G H I J K L M
# O   O P Q R S T U V W X Y Z A B C D E F G H I J K L M N
# P   P Q R S T U V W X Y Z A B C D E F G H I J K L M N O
# Q   Q R S T U V W X Y Z A B C D E F G H I J K L M N O P
# R   R S T U V W X Y Z A B C D E F G H I J K L M N O P Q
# S   S T U V W X Y Z A B C D E F G H I J K L M N O P Q R
# T   T U V W X Y Z A B C D E F G H I J K L M N O P Q R S
# U   U V W X Y Z A B C D E F G H I J K L M N O P Q R S T
# V   V W X Y Z A B C D E F G H I J K L M N O P Q R S T U
# W   W X Y Z A B C D E F G H I J K L M N O P Q R S T U V
# X   X Y Z A B C D E F G H I J K L M N O P Q R S T U V W
# Y   Y Z A B C D E F G H I J K L M N O P Q R S T U V W X
# Z   Z A B C D E F G H I J K L M N O P Q R S T U V W X Y


# Trial 
# HelloWorldhuahauhau
# qweqweqweqweqweqweq


# l=12
# e=5
# l+e=17   and 12-1=16 thus p


def main():

    str = input("Enter string you want to encrypt: ")
    str1 = input("Enter secret key: ")

    n=len(str)

    k = genKey(str1, n)

    cipherText = genCipherText(k,str)
    originalText = genOriginalText(k,cipherText)

    print("\n\nOriginal String =\t",str) 
    print("Key = \t\t\t",k)
    print("\n\n\t----------After Encryption----------\n")
    print("Encrypted Cipher =\t",cipherText) 
    print("\n\n\t----------After Decryption----------\n")
    print("Decrypted Cipher =\t",originalText) 


if __name__ == "__main__":
    main()


