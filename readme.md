
* En /Status.html las cantidades en € solo se dan con 2 decimales (céntimos reales), por ser más legible. No interfiere con las operaciones reales al ser solo esta página de lectura y no guardarse el redondeo en la base de datos.

* En /index.html se redondea a 8 decimales (en la base de datos no se redondea, el valor se deja tal cual entra de coinapi.io). La "Cantidad venta" (único input númerico para el usuario) se deja tal cual la introducida por el usuario.

* Consume muchas llamadas a coinapi.io para efectuar el cálculo en tiempo real del valor actual de la cartera de criptomonedas: Si hacen falta más api_key's pedírselas a Cristian, tiene 4. 