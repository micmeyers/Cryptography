#Cryptography


p = int(input('Please provide a prime number for your key'))
q = int(input('Please provide another prime number for your key'))
#p and q must be prime 
n = p*q
f = (p-1)*(q-1)
list_code = []

#we need a public key for any messsages sent to be decrypted, the first number of the key is 
#p*q, the second has to be another number relatively prime to p*q

#finds the factors in n (p*q)
for i in range (2,n):
    list_code.append(i)
    
#checks if a number divisible by i 
def factors(number):
    list1=[]
    for i in range(2,number):
        if number%i==0:
            list1.append(i)
    return(list1)

#checks if the number in the list multiplied by another number is in the other list and removes it
def remove(list):
    for i in list:
        for ii in range(1,n//2):
            if i*ii in list_code:
                list_code.remove(i*ii)
                

#removes big unwated values    
def remove_big(list):
    for i in list:
        if i in list_code:
            list_code.remove(i)

def decrypt(en):
    i=1
    while i>0:
        formula=(1+f*i)%en
        dec = int(1+f*i)/en
        if formula ==0:
            return(dec)
        i+=i
def encrypt(value):
    cipher=(value**en)%n
    return(cipher)

   
list_n=factors(n)
list_f=factors(f)

remove(list_n)
remove(list_f)

list_big=[]

#checking for i's bigger than f's

for i in list_code:
    if i>f:
        list_big.append(i)
        
remove_big(list_big)
        
    
en= list_code[0]
decryption_key=decrypt(en)
print('Pubic key is:',en, ',',n)


value = ord(input ('enter a letter to encrypt:'))
encrypted_message=encrypt(value)
print('The encrypted message is:',encrypted_message)