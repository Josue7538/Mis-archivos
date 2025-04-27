import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def seleccionar_video():
    archivo = filedialog.askopenfilename(filetypes=[("Archivos de video", "*.mp4;*.avi;*.mov;*.mkv")])
    if archivo:
        reproducir_video(archivo)

def reproducir_video(ruta_video):
    cap = cv2.VideoCapture(ruta_video)
    
    if not cap.isOpened():
        print("Error al abrir el video")
        return
    
    ventana = tk.Toplevel()
    ventana.title("Reproductor de Video")
    
    lbl_video = tk.Label(ventana)
    lbl_video.pack()
    
    def actualizar_frame():
        ret, frame = cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)
            lbl_video.imgtk = imgtk
            lbl_video.configure(image=imgtk)
            lbl_video.after(10, actualizar_frame)
        else:
            cap.release()
            ventana.destroy()
    
    actualizar_frame()

def main():
    root = tk.Tk()
    root.title("Seleccionar Video")
    
    btn_seleccionar = tk.Button(root, text="Seleccionar Video", command=seleccionar_video)
    btn_seleccionar.pack(pady=20)
    
    root.mainloop()

if __name__ == "__main__":
    main()
