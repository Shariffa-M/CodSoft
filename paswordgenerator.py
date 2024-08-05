import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']
print("Welcome to Password Generator !")
no_letters = int(input("How many letters do you want in your Password ?\n"))
no_numbers = int(input("How many numbers do you want in your Password ?\n"))
no_symbols = int(input("How many symbols do you want in your Password ?\n"))
password_list=[]
for i in range(1,no_letters+1):
    char = random.choice(letters)
    password_list += char

for i in range(1,no_numbers+1):
    char = random.choice(numbers)
    password_list += char
    
for i in range(1,no_symbols+1):
    char = random.choice(symbols)
    password_list += char
    
#shuffling the password list
random.shuffle(password_list)

#converting the password_list to string password
password =""
for char in password_list:
    password += char
print(password)