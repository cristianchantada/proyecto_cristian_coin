# Proyecto de Cristian Varela Casas del Bootcamp Cero XII con Flask Classic.

### Siga los pasos aquí indicados para realizar la instalación de la aplicación:

1. Instale las librerías necesarias de Python en su **entorno virtual** mediante el comando en consola *pip install -r requirements.txt*.
2. Renombre los archivos *.env_template* y *config_template.py* a .env y config.py respectivamente. A continuación entre en cada uno de ellos y siga las instrucciones ahí indicadas.
3. En la carpeta **/data** existe el archivo *create.db*, de ayuda para la creación de la base de datos de esta aplicación. Con la sintaxis de SQL ahí contenida, cree su base de datos en esta misma carpeta.

### Notas varias:

* Aplicación diseñada en 1920x1080 px; espero que si se ejecuta en otras resoluciones de pantalla siga quedando todo bien alineadito (en varias pruebas ha sido correcto).

* En */Status.html* las cantidades en € solo se dan con 2 decimales (céntimos reales), por ser más legible. No interfiere con las operaciones reales al ser esta página solamente de lectura. Este redondeo no se guarda en la base de datos.

* En */index.html* se redondea a 8 decimales (en la base de datos no se redondea, el valor se deja tal cual entra de coinapi.io). La *"Cantidad venta"* (único input númerico para el usuario) se deja tal cual la introducida por el usuario sin redondeo para que pueda vender exactamene lo que deseeo o bien todo lo que tenga de esa cripto en concreto.

* Si se necesitan más apikey por haber consumido las 100 llamadas diarias, pídasela a Cristian Varela, posee 4 (cristianchantada@gmail.com)

* EL desarrollador del presente proyecto tuvo un cacao mental al regresar commits atrás con *git reset --hard HEAD~1* para deshacer el primer intento infructuoso de crear la class EnterInDataBase. A partir de ahí bifurcó la rama varias veces sin haberse percatado de en cúal de ellas estaba, fue para atrás y hacia adelante por no encontrar el último commit actualizado y no dejarle hacer push. Cuando se recuperó y ordenó el proyecto de nuevo, creo la rama *"hacia_entrega"*. Es el último commit de esta rama con el que corregir el proyecto.

* Si tiene cualquier duda de funcionamiento póngase en contacto con el desarrollador mediante el email facilitado anteriormente.