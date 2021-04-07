# Pogram 1
'''
In this Program I print numbers from 1 to 100.
For multiples of three, print the word “Hi” instead of the number. 
For multiples of five, print the word "Bro" instead of the number. 
For numbers which are multiples of both three and five, print “Hola super amigo” 
instead of the number.
'''
for n in range(1,100):
    if (n%3 == 0) and (n%5 == 0):
        print("Hola super amigo")
    elif n%3 == 0:
        print("Hi")
    elif n%5 == 0:
        print("Bro")  
    else:
    	print(n)
        