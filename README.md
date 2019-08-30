# Cryptography

## 1: Classical Encryption Techniques

### Objective: - To understand the concept of passwords, Brute Force Techniques.

1. Develop a program to show the workings of substitution method.
2. Develop a login system, which will take two inputs username and password (4 digit
pin). As an Adversary develop a program, which will generate passwords serially, and
find the right password for the developed login system.

-------------------------------------------------------------------------------------

## 2: Shift Cipher Techniques

### Objective: - To understand the concept of Shift Ciphers.

1. Implement a program to show the working of Caesar cipher.

The Caesar cipher is one of the earliest known and simplest ciphers. It is a type of substitution cipher in which each letter  in the plaintext is 'shifted' a certain number of places down the alphabet. For example, with a shift of 1, A would be replaced by B, B would become C, and so on. The method is named after Julius Caesar, who apparently used it to communicate with his generals.

2. Implement a program to show the working of Vigenère cipher.

The Vigenère Cipher is a polyalphabetic substitution cipher. The method was originally described by Giovan Battista Bellaso in his 1553 book La cifra del. Sig. Giovan Battista Bellaso; however, the scheme was later misattributed to Blaise de Vigenère in the 19th century, and is now widely known as the Vigenère cipher.

Blaise de Vigenère actually invented the stronger Autokey cipher in 1586.


The Vigenere Cipher uses the following tableau (the 'tabula recta') to encipher the plaintext:

    A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
    ---------------------------------------------------
A   A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
B   B C D E F G H I J K L M N O P Q R S T U V W X Y Z A
C   C D E F G H I J K L M N O P Q R S T U V W X Y Z A B
D   D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
E   E F G H I J K L M N O P Q R S T U V W X Y Z A B C D
F   F G H I J K L M N O P Q R S T U V W X Y Z A B C D E
G   G H I J K L M N O P Q R S T U V W X Y Z A B C D E F
H   H I J K L M N O P Q R S T U V W X Y Z A B C D E F G
I   I J K L M N O P Q R S T U V W X Y Z A B C D E F G H
J   J K L M N O P Q R S T U V W X Y Z A B C D E F G H I
K   K L M N O P Q R S T U V W X Y Z A B C D E F G H I J
L   L M N O P Q R S T U V W X Y Z A B C D E F G H I J K
M   M N O P Q R S T U V W X Y Z A B C D E F G H I J K L
N   N O P Q R S T U V W X Y Z A B C D E F G H I J K L M
O   O P Q R S T U V W X Y Z A B C D E F G H I J K L M N
P   P Q R S T U V W X Y Z A B C D E F G H I J K L M N O
Q   Q R S T U V W X Y Z A B C D E F G H I J K L M N O P
R   R S T U V W X Y Z A B C D E F G H I J K L M N O P Q
S   S T U V W X Y Z A B C D E F G H I J K L M N O P Q R
T   T U V W X Y Z A B C D E F G H I J K L M N O P Q R S
U   U V W X Y Z A B C D E F G H I J K L M N O P Q R S T
V   V W X Y Z A B C D E F G H I J K L M N O P Q R S T U
W   W X Y Z A B C D E F G H I J K L M N O P Q R S T U V
X   X Y Z A B C D E F G H I J K L M N O P Q R S T U V W
Y   Y Z A B C D E F G H I J K L M N O P Q R S T U V W X
Z   Z A B C D E F G H I J K L M N O P Q R S T U V W X Y

-------------------------------------------------------------------------------------

## 3: DES Encryption Techniques

### Objective: - To understand the concept of Block Ciphers

1. Implement the Data Encryption Standards.

-------------------------------------------------------------------------------------

## 4: AES Encryption Techniques

### Objective: - To understand the concept of Block Ciphers

1. Implement the Advanced Encryption Standards.

-------------------------------------------------------------------------------------

## 5: Public key Cryptography:

### Objective: - To understand the concept of secret key, cipher and plain text.

1. Design a system, which will demonstrate the working of RSA public key
cryptography.

-------------------------------------------------------------------------------------

## 6: Diffie Hellman Key Exchange Algorithm:

### Objective: - To understand the concept of exchanging keys through Diffie Hellman.

1. Design a system, which will demonstrate the working of Diffie Hellman.

-------------------------------------------------------------------------------------

## 7: Hash Function

### Objective: - To understand the concept of Integrity, Non-repudiation and message
digest.

1. Write a program to demonstrate the working of SHA-512.
2. Create a mail (treat it as a string) and attach the digital signature with your mail.
show that the attached digital signature can be used to:
a. Verify the author and the date and time of the signature.
b. Authenticate the contents at the time of the signature.
