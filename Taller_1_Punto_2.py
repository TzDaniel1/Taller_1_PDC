primer_num=float(input("Ingrese el primer numero (real)"))
segundo_num=float(input("Ingrese el segundo numero (real)"))
tercer_num=float(input("Ingrese el tercer numero (real)"))


if primer_num!=segundo_num and primer_num!=tercer_num and tercer_num!=segundo_num:
    if primer_num>segundo_num and primer_num>tercer_num: #Se evalua el primer numero vs los otros dos
        print ("El primer "+str(primer_num)+" numero es mayor")
    elif segundo_num>primer_num and segundo_num>tercer_num: #Se evalua el segundo numero vs los otros dos
        print ("El segundo "+str(segundo_num)+" numero es mayor")
    else: #Si ambas funciones evaluadas no dan, por consiguiente el tercero debe ser el mayor
        print ("El tercer "+str(tercer_num)+" numero es mayor")
elif primer_num==segundo_num :
    if primer_num>tercer_num: #Se evalua el primer numero vs el tercero sabiendo que 1 y 2 son iguales
        print ("El primero y segundo "+str(primer_num)+"  son los mayores que el tercero")
    else:  #Se sabria que el tercero es el mayor
        print ("El tercer "+str(tercer_num)+"  numero es el mayor")
elif primer_num==tercer_num:  
    if primer_num>segundo_num: #Se evalua el primer numero vs el segund sabiendo que 1 y 3 son iguales
        print ("El primer y tercer "+str(tercer_num)+"  numero son mayores")
    else:  #Se sabria que el tercero es el mayor
        print ("El segundo "+str(segundo_num)+"  numero es el mayor")
elif segundo_num==tercer_num:  
    if segundo_num>primer_num: #Se evalua el segundo numero vs el primer sabiendo que 2 y 3 son iguales
     print ("El segundo y tercer "+str(segundo_num)+"  numero son mayores")
    else:  #Se sabria que el tercero es el mayor
        print ("El primer "+str(primer_num)+"  numero es el mayor")