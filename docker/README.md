# Docker para Data WareHouse
___
> probamos la utilización de docker para crear un data warehouse



## Pasos a seguir
___
1. Instalar docker en tú compu si todavia no lo tenés.
   - [docker](https://www.docker.com/) - si no sabes como instalarlo aquí esta la documentación oficial.
2. Levantar el contenedor.
```dockerfile
docker-compose up -d
```
3. Usa tú cliente de SQL favorito, en mi caso es DBeaver, y sigue estos pasos.
   - presiona **New Database Connection**
   - Port: 3307
   - Username: root 
   - Password: *Escribe la contraseña de tú root*
   - presiona **Test Connection**
   - presiona **Finally** y Listo!
