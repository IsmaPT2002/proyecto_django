# Complejo Deportivo de Vigo

Bienvenido al proyecto de Django en Python para el complejo deportivo de Vigo. Este sitio web te permitirá conocer nuestras instalaciones, precios y horarios, y contactar con nuestro equipo.

## Requisitos

Este proyecto ha sido desarrollado con Python 3.8 y Django 3.2. Para instalar las dependencias adicionales necesarias, por favor revisa el archivo `requirements.txt`.

## Instalación

Para ejecutar este proyecto en tu máquina local, sigue estos sencillos pasos:

1. Clona este repositorio en tu máquina local: `git clone https://github.com/IsmaPT2002/proyecto_django.git`
2. Crea un entorno virtual de Python: `python3 -m venv nombre_entorno`
3. Activa el entorno virtual: `source nombre_entorno/bin/activate`
4. Instala las dependencias del proyecto: `pip install -r requirements.txt`
5. Ejecuta las migraciones de Django: `python manage.py migrate`
6. Carga los datos iniciales en la base de datos: `python manage.py loaddata initial_data.json`
7. Ejecuta el servidor de desarrollo: `python manage.py runserver`

## Características

### Alta y Baja de Clientes

En nuestra página web, los administradores podrán dar de alta y baja a los clientes, permitiendo un mayor control y seguimiento de nuestra base de datos de clientes.

### Instalaciones

En nuestro complejo deportivo, ofrecemos diversas instalaciones deportivas, como polideportivo, piscinas, hipódromo y más. En la página web, podrás ver la lista completa de nuestras instalaciones y horarios de disponibilidad.

### Precios

En nuestro complejo deportivo, ofrecemos una gran variedad de tarifas y precios, dependiendo del tipo de instalación, la edad del usuario y la duración de la reserva. En la página web, podrás encontrar toda la información necesaria sobre nuestros precios y descuentos.

### Contacto

¿Tienes alguna pregunta o sugerencia? ¡No dudes en contactar con nosotros! En nuestra página web, podrás encontrar un formulario de contacto donde podrás enviarnos tus comentarios o preguntas.

## Contribución

Si deseas contribuir al proyecto, por favor sigue los siguientes pasos:

1. Crea un fork del repositorio en tu cuenta de GitHub.
2. Crea una nueva rama para tu contribución: `git checkout -b mi_contribucion`
3. Realiza tus cambios y haz commit de los mismos: `git commit -am "Añadido mi contribución"`
4. Realiza un push de los cambios a tu repositorio en GitHub: `git push origin mi_contribucion`
5. Crea un pull request desde tu rama de contribución a la rama `main` del repositorio original.

## Licencia

Este proyecto se distribuye bajo la licencia MIT. Ver el archivo LICENSE para más detalles
