#programa que solicite al usuario una letra y determine si es una vocal o una consonante.
letra_eval: int
letra_eval = (input("Ingrese letra :"))
n=letra_eval
if ord(n)== 97 or ord(n)==101 or ord(n)==105 or ord(n)==111 or ord(n)==117:
    print("Es vocal")
else:
    print("Es consonante")