import math 

def gcd(a, h):
    temp = 0  
    while (1):
        temp = a%h 
        if (temp == 0): 
          return h 
        a = h 
        h = temp 
   
p = 3 
q = 7 
  
n = p*q 

# Finding second part of publickey. 
e = 2
pq = (p-1)*(q-1)

while (e < pq):
    
    # e must be co-prime to pq and smaller than pq. 
    
    if (gcd(e, pq)==1):
        break
    else:
        e=e+1

# d*e = 1 + k * quotient 

k = 2; #constant

d = (1 + (k*pq))/e 
 
msg = 10

print("Message =", msg) 

#  c = (msg ^ e) % n 

c = pow(msg, e)
c = math.fmod(c, n) 
print("\nEncrypted data =", c) 

#  m = (c ^ d) % n 

m = pow(c, d) 
m = math.fmod(m, n)
print("\nDecrypted Message =", m)
 