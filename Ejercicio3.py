# Program 3
"""
You have a bicycle lock. The locking mechanism consists of several dials. 
Each dial contains the digits 0-9 in a cycle, in this order. From each dial 
exactly one digit is visible.
Each dial can be rotated in either direction:
    Rotating the dial one step in the positive direction (denoted '+') 
    increments the digit shown.

E.g., if the dial currently shows 4 and you make the '+' rotation, the dial 
will now show 5. After the digit 9 comes the digit 0 again.
    Rotating the dial one step in the negative direction (denoted '-') does the
    opposite.

E.g., the '-' rotation will change a dial showing 5 into a dial showing 4, and 
it will change a dial showing 0 into a dial showing 9.
Your finger is currently on the leftmost dial. You can use it to rotate the 
dial it's on. You can also move your finger one dial to the right (denoted '>')
or one dial to the left (denoted '<'). You can only move your finger if the 
destination dial actually exists.
You are given the int[] dials. The elements of dials are the digits currently 
shown on the dials of your lock, from the left to the right.
You would like to scramble your lock into a state where all of the digits shown
on the dials are mutually distinct. Find any sequence of at most 100 actions 
that accomplishes this goal, and return it as a String[].

Class:	BicycleLock
Method:	makeDistinct
Parameters:	int[]
Returns:	String
Method signature:	String makeDistinct(int[] dials)
(be sure your method is public)

You are not required to minimize the number of operations.

dials will contain between 1 and 10 elements, inclusive.
Each element of dials will be between 0 and 9, inclusive.

EXAMPLES:

Input: {3, 2, 7}
Output: ""
All dials already show distinct numbers, so we do not have to do anything at 
all.

Input: {8, 8, 0, 9}
Output: ">+++"
Our solution moves the finger to the second dial and then rotates it three 
times in the positive direction. This changes the lock from its initial state 
8809 into 8909, then 8009, and finally 8109, which is a valid final state.
There are many other valid solutions. The most efficient one is to simply 
rotate the first dial once in the negative direction, changing the lock to 7809.

Input:{9}
Output: "+++--+-"
Again, we do not have to do anything, but we can. Remember that any solution 
that consists of at most 100 actions will be accepted.

Input: {0, 1, 0, 2, 0}
Output: ">>>>-<+<+++++"
The returned solution produces the dial values {0, 1, 5, 3, 9} in the end.

"""
class BicycleLock:
    
    def __init__(self, dials):
        self.dials = dials
    
     # metodo muestra indices de elementos repetidos
    @classmethod
    def repetidos(cls, lista):
        indices = [i for i, _ in enumerate(lista) if lista.count(_)>1]
        return  indices
    
    # Funcion para buscar elemento en lista y diferencia 
    @classmethod
    def busqueda(cls,elemento, lista):
        bol = False
        nes = 0
        for i,j in enumerate(lista):
            if elemento == 0:
                continue
            else:
                if elemento == j:
                    nes = lista[i] - lista[i-1]
                    bol = True
                    break
                else:
                    continue
        return bol, nes
    
    #metodo principal
    def makeDistinct(self, dials):
        ctotal = ""
        if len(dials)<2:
            print("\" \"")
        else:
            indices = BicycleLock.repetidos(dials)
            i = 0
            for i,elemento in enumerate(dials):
                if BicycleLock.busqueda(i, indices)[0]:
                    for j in range(BicycleLock.busqueda(i, indices)[1]):
                        ctotal += ">"
                    n=elemento
                    while True:
                        if n not in dials:
                            dials[i] = n
                            break
                        else:
                            if n == 9:
                                n = 0
                                ctotal += "+"
                            n += 1
                            ctotal += "+"
        print(ctotal)
    

NM= input('ingrese 2 numero separados por espacio: ')
NM= list(map(int, NM.split()))

primer=BicycleLock(NM)
primer.makeDistinct(NM)