#Taller_1_Punto_10
distancia: float #distancia ingresada en metros
velocidadLuz: int = 300000000 #m/s
velocidadSonido: int = 344 #m/s
velocidadVehiculo: float = 141.11 #m/s
velocidadBolt: float = 12.5 #m/s
distancia = float(input('Ingrese una distancia en metros ')) #usuario ingresa valor de distancia y se hace la conversion a real
tiempoLuz: float = distancia / velocidadLuz  #calculo del tiempo a partir de la distancia y velocidad 
tiempoSonido: float = distancia / velocidadSonido
tiempoVehiculo: float = distancia / velocidadVehiculo
tiempoBolt: float = distancia / velocidadBolt

print("El tiempo que le tomaría a la luz recorrer " +str(distancia)+ " metros es de " +str(tiempoLuz)+ " segundos" )
print("El tiempo que le tomaría al sonido recorrer " +str(distancia)+ " metros es de " +str(tiempoSonido)+ " segundos" )
print("El tiempo que le tomaría al vehiculo mas veloz recorrer" +str(distancia)+ " metros es de " +str(tiempoVehiculo)+ " segundos" )
print("El tiempo que le tomaría a Usain Bolt recorrer " +str(distancia)+ " metros es de " +str(tiempoBolt)+ " segundos" )