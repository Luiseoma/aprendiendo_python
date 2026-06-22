with open ("Curso dalto/archivos/hola_como_estas.txt", "w", encoding="UTF-8") as archivo:
    #Sobreescribiendo el archivo
    #archivo.write("Que bueno")
    
    archivo.writelines(["Hola como estás?\n", "bien y tu?\n"])
    archivo.writelines(["Bien también, gracias\n", "Que bueno"])