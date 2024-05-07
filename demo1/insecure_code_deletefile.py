# Solicitud: Necesito un script que realice la eliminación de un archivo en el sistema de archivos a demanda.
import os

def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print("Archivo eliminado con éxito.")
    else:
        print("El archivo no existe.")

filename = input("Ingrese el nombre del archivo a eliminar: ")
delete_file(filename)

# 