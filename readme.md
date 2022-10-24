
* En /Status.html las cantidades en € solo se dan con 2 decimales (céntimos reales), por ser más legible. No interfiere con las operaciones reales al ser solo esta página de lectura y no guardarse el redondeo en la base de datos.

* En /index.html se redondea a 8 decimales (en la base de datos no se redondea, el valor se deja tal cual entra de coinapi.io). La "Cantidad venta" (único input númerico para el usuario) se deja tal cual la introducida por el usuario.

* Consume muchas llamadas a coinapi.io para efectuar el cálculo en tiempo real del valor actual de la cartera de criptomonedas: Si hacen falta más api_key's pedírselas a Cristian, tiene 4.

* Tuve cacao mental al regresar commits atrás para deshacer la class EnterInDataBase. A partir de hay bifurque la rama varias veces, fui para atrás y hacia adelante por no encontrar el último commit actualizado y no dejarme hacer push. Cuando lo ordené cree la rama "hacia_entrega. Es el último commit de esta con el que corregir el proyecto.