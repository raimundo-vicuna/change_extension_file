import os

carpeta = ""
extension = ""
for nombre_archivo in os.listdir(carpeta):
    ruta_completa = os.path.join(carpeta, nombre_archivo)
    
    if os.path.isfile(ruta_completa):
        nombre_sin_ext = os.path.splitext(nombre_archivo)[0]
        
        nuevo_nombre = nombre_sin_ext + extension
        nueva_ruta = os.path.join(carpeta, nuevo_nombre)

        os.rename(ruta_completa, nueva_ruta)
        print(f"Renombrado: {nombre_archivo} → {nuevo_nombre}")
