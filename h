[33mcommit 9a7d9b4c3ef680db362bd70247e9a5c3d4703248[m[33m ([m[1;36mHEAD -> [m[1;32mmain[m[33m)[m
Author: Cristian Varela Casas <cristianchantada@gmail.com>
Date:   Sat Oct 22 11:44:59 2022 +0200

    Creo que la he liado al crear la class EnterInDataBase. Retrocedo un commit con git reset hard HEAD~1

[33mcommit 584fbe8b39da3e955f394bd4fa5453661f56d8b8[m[33m ([m[1;31morigin/main[m[33m)[m
Author: Cristian Varela Casas <cristianchantada@gmail.com>
Date:   Fri Oct 21 20:03:37 2022 +0200

    Se reparan bugs surgidos esta mañana y otros nuevos surgidos al arreglar estos; se sigue dando estilo y modificando estructura. Queda el color e imágenes en el estilo para darle visibilidad a la página e intentar el class EnterInBaseDate con todas las que ahora son funciones de entrada a la DB

[33mcommit 39b08f3be56c59e235be2dba81c9f0e88dd6781f[m
Author: Cristian Varela Casas <cristianchantada@gmail.com>
Date:   Fri Oct 21 12:34:40 2022 +0200

    Realizo la mayor parte de la refactorización, solo quedándome la class con métodos de conexión a la base de datos; reestructuro .html y queda arreglar tabla inferior operations.html porq ue hace que el programa casque

[33mcommit cc476ff8f296f6c7c2d68bb8205f7a6316b59403[m
Author: Cristian Varela Casas <cristianchantada@gmail.com>
Date:   Thu Oct 20 19:17:05 2022 +0200

    Desarrollo de estilo y ajustes de estructura; aún queda por hacer

[33mcommit a34144cb9c763fdb326d0dfb52859a680781c6a1[m
Author: Cristian Varela Casas <cristianchantada@gmail.com>
Date:   Thu Oct 20 11:51:11 2022 +0200

    Se acaba de gestionar los errores, se da estructura y estilo (sin rematar) y se descargan los iconos e imágenes a implementar

[33mcommit 2b4e4d1503d577c50cb975cf6e36e61bae4d74ba[m
Author: Cristian Varela Casas <cristianchantada@gmail.com>
Date:   Wed Oct 19 20:24:16 2022 +0200

    Tarde muy productiva: los <a href> ya han sido dinámicamente modificados con Jinja para que no aparezcan en su misma pestaña (/index o /purchase o /status); además se da mucha estructura y formato a los .html

[33mcommit 5914b280fe733032a88c0d0d6613a1e450512f77[m
Author: Cristian Varela Casas <cristianchantada@gmail.com>
Date:   Wed Oct 19 13:36:51 2022 +0200

    Se formatean los resultados para limitar decimales, se corrige parte de la validación en /purchase que ayer no salía, se hace la mayor parte de la gestión de errores

[33mcommit 716125860d170bac1d5bbb2b266c140ff292c9d3[m
Author: Cristian Varela Casas <cristianchantada@gmail.com>
Date:   Tue Oct 18 20:35:35 2022 +0200

    Se implementa el control de errores con flask.flash (aun sin acabar)

[33mcommit cce203e010ec1673e044990e7913f2d4b294bf49[m
Author: Cristian Varela Casas <cristianchantada@gmail.com>
Date:   Tue Oct 18 17:22:32 2022 +0200

    Se remata desarrollo sintaxis sql para la pestaña /status

[33mcommit 918b724d2074e2e80bcb2b3d0638a0a8ab35fd3f[m
Author: Cristian Varela Casas <cristianchantada@gmail.com>
Date:   Mon Oct 17 21:00:30 2022 +0200

    Consigo desarrollar en gran medida la programación en models.py de /status; sigo construyendo mañana

[33mcommit badfd4c9d0e92d2e911a165deaaf0298d266749a[m
Author: Cristian Varela Casas <cristianchantada@gmail.com>
Date:   Mon Oct 17 11:12:39 2022 +0200

    Logro de validación completa con éxito, empezando a crear my wallet

[33mcommit 55bf4234de3965ad359f23f86a0c0cc32237983d[m
Author: Cristian Varela Casas <cristianchantada@gmail.com>
Date:   Sun Oct 16 19:21:13 2022 +0200

    La validación estaba mal, arreglo algo, el quantity to hay que recalcular y creo tabla para guardar la operación calculada

[33mcommit 7a5125fbc46920f27a894f308023a2bd9c4c9355[m
Author: Cristian Varela Casas <cristianchantada@gmail.com>
Date:   Sat Oct 15 13:20:02 2022 +0200

    He conseguido progresar con el cálculo y validación desde /purchase e inicio grabar datos en sqlite a falta de traerme la fecha y la hora también del json de llegada

[33mcommit c1e28fe30af9f509cf8ffbcbb88b7b57ab9307fd[m
Author: Cristian Varela Casas <cristianchantada@gmail.com>
Date:   Fri Oct 14 20:30:29 2022 +0200

    Trabajo son demasiados resultados en uso de los dos submit en el html de operaciones

[33mcommit 282cc0e70f1e4d0d3317c359ccdc8fd197159e23[m
Author: Cristian Varela Casas <cristianchantada@gmail.com>
Date:   Fri Oct 14 11:03:22 2022 +0200

    Se ha trabajado en operations, cambiando la estructura y ahora estoy a medias de validar los datos

[33mcommit e8d21298aebd437fdc0068e8847c3ef90ad8e20f[m
Author: Cristian Varela Casas <cristianchantada@gmail.com>
Date:   Thu Oct 13 21:03:02 2022 +0200

    Introducimos cambios durante la tutoría

[33mcommit e5a68a398ece43c3cd0cf4d30ca31bb5acf98abf[m
Author: Cristian Varela Casas <cristianchantada@gmail.com>
Date:   Thu Oct 13 18:59:28 2022 +0200

    Prosigo desarrollando purchase

[33mcommit e727b7f5cd8e25d880a6dfbe2e98cfe309ec65c5[m
Author: Cristian Varela Casas <cristianchantada@gmail.com>
Date:   Thu Oct 13 12:06:39 2022 +0200

    En desarrollo de la parte python de /purchase

[33mcommit 66cc2818e92ab7f2f388a0d3e38fd468211ef095[m
Author: Cristian Varela Casas <cristianchantada@gmail.com>
Date:   Wed Oct 12 19:06:33 2022 +0200

    status.html a medias y poco más hecho

[33mcommit 9bcb50aeddf92ef78e7819c1034fff68433ef48f[m
Author: Cristian Varela Casas <cristianchantada@gmail.com>
Date:   Wed Oct 12 11:38:09 2022 +0200

    Desarrollo del forms con wtforms, del operations h

[33mcommit afaa7b779222641a606206a61909ecc9d3f6c3dd[m
Author: Cristian Varela Casas <cristianchantada@gmail.com>
Date:   Tue Oct 11 18:26:03 2022 +0200

    Tabla operations creada, desarrollo inicial index, desarrollo inicial funcion select_all en models

[33mcommit 53feb9f2652ef24d0953d640297d558d99ab9ed9[m
Author: Cristian Varela Casas <cristianchantada@gmail.com>
Date:   Tue Oct 11 13:52:59 2022 +0200

    Desarrollo base.html, introduzco css's

[33mcommit 60ef7be816cef90c660456f3c43d3609598328ad[m
Author: Cristian Varela Casas <cristianchantada@gmail.com>
Date:   Mon Oct 10 17:35:50 2022 +0200

    Commit inicial con infraestructura mínima y servidor funcionando
