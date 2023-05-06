from claseConjunto import Conjunto

if __name__ == '__main__':
 A = Conjunto([1, 2, 3, 4])
 B = Conjunto([3, 6, 9])
 C = A + B
 print("Unión de A y B:", C) 
 D = A - B
 print("Diferencia de A y B:", D)
 print("A es igual a B:", A == B)
 E = Conjunto([1, 2, 3, 4])
 print("A es igual a E:", A == E)
