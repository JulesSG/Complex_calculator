import math

def rectangular(polar):
    rect = [polar[0]*math.cos(math.radians(polar[1])),polar[0]*math.sin(math.radians(polar[1]))]
    return rect
def polar(recta):
    pol = []
    pol.append(math.sqrt(pow(recta[0],2)+pow(recta[1],2)))
    angulo = 0
    if recta[0] == 0:
        if recta[1] > 0:
            angulo = math.pi/2
        elif recta[1] < 0:
            angulo = -math.pi / 2
        elif recta[1] == 0:
            angulo = 0
    else:
            angulo = math.atan(recta[1]/recta[0])
    if recta[0]<0 and recta[1]>0:
        angulo += math.pi
    elif recta[0]<0 and recta[1]<0:
        angulo -= math.pi
    pol.append(math.degrees(angulo))
    return pol
def suma(polar1,polar2):
    vec1 = rectangular(polar1)
    vec2 = rectangular(polar2)
    sumar = [vec1[0]+vec2[0],vec1[1]+vec2[1]]
    resultpolar = polar(sumar)
    return resultpolar

def multiplicar(polar1, polar2):
    modulo = polar1[0]*polar2[0]
    angulo = polar1[1]+polar2[1]
    multi = [modulo,angulo]
    return multi

def suma_3n(polar1,polar2,polar3):
    return suma(suma([polar1,polar2]),polar3)


def divicion(polar1,polar2):
    modulo = polar1[0]/polar2[0]
    angulo = polar1[1]-polar2[1]
    div = [modulo,angulo]
    return div

