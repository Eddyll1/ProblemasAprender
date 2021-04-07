# Program 2
"""
A string is called a palindrome if it reads the same forwards and backwards. 
E.g., "a", "noon" and "tacocat" are palindromes but "cocoa" isn't.
A string is called a near-palindrome if we can rearrange its characters to make
it a palindrome. For example, "aaa", "cocoa" and "xxyyzz" are near-palindromes 
but "abc" isn't.

Class:      NearPalindromesDiv1
Method:     Solve
Parameters: String
Returns:	Int

Contrains:
S will contain between 1 and 2,500 characters, inclusive.
Each character of S will be a lowercase English letter ('a'-'z').

Examples:

input: "cocoa"
output: 0
This is already a near-palindrome, no operations are needed.

input: "daddy"
output: 2
One optimal solution is to increment S[4] twice, changing the input string into 
the near-palindrome "dadda".
(The string "dadda" is a near-palindrome because we can rearrange its letters 
to get a palindrome. One of the palindromes we can obtain this way is "dadad".)

input: "abcdefgh"
output: 4

"""

class NearPalindromesDiv1:
  
  def __init__(self, S):
    self.S = S
  
  #Metodo para contras letras que no estan repetidas
  @classmethod
  def contarletras(cls, cadena):
    nl = [] #numero de apariciones de cada letra
    cAux = cadena #acadena auxiliar
    let = [] #letra no esta repetida
    for letra in cadena:
      if letra not in  let:
        nl.append(cAux.count(letra))
        let.append(letra)
      else:
        continue
    dicl = dict(zip(let,nl)) #diccionario de letras
    return dicl
  
  #Metodo para buscar numero de letras impares en la palabra
  @classmethod
  def buscarimpares(cls, vnl):
    ili = [] #indice de letras impares
    for i in vnl:
      if vnl[i]%2 == 0:
        continue
      else:
        ili.append(i)
    return ili

    #Metodo para hallar el menor camino entre dos letras
  @classmethod
  def menorcamino(cls, l1, l2):
  #l1 y l2 son entradas de la funcion de ellas se vera el menor camino
  #l1 siempre sera mayor en camino normal
    array = []
    cam1 = l1-l2 #camino 1
    if cam1 < 0: #l2>l1
      n1 = 122-l2
      n2 = l1-97
      cam1 = n1+n2+1
      cam2 = l2-l1
    else: #l1>l2
      n1 = 122-l1
      n2 = l2-9
      cam2 = l2+l1+1
        
    if cam1 < cam2:
      return cam1
    else:
      return cam2
  
  #Metodo buscar menor camino entre letras de la cadena
  @classmethod
  def entreletras(cls, vl):
  #vl: Vector de letras sin pareja
    contadorpasos=0 # contador final
    lvl = len(vl) # longitud inicial 
    i = 0
    j = 0
    vlaux = [] # auxiliar
    while i < (lvl//2):
      vlaux.append(vl[j])
      vl.remove(vl[j])
      vmin=[] #vector de valores minimos
      for k in vl:
        menor = NearPalindromesDiv1.menorcamino(ord(vlaux[i]),ord(k)) #Salto menor
        vmin.append(menor)

      contadorpasos += min(vmin)
      indice = vmin.index(min(vmin))
      vl.pop(indice)
      i += 1
    return contadorpasos

  # Metodo principal
  def  solve(self, S):
    lS = len(S) # longitud de cadena
    dicc = NearPalindromesDiv1.contarletras(S) #diccionario de letras
    dico = sorted(dicc) #diccionario ordenado
    vi = NearPalindromesDiv1.buscarimpares(dicc)
    vi.sort()

    if lS<2:
      print(0) #Retorna cero por que de ley es palindromo

    else:
      if lS%2 == 0: #numero de letras par
      
        if len(vi) == 0:
          print(0) # retorna cero por que es casi palindromo              
        elif len(vi) > 0:
          ##proceder con algoritmo de conversion
          print(NearPalindromesDiv1.entreletras(vi))

      elif lS%2 == 1: #numero de letras impar
        if len(vi) > 1:
          ##proceder con algoritmo de conversion
          print(NearPalindromesDiv1.entreletras(vi))
        elif len(vi) == 1:
          print(0) # retorna cero por que es casi palindromo

S=list(input("Enter a lowercase word: "))
palabra=NearPalindromesDiv1(S)
palabra.solve(S)