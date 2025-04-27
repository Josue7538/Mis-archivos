import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def abrir_calculadora():
    calc_ventana = tk.Toplevel(ventana)
    calc_ventana.title("Calculadora")
    calc_ventana.geometry("300x400")
    
    entrada = tk.Entry(calc_ventana, font=("Arial", 20), justify="right")
    entrada.pack(fill="both")
    
    def click_boton(valor):
        entrada.insert(tk.END, valor)
    
    def limpiar():
        entrada.delete(0, tk.END)
    
    def calcular():
        try:
            resultado = eval(entrada.get())
            entrada.delete(0, tk.END)
            entrada.insert(tk.END, resultado)
        except:
            entrada.delete(0, tk.END)
            entrada.insert(tk.END, "Error")
    
    botones = [
        ("7", "8", "9", "/"),
        ("4", "5", "6", "*"),
        ("1", "2", "3", "-"),
        ("C", "0", "=", "+")
    ]
    
    for fila in botones:
        frame = tk.Frame(calc_ventana)
        frame.pack(fill="both", expand=True)
        for btn in fila:
            boton = tk.Button(frame, text=btn, font=("Arial", 15), height=2, width=5,
                              command=lambda b=btn: click_boton(b) if b not in ["=", "C"] else calcular() if b == "=" else limpiar())
            boton.pack(side="left", fill="both", expand=True)

def abrir_calculo_area():
    area_ventana = tk.Toplevel(ventana)
    area_ventana.title("Calcular Área")
    area_ventana.geometry("300x300")
    
    def calcular_area(figura):
        area_ventana.withdraw()
        datos_ventana = tk.Toplevel(ventana)
        datos_ventana.title(f"Área de {figura}")
        
        tk.Label(datos_ventana, text=f"Ingresa los valores para el {figura}").pack()
        valores = []
        
        if figura == "Cuadrado":
            tk.Label(datos_ventana, text="Lado:").pack()
            lado = tk.Entry(datos_ventana)
            lado.pack()
            valores.append(lado)
        elif figura in ["Rectángulo", "Triángulo"]:
            tk.Label(datos_ventana, text="Base:").pack()
            base = tk.Entry(datos_ventana)
            base.pack()
            valores.append(base)
            
            tk.Label(datos_ventana, text="Altura:").pack()
            altura = tk.Entry(datos_ventana)
            altura.pack()
            valores.append(altura)
        
        def mostrar_resultado():
            try:
                if figura == "Cuadrado":
                    resultado = float(valores[0].get()) ** 2
                elif figura == "Rectángulo":
                    resultado = float(valores[0].get()) * float(valores[1].get())
                elif figura == "Triángulo":
                    resultado = 0.5 * float(valores[0].get()) * float(valores[1].get())
                messagebox.showinfo("Resultado", f"El área del {figura} es {resultado}")
            except:
                messagebox.showerror("Error", "Ingresa valores válidos")
        
        tk.Button(datos_ventana, text="Calcular", command=mostrar_resultado).pack()
    
    figuras = ["Cuadrado", "Rectángulo", "Triángulo"]
    for figura in figuras:
        tk.Button(area_ventana, text=figura, command=lambda f=figura: calcular_area(f)).pack()

def abrir_guia_python():
    guia_ventana = tk.Toplevel(ventana)
    guia_ventana.title("Guía de Python")
    guia_ventana.geometry("600x600")
    
    texto = """
    🐍 Guía Completa de Python
    
    1️⃣ Introducción a Python
    2️⃣ Sintaxis Básica
    3️⃣ Estructuras de Control
    4️⃣ Funciones
    5️⃣ Listas y Diccionarios
    6️⃣ Programación Orientada a Objetos
    7️⃣ Módulos y Librerías
    8️⃣ Desarrollo Web y Ciencia de Datos
    """
    
    label = tk.Label(guia_ventana, text=texto, justify="left", wraplength=580)
    label.pack(padx=10, pady=10)
    
    imagenes = ["python_sintaxis.png", "estructuras_control.png", "poo_diagrama.png"]
    for img_path in imagenes:
        try:
            img = Image.open(img_path)
            img = img.resize((500, 300), Image.ANTIALIAS)
            img_tk = ImageTk.PhotoImage(img)
            img_label = tk.Label(guia_ventana, image=img_tk)
            img_label.image = img_tk
            img_label.pack(pady=5)
        except:
            print(f"No se pudo cargar la imagen {img_path}")

# Ventana principal
ventana = tk.Tk()
ventana.title("Menú Principal")
ventana.geometry("300x200")

# Botones principales
tk.Button(ventana, text="Calculadora", command=abrir_calculadora).pack(fill="both")
tk.Button(ventana, text="Calcular Área", command=abrir_calculo_area).pack(fill="both")
tk.Button(ventana, text="Guía de Python", command=abrir_guia_python).pack(fill="both")

ventana.mainloop()
