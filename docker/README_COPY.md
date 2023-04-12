# Docker para Data WareHouse
___
> probamos la utilización de docker para crear un data warehouse



## Pasos a seguir
___
1. Instalar docker en tú compu
2. Descarga de la imagen de MariaDB
```docker
docker pull mariadb
```
3. Creamos un contenedor
```dockerfile
docker run --name job -e MYSQL_ROOT_PASSWORD=mi_contraseña -d mariadb
```
4. Averiguamos el puerto donde esta corriendo el contenedor de mariadb
```dockerfile
docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' job
```
Este comando nos retornará el puerto donde está corriendo el contenedor de Docker.
5. Conectamos a la Base de Datos desde DBeaver o cualquier otro cliente de SQL
    - Port: 3306
    - Username: root (usuario por defecto de MariaDB)
    - Password: la contraseña utiliza para el usuario
    - Test Connection. realizamos la prueba de conexión.
    - Listo!
