with open ("Curso dalto/archivos/hola_como_estas.txt", "a", encoding="UTF-8") as archivo:
    #usando un bucle para agregar varias lineas
    archivo.write("\n")
    for i in range(5):
        archivo.write(f"linea{i+1} agregada\n")
