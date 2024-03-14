#frecuencia de una onda en hz y como salida arroje en que parte del espectro electromagnético se encuentra.
hz: int
hz = int(input("Ingrese la frecuencia de la onda en hz (hertz): "))
if hz > 30e+18:
  print("La onda pertenece a la región de rayos gamma")
elif hz > 30e+15:
  print("La onda pertenece a la región de rayos X")
elif hz > 1.5e+15:
  print("La onda es del ultravioleta extremo")
elif hz > 7.89e+14:
  print("La onda es del ultravioleta cercano")
elif hz > 384e+12:
  print("La onda es del espectro visible")
elif hz > 120e+12:
  print("La onda es del infrarrojo cercano")
elif hz > 6e+12:
  print("La onda es del infrarrojo medio")
elif hz > 300e+9:
  print("La onda es del infrarrojo lejano")
elif hz > 3e+8:
  print("La onda es una microonda")
elif hz > 300e+6:
  print("La onda es de Ultra Alta Frecuencia")
elif hz > 30e+6:
  print("La onda es de muy alta frecuencia y de radio")
elif hz > 1.7e+6:
  print("La onda es corta y de radio")
elif hz > 650e+3:
  print("La onda es media y de radio")
elif hz > 30e+3:
    print("La onda es larga y de radio")
else:
    print("La onda es de muy baja frecuencia")