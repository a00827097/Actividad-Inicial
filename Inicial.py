#A00827097 Emma Gomez Guerra
#A01633320 José Diego S. Larragoiti
#proposito del programa
import math

#funcion1  calcular área del rectángulo
def area_rectangulo(l1,l2):
    area = l1*l2
    return print('area del rectangulo es: ', area)

#funcion2  calcular perímetro del rectángulo
def perimetro_rectangulo(l1,l2):
    perimetro = l1*2 + l2*2
    return print('el perimetro es: ', perimetro)


#instrucciones de accion
#pedir datos
print("medida de un lado del rectángulo")
l1 = float(input())

print("medida de un lado del rectángulo")
l2 = float(input())

#desplegar calculo funcion1
area = area_rectangulo(l1,l2)
print(l1, "*", l2, "=", area)



#desplegar calculo funcion 2
perimetro = perimetro_rectangulo(l1,l2)
print(l1, "*2 +", l2, "*2 =", perimetro)


