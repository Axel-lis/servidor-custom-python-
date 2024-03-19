import os

# Rutas a los archivos de configuración. Modifica esto según tu sistema.
VHOSTS_PATH = 'C:/xampp/apache/conf/extra/httpd-vhosts.conf'
HOSTS_PATH = 'C:/Windows/System32/drivers/etc/hosts'

# Plantilla para la configuración de VirtualHost
VHOST_CONFIG = """
<VirtualHost *:80>
    ServerAdmin webmaster@{server_name}
    DocumentRoot "C:/xampp/htdocs/{doc_root}"
    ServerName {server_name}
    ErrorLog "logs/{server_name}-error.log"
    CustomLog "logs/{server_name}-access.log" common
</VirtualHost>
"""

def add_virtual_host(server_name, doc_root):
    # Asegurando que los nombres de archivo y rutas son seguros
    server_name = server_name.replace(' ', '_')
    doc_root = doc_root.replace(' ', '_')

    # Añadir la configuración a httpd-vhosts.conf
    with open(VHOSTS_PATH, 'a') as vhosts_file:
        vhosts_file.write(VHOST_CONFIG.format(server_name=server_name, doc_root=doc_root))

    # Añadir entrada al archivo de hosts
    with open(HOSTS_PATH, 'a') as hosts_file:
        hosts_file.write(f"\n127.0.0.1    {server_name}\n")

    print(f"El sitio {server_name} ha sido añadido a VirtualHosts y al archivo de hosts.")

def main():
    print("Configurador de nuevos sitios en XAMPP")
    server_name = input("Introduce el nombre del servidor (ejemplo: misitio.local): ")
    doc_root = input("Introduce el nombre de la carpeta del sitio en htdocs (ejemplo: misitio): ")

    add_virtual_host(server_name, doc_root)

    print("Recuerda reiniciar Apache para aplicar los cambios.")

if __name__ == "__main__":
    # Se requiere permiso de administrador para ejecutar este script
    if os.name == 'nt' and not os.access(VHOSTS_PATH, os.W_OK):
        print("Por favor, ejecuta este script como administrador.")
    else:
        main()
