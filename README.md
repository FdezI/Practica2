Practica2:Aislamiento de una aplicación web usando jaulas
===========================

Crear una mini-aplicación web (un hola mundo o un simple formulario) y aislarlo en una jaula chroot.

Para la realización de la práctica descrita correremos sobre un sistema Debian Sid "chrooteado" una aplicación web muy básica
haciendo uso del framework de Python: WebPy, por lo que será necesario instalar en el sistema Debian dicho framework y todas
sus dependencias. La máquina anfitriona se encuentra bajo un sistema Ubuntu 12.04.


## Instalación del sistema

El primer paso será crear el directorio que contendrá nuestro sistema debian:

```
# mkdir -p /home/chroots/sid
# debootstrap sid /home/chroots/sid http://ftp.es.debian.org/debian/
```
Para agilizar el procedimiento es recomendable seleccionar un mirror cercano, en este caso uno español (es).

De esta forma ya tendremos un sistema para hacer "chroot", aunque con algunas limitaciones que darán error posteriormente.
Por ello, para evitar algunos errores deberemos montar el sistema de directorios básico del sistema a usar:

Directorio de procesos:
```
# mount --bind /proc /home/chroots/sid/proc
```

Si deseáramos utilizar algún dispositivo adicional, así como dispositivos de almacenamiento externo, deberíamos también
montar el directorio de dispositivo:

```
# mount --bind /dev /home/chroots/sid/dev
```

De esta forma pasaría lo mismo con cualquier directorio del sistema anfitrión del que quisiéramos disponer en el sistema
chroot.

En este caso nos bastará con el de procesos.


## Instalación de las dependencias de la aplicación

Antes de proceder a la instalación de la aplicación y una vez lista la jaula el siguiente paso es entrar en ella:
```
# chroot /home/chroots/sid
```

Para comprobar que realmente estamos en la jaula podemos comprobar que el directorio /home no contiene la carpeta de
jaulas "chroots":
```
# ls /home
```

Bien, comprobado que estamos correctamente "chrooteados" procedemos a instalar las dependencias de la aplicación,
haciendo uso de la inmensa comodidad del apt-get, que aunque tiene sus desventajas frente a una compilación/instalación
manual, nos facilita mucho la labor:
```
# apt-get install python-webpy
```

Con esto deberíamos tener todo listo para arrancar la aplicación web sin problemas.

## Ejecutando la aplicación desde el chroot

Al estar la aplicación fuera del sistema debian deberemos copiarla a éste. Para ello, desde fuera del chroot copiamos la aplicación a algún directorio
de dentro de nuestro sistema (visible por él):
```
# cp /home/<username>/aplicacion.d /home/chroots/sid/var/www/aplicacion.d
```

Probamos a ejecutar la aplicación desde el chroot:
```
# chroot /home/chroots/sid
# python /var/www/aplication.d/app.py
```

Probamos que efectivamente, se puede acceder a la aplicación ejecutada dentro del chroot desde fuera, para ello, desde
un navegador:

```
http://localhost:8080
```

WebPy por defecto usa el puerto 8080 para servir el contenido web de nuestro sitio.


![image](http://imageshack.com/i/0jfzuwp)
