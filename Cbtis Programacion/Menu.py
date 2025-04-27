def area_figura():
    figuras = {
        "triangulo": ["base", "altura"],
        "cuadrado": ["lado"],
        "rectangulo": ["base", "altura"]
    }
    
    figura = input("Elige una figura (triangulo, cuadrado, rectangulo): ").strip().lower()
    
    if figura in figuras:
        datos = [float(input(f"Ingrese {dato}: ")) for dato in figuras[figura]]
        
        if figura == "triangulo":
            print(f"El area del triangulo es: {0.5 * datos[0] * datos[1]}")
        elif figura == "cuadrado":
            print(f"El area del cuadrado es: {datos[0] ** 2}")
        elif figura == "rectangulo":
            print(f"El area del rectangulo es: {datos[0] * datos[1]}")        
        
    else:
        print("Figura no válida.")

def operacion_matematica():
    operaciones = {
        "suma": lambda a, b: a + b,
        "resta": lambda a, b: a - b,
        "multiplicacion": lambda a, b: a * b,
        "division": lambda a, b: a / b if b != 0 else "No se puede dividir entre cero"
    }

    operacion = input("Elige una operación (suma, resta, multiplicacion, division): ").strip().lower()
    
    if operacion in operaciones:
        a, b = float(input("Número 1: ")), float(input("Número 2: "))
        print(f"El resultado de la {operacion} es: {operaciones[operacion](a, b)}")
    else:
        print("Operación no válida.")

while True:
    eleccion = input("\n¿Quieres calcular un área o realizar una operación? (area/operacion): ").strip().lower()
    eleccion = eleccion.replace("á", "a").replace("ó", "o")  

    if eleccion == "area":
        area_figura()
    elif eleccion == "operacion":
        operacion_matematica()
    else:
        print("Opción no válida.")

    continuar = input("\n¿Quieres continuar? (Si/No): ").strip().lower()
    if continuar != "si":
        print("Programa finalizado.")
        break
