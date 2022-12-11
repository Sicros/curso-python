def bienvenida_usuario(nombre):
    print("Hola ! Te doy la bienvenida a este pequeño curso, " + nombre + " !")

def bienvenida_personalizada(nombre, momento=""):
    if momento == "mañana":
        print("Buenos días ! Te doy la bienvenida a este pequeño curso, " + nombre + " !")
    elif momento == "tarde":
        print("Buenas tardes ! Te doy la bienvenida a este pequeño curso, " + nombre + " !")
    elif momento == "noche":
        print("Buenas noches ! Te doy la bienvenida a este pequeño curso, " + nombre + " !")
    else:
        print("Hola ! Te doy la bienvenida a este pequeño curso, " + nombre + " !")
    
def suma_y_division(a, b, c):
    resultado = a + b
    resultado = resultado / c
    return resultado
    print("Jamás verás este mensaje, muajajaja!!")

def bienvenida_muchos_usuarios(nombres):
    i = 0
    while i < len(nombres):
        print("Hola ! Te doy la bienvenida a este pequeño curso, " + nombres[i] + " !")
        i = i + 1

def bienvenida_muchos_usuarios_interna(nombres):
    i = 0
    while i < len(nombres):
        bienvenida_usuario(nombres[i])
        i = i + 1