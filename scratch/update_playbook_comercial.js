const fs = require('fs');
const path = require('path');

const mdPath = 'c:\\Users\\Lenovo\\Documents\\primavera brain\\playbook_comercial_manual_ventas.md';
const htmlPath = 'c:\\Users\\Lenovo\\Documents\\primavera brain\\playbook_comercial_manual_ventas.html';

// ----------------------------------------------------
// 1. DATA DEFINITIONS FOR EACH RECINTO
// ----------------------------------------------------

const recintos = [
  {
    id: "bloque-1",
    name: "Bloque 1: Centro de Convenciones Presidente",
    ubicacion: "Avenida Defensa Nacional #8, Col. Chamilpa, 62210 Cuernavaca, Morelos.",
    capacidad: "100 a 500 invitados.",
    estilo: "Modernista, elegante e industrial con amplias alturas y acabados de lujo.",
    fortalezas: "Gran salÃ³n climatizado, Ã¡rea infantil con juegos fijos, estacionamiento interno para 35 autos, cocina profesional gigante y baÃ±os mÃºltiples de lujo.",
    pagina: "https://primaveraeventsgroup.com/centro-de-convenciones-presidente/",
    restricciones: "Cierre de evento a las 00:00 AM (Gobernador) o 01:00 AM (Presidente).",
    packages: [
      {
        name: "Paquete Gobernador",
        estacionamiento: "Capacidad para 35 vehÃ­culos compactos en estacionamiento interno vigilado.",
        hospedaje: "No disponible en el recinto. Se cuenta con convenios especiales con hoteles de Cuernavaca (a 5-10 minutos).",
        suiteNupcial: "No disponible en el recinto. Se puede gestionar suite externa en hotel asociado con costo preferencial.",
        areaJardin: "JardÃ­n ornamental de bienvenida con fuente artificial iluminada en la entrada principal.",
        iluminacion: "IluminaciÃ³n arquitectÃ³nica bÃ¡sica en la fachada y luces decorativas en el acceso principal.",
        areaConsagrada: "No disponible dentro del recinto. Se recomienda realizar ceremonias en iglesias cercanas de Cuernavaca.",
        areaTechada: "SalÃ³n principal techado y climatizado para albergar un mÃ¡ximo de 500 personas con estilo modernista y elegante.",
        areaCocina: "Cocina profesional gigante y Ã¡rea para banquete de gran escala.",
        usoRecinto: "Uso del salÃ³n por 8 horas operativas (total 9 horas de servicio continuas de staff).",
        coctel: "Coctel de bienvenida con periqueras altas, salas lounge y sombrillas. Incluye margaritas de sabores sin alcohol (2 sabores), agua fresca (2 sabores) y cruditÃ©s (pepino, jÃ­cama y zanahoria con miguelito y chamoy).",
        montaje: "Mesa principal de honor con sillÃ³n o sillones, templete de madera y centro de mesa floral natural. Centros de mesa florales naturales (redondos/altos/bajos). Mesas redondas o cuadradas con mantelerÃ­a fina (mantel blanco, camino y servilletas de tela a elegir). Sillas Tiffany blancas. Plato base (variados modelos), loza blanca, cuberterÃ­a fina plateada y cristalerÃ­a clÃ¡sica.",
        menu: "Banquete formal a 3 tiempos:<br>â€¢ **Primer Tiempo (Entrada):** Deliciosas ensaladas frescas o cremosas sopas.<br>â€¢ **Segundo Tiempo (Plato Fuerte):** Exquisitas opciones de pollo o cerdo, acompaÃ±adas de dos guarniciones a elegir, pan y chiles al centro.<br>â€¢ **Tercer Tiempo (Tornafiesta):** Barra de esquites o chilaquiles servidos en desechables (calculado al 60% de invitados).",
        menuInfantil: "MenÃº infantil opcional disponible a solicitud ($220.00 MXN extra por niÃ±o) con tiritas de milanesa, hamburguesas o nuggets con papas y espagueti.",
        mezcladores: "Servicio completo de mezcladores: hielo en cubos ilimitado, agua natural, refrescos de la lÃ­nea Coca-Cola (sabores, mineral, clÃ¡sica), limÃ³n y sal.",
        equipo: "Coordinador General del evento, Hostess de recepciÃ³n, Meseros capacitados (1 cada 15-20 invitados), Personal de barra, Stewart de limpieza y Personal de mantenimiento de baÃ±os.",
        dj: "DJ profesional con cabina, audio de alta fidelidad, iluminaciÃ³n robÃ³tica mÃ³vil, pantalla con proyector, globos, pulseras neÃ³n y collares hawaianos (corbatas/velos en bodas), micrÃ³fonos inalÃ¡mbricos, lÃ¡ser y mÃ¡quina de humo.",
        cortesias: "DegustaciÃ³n para 4 personas al firmar. Letras decorativas gigantes 'XV' o 'LOVE', corazÃ³n rojo iluminado, mesas especiales de pastel y regalos, detonaciÃ³n de 2 chisperos, alfombra roja de entrada, espejo selfie y barra mix con 12 toppings dulces/salados.",
        duracion: "9 horas continuas totales de servicio.",
        detalles: "CoordinaciÃ³n y planeaciÃ³n integral de la logÃ­stica del evento desde la recepciÃ³n hasta el cierre.",
        calidad: "Compromiso de alta calidad de alimentos y servicio garantizado por contrato.",
        costos: "â€¢ **100 â€“ 149 personas:** $899.00 MXN por persona<br>â€¢ **150 â€“ 199 personas:** $849.00 MXN por persona<br>â€¢ **200 â€“ 299 personas:** $799.00 MXN por persona<br>â€¢ **300 â€“ 400 personas:** $749.00 MXN por persona<br>â€¢ **401+ personas:** Consultar tarifa personalizada.",
        cortesiasAdic: "DegustaciÃ³n de platillos y decoraciÃ³n bÃ¡sica del salÃ³n.",
        condiciones: "Se requiere un depÃ³sito de apartado para reservar la fecha y firma de contrato.",
        beneficios: "AtenciÃ³n personalizada de los Wedding Planners oficiales de Primavera Events Group.",
        opcionesAdic: "Montaje de ceremonia en el Ã¡rea de jardÃ­n ornamental ($3,500.00 MXN) y Barra de bebidas premium.",
        requisitos: "ConfirmaciÃ³n final de invitados (10 dÃ­as antes) y selecciÃ³n de menÃº y decoraciÃ³n.",
        notas: "Precios NO incluyen impuestos (IVA del 16% si se requiere factura). Se aplican tarifas adicionales por servicios extra o tiempo extra.",
        notaFinal: "DegustaciÃ³n exclusiva para 4 personas al firmar el contrato. DiseÃ±o de montaje de acuerdo a la paleta de colores. Croquis detallado de invitados. Minuto a minuto detallado del evento. Chat de coordinaciÃ³n exclusivo. Planner Richard HernÃ¡ndez y Gerente RubÃ­ Alvarado (Tels: 2711148997 - 7774587923)."
      },
      {
        name: "Paquete Presidente",
        estacionamiento: "Capacidad para 35 vehÃ­culos compactos en estacionamiento interno vigilado.",
        hospedaje: "No disponible en el recinto. Se cuenta con convenios especiales con hoteles de Cuernavaca (a 5-10 minutos).",
        suiteNupcial: "No disponible en el recinto. Se puede gestionar suite externa en hotel asociado con costo preferencial.",
        areaJardin: "JardÃ­n ornamental de bienvenida con fuente artificial iluminada en la entrada principal.",
        iluminacion: "IluminaciÃ³n arquitectÃ³nica bÃ¡sica en la fachada y luces decorativas en el acceso principal.",
        areaConsagrada: "No disponible dentro del recinto. Se recomienda realizar ceremonias en iglesias cercanas de Cuernavaca.",
        areaTechada: "SalÃ³n principal techado y climatizado para albergar un mÃ¡ximo de 500 personas con estilo modernista y elegante.",
        areaCocina: "Cocina profesional gigante y Ã¡rea para banquete de gran escala.",
        usoRecinto: "Uso del salÃ³n por 9 horas operativas.",
        coctel: "Coctel de bienvenida premium extendido con periqueras altas, salas lounge y sombrillas. Incluye margaritas de sabores sin alcohol (2 sabores), piÃ±adas sin alcohol, mojitos sin alcohol, agua fresca (2 sabores) y cruditÃ©s (pepino, jÃ­cama y zanahoria con miguelito y chamoy).",
        montaje: "Mesa principal de honor con sillones imperiales Rey & Reyna, templete de madera y centro de mesa floral natural. Centros de mesa florales naturales (redondos/altos/bajos). Bases de metal altas para centros de mesa. Mesas tipo mÃ¡rmol cuadradas para 10 personas o redondas para 10-12 personas con sillas Tiffany blancas. MantelerÃ­a fina (mantel blanco, camino y servilletas de tela a elegir). Plato base (variados modelos), loza blanca, cuberterÃ­a fina plateada o dorada y cristalerÃ­a fina.",
        menu: "Banquete formal a 4 tiempos:<br>â€¢ **Primer Tiempo (Entrada):** Deliciosas crepas, frescas ensaladas o cremosas sopas.<br>â€¢ **Segundo Tiempo (Plato Fuerte):** Exquisitas opciones de pollo o cerdo, acompaÃ±adas de dos guarniciones a elegir, pan y chiles al centro.<br>â€¢ **Tercer Tiempo (Postre):** SelecciÃ³n de postres de reposterÃ­a fina o de autor.<br>â€¢ **Cuarto Tiempo (Tornafiesta):** Barra de esquites o chilaquiles servidos en desechables (calculado al 60% de invitados).",
        menuInfantil: "MenÃº infantil opcional disponible a solicitud ($220.00 MXN extra por niÃ±o) con tiritas de milanesa, hamburguesas o nuggets con papas y espagueti.",
        mezcladores: "Servicio completo de mezcladores: hielo en cubos ilimitado, agua natural, refrescos de la lÃ­nea Coca-Cola (sabores, mineral, clÃ¡sica), limÃ³n y sal.",
        equipo: "Coordinador General del evento, CapitÃ¡n de Meseros, Hostess de recepciÃ³n, Meseros capacitados (1 cada 15-20 invitados), Personal de barra, Stewart de limpieza y Personal de mantenimiento de baÃ±os.",
        dj: "DJ profesional con cabina, audio de alta fidelidad, iluminaciÃ³n robÃ³tica mÃ³vil, pantalla con proyector, globos, pulseras neÃ³n y collares hawaianos (corbatas/velos en bodas), micrÃ³fonos inalÃ¡mbricos, lÃ¡ser, mÃ¡quina de humo, pista pixel de baile 5x5m y 2 chisperos a control remoto.",
        cortesias: "DegustaciÃ³n para 4 personas al firmar. Letras decorativas gigantes 'XV' o 'LOVE', corazÃ³n rojo iluminado, mesas especiales de pastel y regalos, detonaciÃ³n de 2 chisperos, alfombra roja de entrada, espejo selfie, barra mix con 12 toppings dulces/salados y opciÃ³n de montaje de ceremonia con mobiliario elegante.",
        duracion: "9 horas continuas totales de servicio.",
        detalles: "CoordinaciÃ³n y planeaciÃ³n integral de la logÃ­stica del evento desde la recepciÃ³n hasta el cierre.",
        calidad: "Compromiso de alta calidad de alimentos y servicio garantizado por contrato.",
        costos: "â€¢ **130 â€“ 149 personas:** $899.00 MXN por persona<br>â€¢ **150 â€“ 199 personas:** $849.00 MXN por persona<br>â€¢ **200 â€“ 299 personas:** $799.00 MXN por persona<br>â€¢ **300 â€“ 400 personas:** $749.00 MXN por persona<br>â€¢ **401+ personas:** Consultar tarifa personalizada.",
        cortesiasAdic: "DegustaciÃ³n de platillos y decoraciÃ³n bÃ¡sica del salÃ³n.",
        condiciones: "Se requiere un depÃ³sito de apartado para reservar la fecha y firma de contrato.",
        beneficios: "AtenciÃ³n personalizada de los Wedding Planners oficiales de Primavera Events Group.",
        opcionesAdic: "Montaje de ceremonia en el Ã¡rea de jardÃ­n ornamental (incluido en cortesÃ­a) y Barra de bebidas premium.",
        requisitos: "ConfirmaciÃ³n final de invitados (10 dÃ­as antes) y selecciÃ³n de menÃº y decoraciÃ³n.",
        notas: "Precios NO incluyen impuestos (IVA del 16% si se requiere factura). Se aplican tarifas adicionales por servicios extra o tiempo extra.",
        notaFinal: "DegustaciÃ³n exclusiva para 4 personas al firmar el contrato. DiseÃ±o de montaje de acuerdo a la paleta de colores. Croquis detallado de invitados. Minuto a minuto detallado del evento. Chat de coordinaciÃ³n exclusivo. Planner Richard HernÃ¡ndez y Gerente RubÃ­ Alvarado (Tels: 2711148997 - 7774587923)."
      }
    ]
  },
  {
    id: "bloque-2",
    name: "Bloque 2: Quinta Zarabanda",
    ubicacion: "Avenida Lauro Ortega MartÃ­nez #4, Las Animas, 62583 Temixco, Morelos.",
    capacidad: "100 a 250 personas en Ã¡rea techada.",
    estilo: "Finca campestre natural de alto confort, rodeada de abundante flora y Ã¡reas de descanso.",
    fortalezas: "Suite nupcial de lujo con jacuzzi y vestidor. Hospedaje interno climatizado para 14 personas con alberca privada y cocina. Ãrea consagrada para ceremonias. Uso completo por 10 horas sin restricciones de horario.",
    pagina: "https://primaveraeventsgroup.com/quinta-zarabanda/",
    restricciones: "Ninguna. 10 horas de servicio continuo sin restricciÃ³n de horario nocturno.",
    packages: [
      {
        name: "Paquete ArmonÃ­a",
        estacionamiento: "Amplia capacidad con servicio de Valet Parking incluido.",
        hospedaje: "Espacio privado con capacidad para 14 personas. Cuenta con cocina, baÃ±os, Ã¡rea de jardÃ­n, alberca privada, habitaciones amplias con aire acondicionado y estacionamiento propio (costo adicional por estancia).",
        suiteNupcial: "Espacio exclusivo con jacuzzi, vestidor, tocador elegante y romÃ¡ntico diseÃ±ado para brindar confort y privacidad en ese dÃ­a especial (habitaciÃ³n incluida para novios).",
        areaJardin: "Jardines amplios y maduros con fuente artificial iluminada en la entrada principal.",
        iluminacion: "DiseÃ±o de luz arquitectÃ³nica interior y exterior que realza la belleza de cada espacio, resaltando detalles tanto en interiores como en exteriores.",
        areaConsagrada: "Espacio Ã­ntimo y armonioso, ideal para ceremonias y momentos especiales en un entorno natural y lleno de paz.",
        areaTechada: "SalÃ³n abierto cubierto con capacidad para albergar hasta 250 personas, con estilo arquitectÃ³nico modernista y elegante.",
        areaCocina: "Amplia y funcional cocina equipada para el servicio de banquetes.",
        usoRecinto: "10 horas de servicio continuo sin restricciÃ³n de horario.",
        coctel: "Coctel de bienvenida con periqueras altas, salas lounge y sombrillas. Incluye margaritas de sabores servidas en copa flauta sin alcohol, agua fresca de fruta natural, cruditÃ©s (pepino, jÃ­cama y zanahoria con miguelito y chamoy), mojito sin alcohol y piÃ±ada sin alcohol.",
        montaje: "Mesa principal con sillones imperiales Rey & Reyna. Arreglo natural para centro de mesa con elegante flor natural de temporada (diseÃ±os redondos, altos y bajos). Mesa redonda para 8 o 10 personas con silla Tiffany blanca. Mesa cuadrada de 10 a 12 personas con mantel blanco. Mesa Campirana de 10 a 12 personas (rectangular de madera con silla crossback, Tiffany blanca, boss o lotus). Mesa tipo mÃ¡rmol para 10 a 12 personas (rectangular con acabado tipo mÃ¡rmol con combinaciÃ³n de sillas). MantelerÃ­a de tela (mantel, camino y servilleta) en el color de su elecciÃ³n. Plato base (varios modelos), loza blanca de alta calidad, cuberterÃ­a fina (plata, dorado y gold rose) y cristalerÃ­a (copas transparentes y de color, vaso cubero y tequilero).",
        menu: "Banquete formal a 3 tiempos:<br>â€¢ **Primer Tiempo (Entradas):** Frescas ensaladas o deliciosas cremas ideales para iniciar tu experiencia gastronÃ³mica.<br>â€¢ **Segundo Tiempo (Plato Fuerte):** Exquisitas opciones de pollo o cerdo, acompaÃ±adas de dos guarniciones a elegir, pan y chiles al centro.<br>â€¢ **Tercer Tiempo (Tornafiesta):** Barra de esquites o chilaquiles servidos en desechables (calculado al 60% de invitados).",
        menuInfantil: "MenÃº infantil completo incluido con tiritas de milanesa, hamburguesa o nuggets de pollo acompaÃ±adas de espagueti, papas a la francesa y una golosina sorpresa.",
        mezcladores: "Nuestra oferta de mezcladores incluye un servicio completo de hielo en cubos, agua natural y una variedad de refrescos de la lÃ­nea Coca-Cola (manzana, toronja, agua mineral y la clÃ¡sica Coca-Cola, ademÃ¡s de limÃ³n y sal).",
        equipo: "Coordinador General, CapitÃ¡n de Meseros, Hostess de bienvenida, Meseros capacitados para el servicio, Personal de barra y Personal de baÃ±os.",
        dj: "DJ profesional con amplia experiencia. Incluye mampara DJ, audio e iluminaciÃ³n de alta calidad, torres iluminadas con cabezas robÃ³ticas, pantalla con proyector, globos multicolores, collares hawaianos (corbatas y velos para boda), lÃ¡mpara led wash, micrÃ³fono inalÃ¡mbrico, tramoya para iluminaciÃ³n y mÃ¡quina de humo.",
        cortesias: "Letras decorativas a elegir 'XV' o 'LOVE', corazÃ³n rojo decorativo iluminado, mesa especial para pastel, mesa especial para regalos, detonaciÃ³n de dos chisperos de pirotecnia en frÃ­o y alfombra roja para la entrada.",
        duracion: "10 horas continuas de servicio.",
        detalles: "La planificaciÃ³n y ejecuciÃ³n de su evento incluye un servicio integral que cubre desde la llegada de los invitados hasta el final de la celebraciÃ³n.",
        calidad: "Nos comprometemos a ofrecer un servicio de alta calidad, asegurando que cada evento sea Ãºnico y memorable.",
        costos: "â€¢ **100 â€“ 150 personas:** $1,700.00 MXN por persona<br>â€¢ **151 â€“ 250 personas:** $1,450.00 MXN por persona",
        cortesiasAdic: "Pista pixel LED 5x5m de cortesÃ­a.<br>A elegir 2 opciones adicionales: Pista pixel, cabina 360 o robot leds.",
        condiciones: "Se requiere un depÃ³sito de apartado para reservar la fecha.",
        beneficios: "AtenciÃ³n personalizada y coordinaciÃ³n integral del evento.",
        opcionesAdic: "Montaje de ceremonia en el Ã¡rea consagrada y barra de bebidas premium.",
        requisitos: "ConfirmaciÃ³n de invitados y selecciÃ³n de menÃº.",
        notas: "Los precios NO incluyen impuestos. Se aplican tarifas adicionales por servicios extra.",
        notaFinal: "Al firmar el contrato: DegustaciÃ³n exclusiva (4 personas), diseÃ±o de montaje de acuerdo a la paleta de colores, croquis de distribuciÃ³n detallada de invitados, minuto a minuto (cronograma detallado del evento) y chat exclusivo de comunicaciÃ³n directa. Planner Richard HernÃ¡ndez y C.P. Jessica RodrÃ­guez (Tels: 7774587923 - 7775032733)."
      }
    ]
  },
  {
    id: "bloque-3",
    name: "Bloque 3: Finca Las Isabeles",
    ubicacion: "Xochitepec, Morelos.",
    capacidad: "200 a 400 invitados.",
    estilo: "Finca campestre rÃºstica elegante tropical rodeada de abundante naturaleza.",
    fortalezas: "Ãreas verdes rodeadas de palmeras exÃ³ticas, salÃ³n abierto cubierto ideal para climas cÃ¡lidos y alberca iluminada.",
    pagina: "https://primaveraeventsgroup.com/finca-las-isabeles/",
    restricciones: "Ninguna. 10 horas de servicio sin restricciÃ³n de horario nocturno.",
    packages: [
      {
        name: "Paquete Nature's Majesty",
        estacionamiento: "Amplia capacidad para autos con servicio de valet parking incluido.",
        hospedaje: "Disfrute de una estancia cÃ³moda y tranquila en nuestras cabaÃ±as, diseÃ±adas para brindar descanso, privacidad y un ambiente acogedor en medio de la naturaleza. Ideal para complementar su evento o prolongar la experiencia con una noche especial (Previa reserva y costo adicional).",
        suiteNupcial: "Espacio exclusivo en un ambiente romÃ¡ntico para ese dÃ­a tan especial (habitaciÃ³n incluida para los novios).",
        areaJardin: "Variedad de escenarios naturales y elegantes con cascada e iluminaciÃ³n.",
        iluminacion: "DiseÃ±o de luz arquitectÃ³nica interior y exterior que realza la belleza de cada espacio, creando ambientes sofisticados y resaltando detalles tanto en interiores como en exteriores.",
        areaConsagrada: "Espacio Ã­ntimo y armonioso, ideal para ceremonias y momentos especiales en un entorno natural y lleno de paz.",
        areaTechada: "SalÃ³n abierto para albergar un mÃ¡ximo de 400 personas, de estilo arquitectÃ³nico modernista y elegante.",
        areaCocina: "Amplia y funcional Ã¡rea de cocina para preparaciÃ³n culinaria.",
        usoRecinto: "Uso de la Quinta por 10 Horas de servicio sin restricciÃ³n de horario.",
        coctel: "Coctel de bienvenida con periqueras altas, salas lounge y sombrillas. Incluye margaritas de sabores servidas en copa flauta sin alcohol, agua fresca de fruta natural, cruditÃ©s (pepino, jÃ­cama y zanahoria con miguelito y chamoy), mojito sin alcohol y piÃ±ada (sin alcohol).",
        montaje: "Mesa principal con sillones Rey & Reyna (mesa de honor equipada con sillones, templete de madera y back decorado con luces vintage y telas). Arreglo natural para centro de mesa con flor de temporada. Mesa redonda para 8 o 10 personas con silla Tiffany blanca. Mesa cuadrada de 10 a 12 personas con mantel blanco. Mesa Campirana de 10 a 12 personas (rectangular de madera con silla crossback, Tiffany blanca, boss o lotus). Mesa tipo mÃ¡rmol para 10 a 12 personas (rectangular con acabado tipo mÃ¡rmol con combinaciÃ³n de sillas). MantelerÃ­a de tela (mantel, camino y servilleta) en el color de su elecciÃ³n. Plato base (varios modelos), loza blanca de alta calidad, cuberterÃ­a fina plateada o dorada/gold rose y cristalerÃ­a fina.",
        menu: "Banquete formal a 3 tiempos:<br>â€¢ **Primer Tiempo (Entradas):** Frescas ensaladas o deliciosas cremas ideales para iniciar tu experiencia gastronÃ³mica.<br>â€¢ **Segundo Tiempo (Plato Fuerte):** Exquisitas opciones de pollo o cerdo, acompaÃ±adas de dos guarniciones a elegir, pan y chiles al centro de la mesa.<br>â€¢ **Tercer Tiempo (Tornafiesta):** Barra de esquites o chilaquiles servidos en desechables para cerrar con broche de oro (se considera al 60% de invitados).",
        menuInfantil: "MenÃº Infantil completo incluido con tiritas de milanesa, hamburguesa o nuggets de pollo acompaÃ±adas de espagueti, papas a la francesa y una golosina sorpresa.",
        mezcladores: "Nuestra oferta de mezcladores incluye un servicio completo de hielo en cubos, agua natural y una variedad de refrescos de la lÃ­nea Coca-Cola (manzana, toronja, agua mineral y la clÃ¡sica Coca-Cola, ademÃ¡s de limÃ³n y sal).",
        equipo: "Coordinador General, CapitÃ¡n de Meseros, Hostess de bienvenida, Meseros capacitados para el servicio de alimentos y bebidas, Personal de barra y Personal de baÃ±os.",
        dj: "DJ profesional con amplia experiencia. Incluye mampara DJ, audio e iluminaciÃ³n de alta calidad, torres iluminadas con cabezas robÃ³ticas, pantalla con proyector, globos multicolores, collares hawaianos (corbatas y velos para boda), lÃ¡mpara led wash, micrÃ³fono inalÃ¡mbrico, tramoya para iluminaciÃ³n y mÃ¡quina de humo.",
        cortesias: "Letras decorativas a elegir 'XV' o 'LOVE', corazÃ³n rojo decorativo iluminado, mesa especial para pastel, mesa especial para regalos, detonaciÃ³n de dos chisperos de pirotecnia en frÃ­o y alfombra roja para la entrada.",
        duracion: "10 horas continuas de servicio.",
        detalles: "La planificaciÃ³n y ejecuciÃ³n de su evento incluye un servicio integral que cubre desde la llegada de los invitados hasta el final de la celebraciÃ³n.",
        calidad: "Nos comprometemos a ofrecer un servicio de alta calidad, asegurando que cada evento sea Ãºnico y memorable.",
        costos: "â€¢ **100 â€“ 200 personas:** $1,999.00 MXN por persona<br>â€¢ **201 â€“ 300 personas:** $1,899.00 MXN por persona<br>â€¢ **301 â€“ 400 personas:** $1,799.00 MXN por persona",
        cortesiasAdic: "â€¢ **Escala 100-200 px:** Pista leds 5x5m de cortesÃ­a.<br>â€¢ **Escala 201-300 px:** A elegir 2 opciones: pista leds 5x5, cabina 360, robot leds o show men performance.<br>â€¢ **Escala 301-400 px:** A elegir 3 opciones: pista leds 5x5, cabina 360, robot leds o show men performance.",
        condiciones: "Se requiere un depÃ³sito de apartado para reservar la fecha.",
        beneficios: "AtenciÃ³n personalizada y coordinaciÃ³n integral del evento por parte de Primavera Events Group.",
        opcionesAdic: "Montaje de ceremonia en el Ã¡rea consagrada y barra de bebidas premium.",
        requisitos: "ConfirmaciÃ³n de invitados y selecciÃ³n de menÃº.",
        notas: "Los precios NO incluyen impuestos. Se aplican tarifas adicionales por servicios extra.",
        notaFinal: "Al firmar el contrato: DegustaciÃ³n exclusiva (4 personas), diseÃ±o de montaje de acuerdo a la paleta de colores, croquis de distribuciÃ³n, minuto a minuto (cronograma detallado) y chat exclusivo de comunicaciÃ³n. Responsables: Jessy y Richard (Tels: 7774587923 - 7775032733)."
      }
    ]
  },
  {
    id: "bloque-4",
    name: "Bloque 4: JardÃ­n La Flor",
    ubicacion: "Privada las Fuentes s/n, San Gaspar, Jiutepec, Morelos.",
    capacidad: "100 a 300 invitados.",
    estilo: "JardÃ­n clÃ¡sico de Cuernavaca, fresco, romÃ¡ntico e Ã­ntimo.",
    fortalezas: "Explanada para montajes con cascada monumental de bienvenida con iluminaciÃ³n y Ã¡rea consagrada para ceremonias al aire libre.",
    pagina: "https://primaveraeventsgroup.com/jardin-la-flor/",
    restricciones: "Cierre de mÃºsica a la 01:00 AM.",
    packages: [
      {
        name: "Paquete Esencia Floral",
        estacionamiento: "Amplio estacionamiento interno que alberga hasta 60 autos de forma segura.",
        hospedaje: "No disponible en el recinto. Convenios con hoteles cercanos en Jiutepec.",
        suiteNupcial: "Ãrea de camerino o suite privada de preparaciÃ³n disponible para los anfitriones.",
        areaJardin: "Entorno natural y jardÃ­n plano con abundante vegetaciÃ³n que aporta frescura y amplitud.",
        iluminacion: "IluminaciÃ³n perimetral decorativa y hermosa cascada iluminada rodeada de vegetaciÃ³n natural.",
        areaConsagrada: "Ãrea consagrada destinada a ceremonias religiosas con solemnidad en un ambiente Ã­ntimo y espiritual.",
        areaTechada: "SalÃ³n techado y abierto para albergar un mÃ¡ximo de 200 personas, con estilo arquitectÃ³nico modernista y elegante.",
        areaCocina: "Amplia y funcional cocina equipada para catering profesional.",
        usoRecinto: "Uso del salÃ³n por 8 horas (servicio disponible hasta la 01:00 AM).",
        coctel: "Coctel de bienvenida con periqueras altas, salas lounge y sombrillas. Incluye margaritas de sabores sin alcohol (2 sabores), piÃ±adas sin alcohol, mojitos sin alcohol, agua fresca (2 sabores) y cruditÃ©s (pepino, jÃ­cama y zanahoria con miguelito y chamoy).",
        montaje: "Mesa principal de honor con sillones Rey & Reyna, templete de madera, back con luces vintage y telas, y centro floral natural. Arreglo natural para centro de mesa (diseÃ±os redondos, largos y altos con flor de temporada). Mesa redonda para 8 o 10 personas con silla Tiffany blanca. Mesa cuadrada de 10 a 12 personas con mantel blanco. Mesa Campirana de 10 a 12 personas (rectangular de madera con silla crossback, Tiffany blanca, boss o lotus). Mesa tipo mÃ¡rmol para 10 a 12 personas (rectangular con acabado tipo mÃ¡rmol con combinaciÃ³n de sillas). MantelerÃ­a, plato base (varios modelos), loza blanca de alta calidad, cuberterÃ­a fina en tonos plata/dorado/gold rose y cristalerÃ­a fina.",
        menu: "Banquete formal a 4 tiempos:<br>â€¢ **Primer Tiempo (Entrada):** Frescas ensaladas o deliciosas cremas cremosas para iniciar.<br>â€¢ **Segundo Tiempo (Plato Fuerte):** Exquisitas opciones de pollo o cerdo, acompaÃ±adas de dos guarniciones a elegir, pan y chiles al centro de la mesa.<br>â€¢ **Tercer Tiempo (Tornafiesta):** Barra de esquites o chilaquiles servidos en desechables (calculado al 60% de invitados).<br>â€¢ **Cuarto Tiempo (Postre):** SelecciÃ³n de postres finos de autor.",
        menuInfantil: "MenÃº infantil completo incluido con tiritas de milanesa, hamburguesa o nuggets de pollo acompaÃ±adas de espagueti, papas a la francesa y una golosina sorpresa.",
        mezcladores: "Servicio completo de mezcladores: hielo en cubos, agua natural y refrescos de la lÃ­nea Coca-Cola (sabores, mineral, clÃ¡sica), limÃ³n y sal.",
        equipo: "Coordinador General, CapitÃ¡n de Meseros, Hostess de bienvenida, Meseros capacitados, Personal de barra, Cocineros profesionales, Personal de mantenimiento de sanitarios.",
        dj: "DJ profesional con mampara moderna, audio e iluminaciÃ³n de alta calidad, torres iluminadas con cabezas robÃ³ticas, pantalla con proyector, globos multicolores, pulseras neÃ³n y collares hawaianos (corbatas y velos para boda), 2 chisperos a control remoto, micrÃ³fonos inalÃ¡mbricos, lÃ¡ser y mÃ¡quina de humo.",
        cortesias: "Letras decorativas a elegir 'XV' o 'LOVE', corazÃ³n rojo decorativo iluminado, mesa especial para pastel, mesa especial para regalos, detonaciÃ³n de dos chisperos de pirotecnia en frÃ­o y alfombra roja.",
        duracion: "8 horas de servicio continuo.",
        detalles: "La planificaciÃ³n y ejecuciÃ³n de su evento incluye un servicio de planeaciÃ³n integral paso a paso.",
        calidad: "Compromiso de alta calidad de alimentos y servicio garantizado por la firma Primavera Events Group.",
        costos: "â€¢ **100 â€“ 199 personas:** $999.00 MXN por persona<br>â€¢ **200 â€“ 300 personas:** $899.00 MXN por persona",
        cortesiasAdic: "DegustaciÃ³n de platillos, diseÃ±o de montaje y croquis de distribuciÃ³n de invitados.",
        condiciones: "Se requiere un depÃ³sito de apartado para reservar la fecha.",
        beneficios: "AtenciÃ³n personalizada de los Wedding Planners y DirecciÃ³n Creativa de Primavera.",
        opcionesAdic: "Montaje de ceremonia en el Ã¡rea consagrada y barra de bebidas premium.",
        requisitos: "ConfirmaciÃ³n final de invitados y selecciÃ³n de menÃº y decoraciÃ³n.",
        notas: "Precios NO incluyen impuestos (IVA). Se aplican tarifas adicionales por servicios extra.",
        notaFinal: "Al firmar el contrato: DegustaciÃ³n exclusiva (4 personas), diseÃ±o de montaje de acuerdo a la paleta de colores, croquis de distribuciÃ³n detallada de invitados, minuto a minuto y chat exclusivo de coordinaciÃ³n directa. Planner Richard HernÃ¡ndez y W.P. Jessica RodrÃ­guez (Tels: 7774587923 / 7775032733)."
      }
    ]
  },
  {
    id: "bloque-5",
    name: "Bloque 5: SalÃ³n Los Potrillos",
    ubicacion: "Francisco I. Madero 23, Tepetzingo, 62767 Crucero Tezoyuca, Morelos.",
    capacidad: "100 a 500 invitados.",
    estilo: "RÃºstico ecuestre campirano tradicional estilo rancho elegante.",
    fortalezas: "Picadero visible para espectÃ¡culos de charros, gran calidez tradicional, Ã¡rea al aire libre con alberca y palapa gigante.",
    pagina: "https://primaveraeventsgroup.com/salon-los-potrillos/",
    restricciones: "Cierre de mÃºsica a la 01:00 AM.",
    packages: [
      {
        name: "Paquete Linaje Pura Sangre",
        estacionamiento: "Amplio estacionamiento cerrado con capacidad para 100 vehÃ­culos compactos.",
        hospedaje: "No disponible en el recinto. Convenios con hoteles cercanos en Tezoyuca/Xochitepec.",
        suiteNupcial: "No disponible en el recinto. Se cuenta con camerino privado de uso bÃ¡sico.",
        areaJardin: "Ãrea de jardÃ­n plano con puente rÃºstico y fuente artificial en la entrada principal.",
        iluminacion: "IluminaciÃ³n perimetral decorativa bÃ¡sica.",
        areaConsagrada: "No disponible dentro del recinto. Se recomienda realizar ceremonias en iglesias locales.",
        areaTechada: "SalÃ³n techado y abierto para albergar un mÃ¡ximo de 400 personas, con estilo modernista y elegante.",
        areaCocina: "Amplia y funcional Ã¡rea de cocina y baÃ±os mÃºltiples para invitados.",
        usoRecinto: "Uso de salÃ³n por 8 Horas sin restricciÃ³n de horario (tiempo extra disponible).",
        coctel: "Coctel de bienvenida con periqueras altas, salas lounge y sombrillas. Incluye margaritas de sabores sin alcohol (2 sabores), piÃ±ada sin alcohol, mojito sin alcohol, agua fresca (2 sabores) y cruditÃ©s (pepino, jÃ­cama y zanahoria con miguelito y chamoy).",
        montaje: "Mesa principal de honor con sillÃ³n o sillones, templete de madera y centro de mesa floral natural de temporada. Arreglos naturales para centros de mesa (largo y redondo). Bases de metal altas para centros de mesa. Mesa tipo mÃ¡rmol cuadrada para 10 personas con silla Tiffany blanca. Mesa redonda para 10 o 12 personas con silla Tiffany blanca. MantelerÃ­a fina (mantel blanco, camino y servilleta de tela de color a elegir). Plato base (varios modelos), loza blanca, cuberterÃ­a fina plateada o dorada y cristalerÃ­a fina.",
        menu: "Banquete formal a 3 tiempos:<br>â€¢ **Primer Tiempo (Entradas):** Deliciosas crepas, frescas ensaladas o cremosas sopas.<br>â€¢ **Segundo Tiempo (Plato Fuerte):** Exquisitas opciones de pollo o cerdo, acompaÃ±adas de dos guarniciones a elegir, pan y chiles al centro de la mesa.<br>â€¢ **Tercer Tiempo (Tornafiesta):** Barra de esquites o chilaquiles servidos en desechables.",
        menuInfantil: "MenÃº infantil disponible bajo cotizaciÃ³n separada ($220.00 MXN).",
        mezcladores: "Nuestra oferta de mezcladores incluye un servicio completo de hielo en cubos, agua natural y una variedad de refrescos de la lÃ­nea Coca-Cola (manzana, toronja, agua mineral y la clÃ¡sica Coca-Cola, ademÃ¡s de limÃ³n y sal).",
        equipo: "Coordinador General, CapitÃ¡n de Meseros, Hostess de bienvenida, Meseros capacitados, Personal de barra, Cocineros y Personal de baÃ±os.",
        dj: "DJ profesional con cabina, audio de alta fidelidad, iluminaciÃ³n robÃ³tica mÃ³vil, pantalla con proyector, globos, pulseras neÃ³n y collares hawaianos (corbatas/velos en bodas), 2 chisperos a control remoto, micrÃ³fonos inalÃ¡mbricos, lÃ¡ser y mÃ¡quina de humo.",
        cortesias: "Letras decorativas gigantes 'XV' o 'LOVE', corazÃ³n rojo decorativo, mesa especial para pastel, mesa especial para regalos, detonaciÃ³n de dos chisperos de pirotecnia en frÃ­o y alfombra roja.",
        duracion: "9 horas de servicio continuo.",
        detalles: "LogÃ­stica y planeaciÃ³n integral de la boda o evento por parte de Primavera Events Group.",
        calidad: "Compromiso de alta calidad de alimentos y servicio garantizado por contrato.",
        costos: "â€¢ **100 â€“ 199 personas:** $799.00 MXN por persona<br>â€¢ **200 â€“ 299 personas:** $749.00 MXN por persona<br>â€¢ **300 â€“ 399 personas:** $699.00 MXN por persona<br>â€¢ **400 â€“ 500 personas:** $649.00 MXN por persona<br>â€¢ **501+ personas:** Consultar tarifa personalizada.",
        cortesiasAdic: "DegustaciÃ³n de platillos y decoraciÃ³n bÃ¡sica del salÃ³n.",
        condiciones: "Precios sujetos a cambios sin previo aviso. Se requiere depÃ³sito de reserva.",
        beneficios: "AtenciÃ³n personalizada y coordinaciÃ³n integral.",
        opcionesAdic: "Montaje de ceremonia al aire libre y barra de bebidas premium.",
        requisitos: "ConfirmaciÃ³n de invitados y selecciÃ³n de menÃº.",
        notes: "Los precios NO incluyen impuestos. Se aplican tarifas adicionales por servicios extra.",
        notaFinal: "Al firmar el contrato: DegustaciÃ³n exclusiva (4 personas), diseÃ±o de montaje, croquis de distribuciÃ³n detallada de invitados, minuto a minuto y chat exclusivo de comunicaciÃ³n directa. Planner Richard HernÃ¡ndez y W.P. Jessica RodrÃ­guez."
      }
    ]
  },
  {
    id: "bloque-6",
    name: "Bloque 6: JardÃ­n Tsu Nuum",
    ubicacion: "Carretera a Aeropuerto de Cuernavaca, KM 0.5, Xochitepec, Morelos, MÃ©xico.",
    capacidad: "100 a 250 invitados.",
    estilo: "Zen moderno y minimalista con paisajismo internacional de autor.",
    fortalezas: "Alta privacidad, escenarios fotogÃ©nicos Ãºnicos y gran iluminaciÃ³n ambiental nocturna en los Ã¡rboles maduros. CercanÃ­a al aeropuerto de Cuernavaca y suite privada.",
    pagina: "https://primaveraeventsgroup.com/jardin-tsu-nuum/",
    restricciones: "Ninguna. 10 horas sin restricciones de horario nocturno.",
    packages: [
      {
        name: "Paquete Vuelo Esmeralda",
        estacionamiento: "Amplia capacidad de autos con servicio de valet parking incluido.",
        hospedaje: "Hotel con capacidad para 60 personas a tan solo 80 metros del jardÃ­n, reservaciÃ³n previa (costo adicional por estancia).",
        suiteNupcial: "Suite privada. Espacio Ã­ntimo y elegante diseÃ±ado para brindar confort, privacidad y un ambiente lleno de encanto. Ideal tanto para los novios como para quinceaÃ±eras, ofrece el escenario perfecto para relajarse, prepararse y culminar su celebraciÃ³n con una estancia especial.",
        areaJardin: "Jardines zen de diseÃ±o paisajista con abundante flora exÃ³tica y fuente artificial en la entrada principal.",
        iluminacion: "DiseÃ±o de luz arquitectÃ³nica interior y exterior que realza la belleza de cada espacio, creando ambientes sofisticados y resaltando detalles tanto en interiores como en exteriores.",
        areaConsagrada: "Espacio Ã­ntimo y armonioso, ideal para ceremonias y momentos especiales en un entorno natural y lleno de paz.",
        areaTechada: "Ãrea techada para albergar hasta 250 personas, con estilo arquitectÃ³nico modernista y elegante.",
        areaCocina: "Amplia y funcional cocina equipada para el servicio de banquetes.",
        usoRecinto: "Uso de la locaciÃ³n por 10 Horas de servicio continuo sin restricciÃ³n de horario.",
        coctel: "Coctel de bienvenida con periqueras altas, salas lounge y sombrillas. Incluye margaritas de sabores servidas en copa flauta sin alcohol, agua fresca de fruta natural, cruditÃ©s (pepino, jÃ­cama y zanahoria con miguelito y chamoy), mojito sin alcohol y piÃ±ada (sin alcohol).",
        montaje: "Mesa principal con sillones Rey & Reyna (mesa de honor equipada con sillones, templete de madera y back decorado con luces vintage y telas). Arreglo natural para centro de mesa con elegante flor natural de temporada. Mesa redonda para 8 o 10 personas con silla Tiffany blanca. Mesa cuadrada de 10 a 12 personas con mantel blanco. Mesa Campirana de 10 a 12 personas (rectangular de madera con silla crossback, Tiffany blanca, boss o lotus). Mesa tipo mÃ¡rmol para 10 a 12 personas (rectangular con acabado tipo mÃ¡rmol con combinaciÃ³n de sillas). MantelerÃ­a de tela (mantel, camino y servilleta) en el color de su elecciÃ³n. Plato base (varios modelos), loza blanca de alta calidad, cuberterÃ­a fina plateada o dorada/gold rose y cristalerÃ­a fina.",
        menu: "Banquete formal a 3 tiempos:<br>â€¢ **Primer Tiempo (Entradas):** Frescas ensaladas o deliciosas cremas ideales para iniciar tu experiencia gastronÃ³mica.<br>â€¢ **Segundo Tiempo (Plato Fuerte):** Exquisitas opciones de pollo o cerdo, acompaÃ±adas de dos guarniciones a elegir, pan y chiles al centro de la mesa.<br>â€¢ **Tercer Tiempo (Tornafiesta):** Barra de esquites o chilaquiles servidos en desechables para cerrar con broche de oro (se considera al 60% de invitados).",
        menuInfantil: "MenÃº Infantil completo incluido con tiritas de milanesa, hamburguesa o nuggets de pollo acompaÃ±adas de espagueti, papas a la francesa y una golosina sorpresa.",
        mezcladores: "Nuestra oferta de mezcladores incluye un servicio completo de hielo en cubos, agua natural y una variedad de refrescos de la lÃ­nea Coca-Cola (manzana, toronja, agua mineral y la clÃ¡sica Coca-Cola, ademÃ¡s de limÃ³n y sal).",
        equipo: "Coordinador General, CapitÃ¡n de Meseros, Hostess de bienvenida, Meseros capacitados, Personal de barra y Personal de baÃ±os.",
        dj: "DJ profesional con amplia experiencia. Incluye mampara DJ, audio e iluminaciÃ³n de alta calidad, torres iluminadas con cabezas robÃ³ticas, pantalla con proyector, globos multicolores, collares hawaianos (corbatas y velos para boda), lÃ¡mpara led wash, micrÃ³fono inalÃ¡mbrico, tramoya para iluminaciÃ³n y mÃ¡quina de humo.",
        cortesias: "Letras decorativas a elegir 'XV' o 'LOVE', corazÃ³n rojo decorativo iluminado, mesa especial para pastel, mesa especial para regalos, detonaciÃ³n de dos chisperos de pirotecnia en frÃ­o y alfombra roja.",
        duracion: "10 horas continuas de servicio.",
        detalles: "La planificaciÃ³n y ejecuciÃ³n de su evento incluye un servicio integral que cubre desde la llegada de los invitados hasta el final de la celebraciÃ³n.",
        calidad: "Nos comprometemos a ofrecer un servicio de alta calidad, asegurando que cada evento sea Ãºnico y memorable.",
        costos: "â€¢ **100 â€“ 150 personas:** $2,199.00 MXN por persona<br>â€¢ **151 â€“ 200 personas:** $2,099.00 MXN por persona<br>â€¢ **201 â€“ 250 personas:** $1,999.00 MXN por persona",
        cortesiasAdic: "Pista pixel LED 5x5m de cortesÃ­a.<br>â€¢ **Escala 151-200 px:** Elegir 1: pista pixel 5x5, robot leds, cabina 360 o barra mix con dulces y salados durante el coctel.<br>â€¢ **Escala 201-250 px:** Elegir 2: pista pixel 5x5, robot leds, cabina 360 o cabina inflable.",
        condiciones: "Firma de contrato y depÃ³sito para apartado de fecha.",
        beneficios: "AtenciÃ³n personalizada, CoordinaciÃ³n integral y DirecciÃ³n Creativa Top-Tier.",
        opcionesAdic: "Montaje de ceremonia en el Ã¡rea consagrada y barra de bebidas premium.",
        requisitos: "ConfirmaciÃ³n y entrega de lista de invitados.",
        notas: "Los precios NO incluyen impuestos. Se aplican tarifas adicionales por servicios extra. Todo lo anterior.",
        notaFinal: "Al firmar el contrato: DegustaciÃ³n exclusiva (4 personas), diseÃ±o de montaje de acuerdo a la paleta de colores, croquis de distribuciÃ³n, minuto a minuto y chat exclusivo de comunicaciÃ³n. Responsables: Jessy y Richard. Richard H (Founder & Creative Director) y Jessy R (Founder & Lead Planner) (Tels: 7774587923)."
      }
    ]
  },
  {
    id: "bloque-7",
    name: "Bloque 7: SalÃ³n Los Caballos",
    ubicacion: "Calle Zaragoza 1107, Ocotepec, Cuernavaca, Morelos.",
    capacidad: "100 a 300 invitados.",
    estilo: "Hacienda con establos elegantes de exhibiciÃ³n y cantera tallada.",
    fortalezas: "Gran capacidad logÃ­stica, estacionamiento cerrado masivo e ideal para graduaciones y eventos masivos corporativos.",
    pagina: "https://primaveraeventsgroup.com/salon-los-caballos/",
    restricciones: "Cierre de mÃºsica a la 01:00 AM.",
    packages: [
      {
        name: "Paquete Imperial Ecuestre",
        estacionamiento: "Amplio estacionamiento cerrado con capacidad para autos de los invitados.",
        hospedaje: "No disponible en el recinto. Convenios con hoteles cercanos en Cuernavaca norte.",
        suiteNupcial: "No disponible en el recinto. Se cuenta con camerino privado de uso bÃ¡sico.",
        areaJardin: "Ãrea de jardÃ­n plano con fuente artificial en la entrada principal.",
        iluminacion: "Sistema de iluminaciÃ³n arquitectÃ³nica estratÃ©gica interna y externa que realza la arquitectura y detalles del espacio.",
        areaConsagrada: "No disponible dentro del recinto. Se recomienda realizar ceremonias en iglesias locales.",
        areaTechada: "SalÃ³n techado y cerrado para albergar un mÃ¡ximo de 300 personas, con estilo arquitectÃ³nico modernista y elegante.",
        areaCocina: "Amplia y funcional cocina equipada para el catering.",
        usoRecinto: "Uso del salÃ³n por 8 horas de servicio hasta la 01:00 am.",
        coctel: "Coctel de bienvenida con periqueras altas, salas lounge y sombrillas. Incluye margaritas de sabores servidas en copa flauta sin alcohol, agua fresca, cruditÃ©s (pepino, jÃ­cama y zanahoria con miguelito y chamoy), mojito sin alcohol y piÃ±ada sin alcohol.",
        montaje: "Mesa principal de honor con sillÃ³n o sillones, templete de madera y centro de mesa floral natural. Arreglos naturales para centros de mesa. Bases de metal altas para centros de mesa. Montaje en mesa cuadrada y rectangular de madera con sillerÃ­a Tiffany blanca o crossback. MantelerÃ­a fina (mantel blanco, camino y servilleta de tela de color a elegir). Plato base (varios modelos), loza blanca, cuberterÃ­a fina plateada o dorada y cristalerÃ­a fina.",
        menu: "Banquete formal a 4 tiempos:<br>â€¢ **Primer Tiempo (Entrada):** Frescas ensaladas o cremosas sopas.<br>â€¢ **Segundo Tiempo (Plato Fuerte):** Exquisitas opciones de pollo o cerdo, acompaÃ±adas de dos guarniciones a elegir, pan y chiles al centro de la mesa.<br>â€¢ **Tercer Tiempo (Tornafiesta):** Barra de esquites o chilaquiles servidos en desechables (calculado al 60% de invitados).",
        menuInfantil: "MenÃº infantil completo incluido con tiritas de milanesa, hamburguesa o nuggets de pollo acompaÃ±adas de pasta, papas a la francesa y una golosina sorpresa.",
        mezcladores: "Nuestra oferta de mezcladores incluye un servicio completo de hielo en cubos, agua natural y una variedad de refrescos de la lÃ­nea Coca-Cola (manzana, toronja, agua mineral y la clÃ¡sica Coca-Cola, ademÃ¡s de jugo de limÃ³n y sal).",
        equipo: "Coordinador General, CapitÃ¡n de Meseros, Hostess de bienvenida, Meseros capacitados, Personal de barra, Cocineros y Personal de baÃ±os.",
        dj: "DJ profesional con cabina, audio de alta fidelidad, iluminaciÃ³n robÃ³tica mÃ³vil, pantalla gigante o 2 pantallas, globos, pulseras neÃ³n y collares hawaianos (corbatas/velos en bodas), lÃ¡mparas led wash, micrÃ³fonos inalÃ¡mbricos, lÃ¡ser y mÃ¡quina de humo.",
        cortesias: "Letras decorativas gigantes 'XV' o 'LOVE', corazÃ³n rojo decorativo, mesa especial para pastel, mesa especial para regalos, detonaciÃ³n de dos chisperos de pirotecnia en frÃ­o y alfombra roja.",
        duracion: "9 horas de servicio continuo.",
        detalles: "La planificaciÃ³n y ejecuciÃ³n de su evento incluye un servicio integral por parte de Primavera Events Group.",
        calidad: "Nos comprometemos a ofrecer un servicio de alta calidad, asegurando que cada evento sea Ãºnico y memorable.",
        costos: "â€¢ **100 â€“ 150 personas:** $749.00 MXN por persona<br>â€¢ **151 â€“ 200 personas:** $729.00 MXN por persona<br>â€¢ **201 â€“ 300 personas:** $699.00 MXN por persona",
        cortesiasAdic: "â€¢ **Escala 100-150 px:** Pista leds 5x5m de cortesÃ­a.<br>â€¢ **Escala 151-200 px:** Pista leds 5x5m y robot leds de cortesÃ­a.<br>â€¢ **Escala 201-300 px:** Pista leds 5x5m, robot leds y cabezones coreogrÃ¡ficos de cortesÃ­a.",
        condiciones: "Se requiere depÃ³sito para reservar la fecha.",
        beneficios: "AtenciÃ³n personalizada y coordinaciÃ³n integral del evento.",
        opcionesAdic: "Montaje de ceremonia, tiempo extra de servicio y renta de limosinas.",
        requisitos: "ConfirmaciÃ³n de invitados, selecciÃ³n de menÃº y elecciÃ³n de decoraciÃ³n.",
        notas: "Los precios NO incluyen impuestos. Se aplican tarifas adicionales por servicios extra. Disponibilidad sujeta a confirmaciÃ³n.",
        notaFinal: "Al firmar tu contrato: DegustaciÃ³n exclusiva (4 personas), diseÃ±o de montaje de acuerdo a la paleta de colores, croquis de distribuciÃ³n, minuto a minuto y chat exclusivo de comunicaciÃ³n directa. Responsables: Jessy y Richard."
      }
    ]
  },
  {
    id: "bloque-8",
    name: "Bloque 8: SalÃ³n JardÃ­n Yolomecatl",
    ubicacion: "Calle Palma #6, Acatlipa, Temixco, Morelos.",
    capacidad: "200 a 500 invitados.",
    estilo: "Complejo seÃ±orial cerrado con amplios jardines y salÃ³n techado.",
    fortalezas: "Capilla consagrada in-situ para ceremonias de validez oficial y gran privacidad.",
    pagina: "https://primaveraeventsgroup.com/salon-jardin-yolomecatl/",
    restricciones: "Cierre de mÃºsica a la 01:00 AM.",
    packages: [
      {
        name: "Paquete Destino Yolomecatl",
        estacionamiento: "Capacidad para 35 vehÃ­culos compactos en estacionamiento interno vigilado.",
        hospedaje: "No disponible en el recinto. Se cuenta con convenios especiales con hoteles de Temixco y Cuernavaca.",
        suiteNupcial: "No disponible en el recinto. Se puede gestionar suite externa en hotel asociado con costo preferencial.",
        areaJardin: "Jardines amplios y maduros con fuente artificial iluminada en la entrada principal.",
        iluminacion: "DiseÃ±o de luz arquitectÃ³nica bÃ¡sica en exteriores e interiores.",
        areaConsagrada: "Capilla consagrada dentro del recinto (para ceremonias religiosas con validez oficial, disponible por un costo adicional).",
        areaTechada: "SalÃ³n principal techado para albergar hasta 400 personas, con estilo modernista y elegante.",
        areaCocina: "Amplia y funcional cocina equipada para el servicio de banquetes.",
        usoRecinto: "9 horas de servicio continuo hasta la 01:00 am.",
        coctel: "Coctel de bienvenida con periqueras altas, salas lounge y sombrillas. Incluye margaritas de sabores sin alcohol (2 sabores), piÃ±ada sin alcohol, mojito sin alcohol, agua fresca (2 sabores) y cruditÃ©s (pepino, jÃ­cama y jÃ­cama y zanahoria con miguelito y chamoy).",
        montaje: "Mesa principal de honor con sillÃ³n o sillones, templete de madera y centro de mesa floral natural. Arreglos naturales para centros de mesa (largo y redondo). Bases de metal altas para centros de mesa. Mesa tipo mÃ¡rmol cuadrada para 10 personas con silla Tiffany blanca. Mesa redonda para 10 o 12 personas con silla Tiffany blanca. MantelerÃ­a fina (mantel blanco, camino y servilleta de tela de color a elegir). Plato base (varios modelos), loza blanca, cuberterÃ­a fina plateada o dorada y cristalerÃ­a fina.",
        menu: "Banquete formal a 4 tiempos:<br>â€¢ **Primer Tiempo (Entrada):** Deliciosas crepas, frescas ensaladas o cremosas sopas.<br>â€¢ **Segundo Tiempo (Plato Fuerte):** Exquisitas opciones de pollo o cerdo, acompaÃ±adas de dos guarniciones a elegir, pan y chiles al centro de la mesa.<br>â€¢ **Tercer Tiempo (Postre):** SelecciÃ³n de postres que endulzarÃ¡n tu evento, desde pasteles hasta postres de autor.<br>â€¢ **Cuarto Tiempo (Tornafiesta):** Barra de esquites o chilaquiles servidos en desechables (calculado al 60% de invitados).",
        menuInfantil: "MenÃº infantil opcional disponible a solicitud ($220.00 MXN extra por niÃ±o) con tiritas de milanesa, hamburguesas o nuggets con papas y espagueti.",
        mezcladores: "Nuestra oferta de mezcladores incluye un servicio completo de hielo en cubos, agua natural y una variedad de refrescos de la lÃ­nea Coca-Cola (manzana, toronja, agua mineral y la clÃ¡sica Coca-Cola, ademÃ¡s de limÃ³n y sal).",
        equipo: "Coordinador General, CapitÃ¡n de Meseros, Hostess de bienvenida, Meseros capacitados, Personal de barra, Stewart de limpieza, Cocineros y Personal de baÃ±os.",
        dj: "DJ profesional con cabina, audio e iluminaciÃ³n de alta calidad, torres iluminadas con cabezas robÃ³ticas, pantalla con proyector, globos, pulseras neÃ³n y collares hawaianos (corbatas/velos en bodas), 2 chisperos a control remoto, micrÃ³fonos inalÃ¡mbricos, lÃ¡ser, mÃ¡quina de humo y pista pixel de baile 5x5m.",
        cortesias: "DegustaciÃ³n para 4 personas al firmar. Letras decorativas gigantes 'XV' o 'LOVE', corazÃ³n rojo iluminado, mesas especiales de pastel y regalos, detonaciÃ³n de 2 chisperos, alfombra roja de entrada, espejo selfie, barra mix con 12 toppings dulces/salados y opciÃ³n de montaje de ceremonia con mobiliario elegante.",
        duracion: "9 horas continuas totales de servicio.",
        detalles: "La planificaciÃ³n y ejecuciÃ³n de su evento incluye un servicio integral que cubre desde la llegada de los invitados hasta el final de la celebraciÃ³n.",
        calidad: "Nos comprometemos a ofrecer un servicio de alta calidad, asegurando que cada evento sea Ãºnico y memorable.",
        costos: "â€¢ **100 â€“ 149 personas:** $899.00 MXN por persona<br>â€¢ **150 â€“ 199 personas:** $849.00 MXN por persona<br>â€¢ **200 â€“ 299 personas:** $799.00 MXN por persona<br>â€¢ **300 â€“ 400 personas:** $749.00 MXN por persona<br>â€¢ **401+ personas:** Consultar tarifa personalizada.",
        cortesiasAdic: "DegustaciÃ³n de platillos y decoraciÃ³n bÃ¡sica del salÃ³n.",
        condiciones: "Precios sujetos a cambios sin previo aviso. Se requiere depÃ³sito de reserva.",
        beneficios: "AtenciÃ³n personalizada de los Wedding Planners y DirecciÃ³n de Primavera.",
        opcionesAdic: "Montaje de ceremonia en la capilla consagrada (costo extra) y barra de bebidas premium.",
        requisitos: "ConfirmaciÃ³n final de invitados y selecciÃ³n de menÃº y decoraciÃ³n.",
        notes: "Los precios NO incluyen impuestos. Se aplican tarifas adicionales por servicios extra.",
        notaFinal: "Al firmar el contrato: DegustaciÃ³n exclusiva para 4 personas, diseÃ±o de montaje, croquis de distribuciÃ³n, minuto a minuto y chat exclusivo de comunicaciÃ³n. Planner Richard HernÃ¡ndez y Gerente Carlos Osorio (Tels: 7774587923)."
      }
    ]
  },
  {
    id: "bloque-9",
    name: "Bloque 9: Villa Di Fiori",
    ubicacion: "Xochitepec, Morelos.",
    capacidad: "100 a 350 invitados.",
    estilo: "Finca de arquitectura Toscana con imponentes arcos de cantera tallada.",
    fortalezas: "Paisajismo europeo, suite de preparaciÃ³n y fachadas perfectas para fotografÃ­a de alta gama.",
    pagina: "https://primaveraeventsgroup.com/venues/villa-di-fiori/",
    restricciones: "Cierre de mÃºsica a la 01:00 AM.",
    packages: [
      {
        name: "Paquete Esencia Floral (EdiciÃ³n Toscana)",
        estacionamiento: "Amplio estacionamiento cerrado con alta capacidad logÃ­stica.",
        hospedaje: "No disponible en el recinto. Convenios con hoteles cercanos en Xochitepec.",
        suiteNupcial: "Suite de preparaciÃ³n exclusiva y privada para anfitriones y quinceaÃ±eras con acabados elegantes.",
        areaJardin: "Jardines de diseÃ±o paisajista europeo con abundante flora exÃ³tica y explanada para banquetes.",
        iluminacion: "IluminaciÃ³n perimetral decorativa y hermosa cascada iluminada rodeada de vegetaciÃ³n natural.",
        areaConsagrada: "Ãrea consagrada al aire libre destinada a ceremonias religiosas con solemnidad en un ambiente Ã­ntimo y espiritual.",
        areaTechada: "SalÃ³n techado y abierto para albergar un mÃ¡ximo de 200 personas (y estructuras portantes en jardines para hasta 350 personas), con arcos de cantera tallada.",
        areaCocina: "Amplia y funcional cocina equipada para catering profesional.",
        usoRecinto: "Uso del salÃ³n por 8 horas (servicio disponible hasta la 01:00 AM).",
        coctel: "Coctel de bienvenida con periqueras altas, salas lounge y sombrillas. Incluye margaritas de sabores sin alcohol (2 sabores), piÃ±adas sin alcohol, mojitos sin alcohol, agua fresca (2 sabores) y cruditÃ©s (pepino, jÃ­cama y zanahoria con miguelito y chamoy).",
        montaje: "Mesa principal de honor con sillones Rey & Reyna, templete de madera, back con luces vintage y telas, y centro floral natural. Arreglo natural para centro de mesa (diseÃ±os redondos, largos y altos con flor de temporada). Mesa redonda para 8 o 10 personas con silla Tiffany blanca. Mesa cuadrada de 10 a 12 personas con mantel blanco. Mesa Campirana de 10 a 12 personas (rectangular de madera con silla crossback, Tiffany blanca, boss o lotus). Mesa tipo mÃ¡rmol para 10 a 12 personas (rectangular con acabado tipo mÃ¡rmol con combinaciÃ³n de sillas). MantelerÃ­a, plato base (varios modelos), loza blanca de alta calidad, cuberterÃ­a fina en tonos plata/dorado/gold rose y cristalerÃ­a fina.",
        menu: "Banquete formal a 4 tiempos:<br>â€¢ **Primer Tiempo (Entrada):** Frescas ensaladas o deliciosas cremas cremosas para iniciar.<br>â€¢ **Segundo Tiempo (Plato Fuerte):** Exquisitas opciones de pollo o cerdo, acompaÃ±adas de dos guarniciones a elegir, pan y chiles al centro de la mesa.<br>â€¢ **Tercer Tiempo (Tornafiesta):** Barra de esquites o chilaquiles servidos en desechables (calculado al 60% de invitados).<br>â€¢ **Cuarto Tiempo (Postre):** SelecciÃ³n de postres finos de autor.",
        menuInfantil: "MenÃº infantil completo incluido con tiritas de milanesa, hamburguesa o nuggets de pollo acompaÃ±adas de espagueti, papas a la francesa y una golosina sorpresa.",
        mezcladores: "Servicio completo de mezcladores: hielo en cubos, agua natural y refrescos de la lÃ­nea Coca-Cola (sabores, mineral, clÃ¡sica), limÃ³n y sal.",
        equipo: "Coordinador General, CapitÃ¡n de Meseros, Hostess de bienvenida, Meseros capacitados, Personal de barra, Cocineros profesionales, Personal de mantenimiento de sanitarios.",
        dj: "DJ profesional con mampara moderna, audio e iluminaciÃ³n de alta calidad, torres iluminadas con cabezas robÃ³ticas, pantalla con proyector, globos multicolores, pulseras neÃ³n y collares hawaianos (corbatas y velos para boda), 2 chisperos a control remoto, micrÃ³fonos inalÃ¡mbricos, lÃ¡ser y mÃ¡quina de humo.",
        cortesias: "Letras decorativas a elegir 'XV' o 'LOVE', corazÃ³n rojo decorativo iluminado, mesa especial para pastel, mesa especial para regalos, detonaciÃ³n de dos chisperos de pirotecnia en frÃ­o y alfombra roja.",
        duracion: "8 horas de servicio continuo.",
        detalles: "La planificaciÃ³n y ejecuciÃ³n de su evento incluye un servicio de planeaciÃ³n integral paso a paso.",
        calidad: "Compromiso de alta calidad de alimentos y servicio garantizado por la firma Primavera Events Group.",
        costos: "â€¢ **100 â€“ 199 personas:** $999.00 MXN por persona<br>â€¢ **200 â€“ 300 personas:** $899.00 MXN por persona",
        cortesiasAdic: "DegustaciÃ³n de platillos, diseÃ±o de montaje y croquis de distribuciÃ³n de invitados.",
        condiciones: "Se requiere un depÃ³sito de apartado para reservar la fecha.",
        beneficios: "AtenciÃ³n personalizada de los Wedding Planners y DirecciÃ³n de Primavera.",
        opcionesAdic: "Montaje de ceremonia en el Ã¡rea consagrada y barra de bebidas premium.",
        requisitos: "ConfirmaciÃ³n final de invitados y selecciÃ³n de menÃº y decoraciÃ³n.",
        notas: "Precios NO incluyen impuestos (IVA). Se aplican tarifas adicionales por servicios extra.",
        notaFinal: "Al firmar el contrato: DegustaciÃ³n exclusiva (4 personas), diseÃ±o de montaje de acuerdo a la paleta de colores, croquis de distribuciÃ³n detallada de invitados, minuto a minuto y chat exclusivo de coordinaciÃ³n directa. Planner Richard HernÃ¡ndez y W.P. Jessica RodrÃ­guez (Tels: 7774587923 / 7775032733)."
      }
    ]
  },
  {
    id: "bloque-10",
    name: "Bloque 10: SalÃ³n & JardÃ­n Solaire",
    ubicacion: "Cuernavaca, Morelos.",
    capacidad: "80 a 180 invitados.",
    estilo: "Industrial-chic moderno con toques de madera sÃ³lida y cascada monumental.",
    fortalezas: "Pista Pixel LED 5x5 inteligente pre-instalada y mobiliario de autor campestre. Cascada monumental en la entrada y Ã¡rea consagrada al aire libre.",
    pagina: "https://primaveraeventsgroup.com/venues/solaire/",
    restricciones: "Cierre de mÃºsica a la 01:00 AM.",
    packages: [
      {
        name: "Paquete Solaire (Propuesta Viky)",
        estacionamiento: "Estacionamiento privado con capacidad adecuada para los invitados del recinto.",
        hospedaje: "No disponible en el recinto. Convenios con hoteles cercanos en Cuernavaca.",
        suiteNupcial: "No disponible en el recinto. Camerino privado bÃ¡sico para los anfitriones.",
        areaJardin: "JardÃ­n de ambientaciÃ³n industrial-chic moderno con vegetaciÃ³n colgante y cascada monumental de bienvenida.",
        iluminacion: "IluminaciÃ³n perimetral decorativa e iluminaciÃ³n del recinto de Ãºltima generaciÃ³n.",
        areaConsagrada: "Ãrea consagrada al aire libre para ceremonias solemnes en un ambiente sofisticado.",
        areaTechada: "SalÃ³n techado estilo industrial con acabados de madera sÃ³lida y vegetaciÃ³n colgante.",
        areaCocina: "Cocina funcional equipada para el catering.",
        usoRecinto: "Uso del salÃ³n por 8 horas operativas.",
        coctel: "Coctel de bienvenida con periqueras altas, salas lounge y sombrillas. Incluye margaritas de sabores sin alcohol, agua fresca y cruditÃ©s.",
        montaje: "Mesa principal de honor con sillÃ³n o sillones, templete de madera y centro de mesa floral natural. Mobiliario de autor campirano premium (mesas vintage de madera sÃ³lida, sillas Crossback). MantelerÃ­a fina, loza, cuberterÃ­a y cristalerÃ­a fina.",
        menu: "Banquete formal gourmet a 3 tiempos:<br>â€¢ **Primer Tiempo (Entrada):** Ensaladas frescas o deliciosas cremas cremosas.<br>â€¢ **Segundo Tiempo (Plato Fuerte):** Exquisitas opciones de pollo o cerdo, acompaÃ±adas de dos guarniciones a elegir, pan y chiles al centro.<br>â€¢ **Tercer Tiempo (Tornafiesta):** Barra de esquites o chilaquiles servidos en desechables (calculado al 60% de invitados).",
        menuInfantil: "MenÃº infantil opcional disponible a solicitud ($220.00 MXN extra por niÃ±o).",
        mezcladores: "Descorche libre de 8 horas sin costo de servicio (sin cargo por botella). Servicio completo de hielo en cubos y refrescos de la lÃ­nea Coca-Cola.",
        equipo: "Coordinador General, CapitÃ¡n de Meseros, Hostess de bienvenida, Meseros capacitados, Personal de barra y Personal de baÃ±os.",
        dj: "DJ profesional con audio de alta fidelidad, iluminaciÃ³n robÃ³tica mÃ³vil, cabezas mÃ³viles, mÃ¡quina de humo y pista pixel LED 5x5m inteligente pre-instalada.",
        cortesias: "CortesÃ­a tecnolÃ³gica premium a elegir entre: Cabina de Fotos Espejo instantÃ¡nea o CÃ¡mara 360 interactiva.",
        duracion: "8 horas de servicio continuo.",
        detalles: "La planificaciÃ³n y ejecuciÃ³n de su evento incluye un servicio integral de logÃ­stica.",
        calidad: "Compromiso de alta calidad de alimentos y servicio garantizado por contrato.",
        costos: "â€¢ **Banquete Gourmet 3 Tiempos:** $1,199.00 MXN por persona<br>â€¢ **Taquiza Premium:** $590.00 MXN por persona",
        cortesiasAdic: "Pista Pixel LED 5x5m y descorche libre de cortesÃ­a.",
        condiciones: "Se requiere un depÃ³sito de apartado para reservar la fecha y firma de contrato.",
        beneficios: "AtenciÃ³n personalizada de los Wedding Planners oficiales de Primavera.",
        opcionesAdic: "Montaje de ceremonia en el Ã¡rea consagrada y barra de bebidas premium.",
        requisitos: "ConfirmaciÃ³n final de invitados (10 dÃ­as antes) y selecciÃ³n de menÃº y decoraciÃ³n.",
        notas: "Precios NO incluyen impuestos (IVA). Se aplican tarifas adicionales por servicios extra.",
        notaFinal: "Al firmar el contrato: DegustaciÃ³n exclusiva (4 personas), diseÃ±o de montaje de acuerdo a la paleta de colores, croquis de distribuciÃ³n, minuto a minuto y chat exclusivo de comunicaciÃ³n. Responsables: Jessy y Richard."
      }
    ]
  }
];

// ----------------------------------------------------
// 2. GENERATE MARKDOWN SECTION 3
// ----------------------------------------------------

let mdContent = `## 3. CatÃ¡logo de Locaciones (Venues) y Paquetes por Bloque

A continuaciÃ³n se detalla toda la informaciÃ³n comercial estructurada por **bloque de locaciÃ³n**. Para cada locaciÃ³n se describe su ficha tÃ©cnica y se desglosa el paquete asociado en detalle completo, siguiendo la estructura oficial de la empresa.

`;

recintos.forEach(recinto => {
  mdContent += `### ${recinto.name}\n\n`;
  mdContent += `#### ðŸ›ï¸ Ficha TÃ©cnica del Venue\n`;
  mdContent += `*   **UbicaciÃ³n:** ${recinto.ubicacion.replace('<br>', ' ')}\n`;
  mdContent += `*   **Capacidad:** ${recinto.capacidad}\n`;
  mdContent += `*   **Estilo:** ${recinto.estilo}\n`;
  mdContent += `*   **Fortalezas:** ${recinto.fortalezas}\n`;
  mdContent += `*   **PÃ¡gina de Referencia:** [Enlace al sitio](${recinto.pagina})\n`;
  if (recinto.restricciones) {
    mdContent += `*   **Restricciones:** ${recinto.restricciones}\n`;
  }
  mdContent += `\n#### ðŸ“¦ Paquete(s) Asociado(s):\n\n`;

  recinto.packages.forEach(pkg => {
    mdContent += `##### ðŸŒŸ ${pkg.name}\n\n`;
    mdContent += `*   **âž¢ Estacionamiento**\n    ${pkg.estacionamiento}\n\n`;
    mdContent += `*   **âž¢ Hospedaje**\n    ${pkg.hospedaje}\n\n`;
    mdContent += `*   **âž¢ Suite nupcial**\n    ${pkg.suiteNupcial}\n\n`;
    mdContent += `*   **âž¢ Ãrea de jardÃ­n**\n    ${pkg.areaJardin}\n\n`;
    mdContent += `*   **âž¢ IluminaciÃ³n arquitectÃ³nica interior y exterior**\n    ${pkg.iluminacion}\n\n`;
    mdContent += `*   **âž¢ Ãrea Consagrada**\n    ${pkg.areaConsagrada}\n\n`;
    mdContent += `*   **âž¢ Ãrea techada**\n    ${pkg.areaTechada}\n\n`;
    mdContent += `*   **âž¢ Ãrea de cocina**\n    ${pkg.areaCocina}\n\n`;
    mdContent += `*   **âž¢ Uso del Recinto / Quinta**\n    ${pkg.usoRecinto}\n\n`;
    mdContent += `*   **La mejor manera de iniciar: Coctel de bienvenida**\n    ${pkg.coctel}\n\n`;
    mdContent += `*   **y Para Decorar y Ambientar: Montaje banquete**\n    ${pkg.montaje}\n\n`;
    mdContent += `*   **MenÃº de Banquete**\n    ${pkg.menu.replace(/<br>/g, '\n    ')}\n\n`;
    mdContent += `*   **MenÃº Infantil**\n    ${pkg.menuInfantil}\n\n`;
    mdContent += `*   **Mezcladores Disponibles**\n    ${pkg.mezcladores}\n\n`;
    mdContent += `*   **Equipo de Servicio**\n    ${pkg.equipo}\n\n`;
    mdContent += `*   **Servicios de DJ Profesional**\n    ${pkg.dj}\n\n`;
    mdContent += `*   **Servicios Complementarios: CortesÃ­as Incluidas**\n    ${pkg.cortesias}\n\n`;
    mdContent += `*   **DuraciÃ³n del Servicio**\n    ${pkg.duracion}\n\n`;
    mdContent += `*   **Detalles del Servicio**\n    ${pkg.detalles}\n\n`;
    mdContent += `*   **Compromiso de Calidad**\n    ${pkg.calidad}\n\n`;
    mdContent += `*   **CotizaciÃ³n de Costos (Precios por Persona)**\n    ${pkg.costos.replace(/<br>/g, '\n    ')}\n\n`;
    if (pkg.cortesiasAdic) {
      mdContent += `*   **CortesÃ­as Adicionales**\n    ${pkg.cortesiasAdic.replace(/<br>/g, '\n    ')}\n\n`;
    }
    mdContent += `*   **Condiciones**\n    ${pkg.condiciones}\n\n`;
    mdContent += `*   **Beneficios**\n    ${pkg.beneficios}\n\n`;
    mdContent += `*   **Opciones Adicionales**\n    ${pkg.opcionesAdic}\n\n`;
    mdContent += `*   **Requisitos**\n    ${pkg.requisitos}\n\n`;
    mdContent += `*   **Notas**\n    ${pkg.notas}\n\n`;
    mdContent += `*   **Nota Final**\n    ${pkg.notaFinal.replace(/<br>/g, '\n    ')}\n\n`;
    mdContent += `---\n\n`;
  });
});

// ----------------------------------------------------
// 3. GENERATE HTML SECTION 3
// ----------------------------------------------------

let htmlContent = `  <!-- SECCION 3 -->
  <div class="section" id="bloques-locaciones">
    <h2 class="section-title">3. CatÃ¡logo de Locaciones (Venues) y Paquetes por Bloque</h2>
    <p>A continuaciÃ³n se detallan las fichas comerciales de las 10 locaciones oficiales de Primavera Events Group, agrupando la informaciÃ³n del recinto y su(s) paquete(s) exclusivo(s) asociado(s).</p>
`;

recintos.forEach(recinto => {
  htmlContent += `    
    <!-- ${recinto.name.toUpperCase()} -->
    <div class="venue-block">
      <div class="venue-title">${recinto.name}</div>
      <p><strong>UbicaciÃ³n:</strong> ${recinto.ubicacion}</p>
      <p><strong>Capacidad:</strong> ${recinto.capacidad}</p>
      <p><strong>Estilo:</strong> ${recinto.estilo}</p>
      <p><strong>Fortalezas:</strong> ${recinto.fortalezas}</p>
      <p><strong>PÃ¡gina de Referencia:</strong> <a href="${recinto.pagina}" target="_blank">Enlace al sitio</a></p>
`;
  if (recinto.restricciones) {
    htmlContent += `      <p><strong>Restricciones:</strong> ${recinto.restricciones}</p>\n`;
  }

  recinto.packages.forEach(pkg => {
    htmlContent += `
      <div class="package-box">
        <h4>ðŸŒŸ ${pkg.name}</h4>
        <p><strong>âž¢ Estacionamiento:</strong> ${pkg.estacionamiento}</p>
        <p><strong>âž¢ Hospedaje:</strong> ${pkg.hospedaje}</p>
        <p><strong>âž¢ Suite nupcial:</strong> ${pkg.suiteNupcial}</p>
        <p><strong>âž¢ Ãrea de jardÃ­n:</strong> ${pkg.areaJardin}</p>
        <p><strong>âž¢ IluminaciÃ³n arquitectÃ³nica:</strong> ${pkg.iluminacion}</p>
        <p><strong>âž¢ Ãrea Consagrada:</strong> ${pkg.areaConsagrada}</p>
        <p><strong>âž¢ Ãrea techada:</strong> ${pkg.areaTechada}</p>
        <p><strong>âž¢ Ãrea de cocina:</strong> ${pkg.areaCocina}</p>
        <p><strong>âž¢ Uso del Recinto / Quinta:</strong> ${pkg.usoRecinto}</p>
        <p><strong>La mejor manera de iniciar (Coctel):</strong> ${pkg.coctel}</p>
        <p><strong>y Para Decorar y Ambientar (Montaje):</strong> ${pkg.montaje}</p>
        <p><strong>MenÃº de Banquete:</strong> ${pkg.menu}</p>
        <p><strong>MenÃº Infantil:</strong> ${pkg.menuInfantil}</p>
        <p><strong>Mezcladores Disponibles:</strong> ${pkg.mezcladores}</p>
        <p><strong>Equipo de Servicio:</strong> ${pkg.equipo}</p>
        <p><strong>DJ Profesional:</strong> ${pkg.dj}</p>
        <p><strong>CortesÃ­as Incluidas:</strong> ${pkg.cortesias}</p>
        <p><strong>DuraciÃ³n del Servicio:</strong> ${pkg.duracion}</p>
        <p><strong>Detalles del Servicio:</strong> ${pkg.detalles}</p>
        <p><strong>Compromiso de Calidad:</strong> ${pkg.calidad}</p>
        <p><strong>CotizaciÃ³n de Costos (Persona):</strong><br>${pkg.costos}</p>
`;
    if (pkg.cortesiasAdic) {
      htmlContent += `        <p><strong>CortesÃ­as Adicionales:</strong><br>${pkg.cortesiasAdic}</p>\n`;
    }
    htmlContent += `        <p><strong>Condiciones:</strong> ${pkg.condiciones}</p>
        <p><strong>Beneficios:</strong> ${pkg.beneficios}</p>
        <p><strong>Opciones Adicionales:</strong> ${pkg.opcionesAdic}</p>
        <p><strong>Requisitos:</strong> ${pkg.requisitos}</p>
        <p><strong>Notas:</strong> ${pkg.notas}</p>
        <p><strong>Nota Final:</strong><br>${pkg.notaFinal}</p>
      </div>
`;
  });

  htmlContent += `    </div>\n`;
});

htmlContent += `  </div>`;

// ----------------------------------------------------
// 4. PERFORM REPLACEMENTS IN MD AND HTML FILES
// ----------------------------------------------------

// Read MD file
let mdData = fs.readFileSync(mdPath, 'utf8');
const mdStartAnchor = '## 3. CatÃ¡logo de Locaciones (Venues) y Paquetes por Bloque';
const mdEndAnchor = '## 4. CatÃ¡logo de Paquetes de GraduaciÃ³n';

const mdStartIndex = mdData.indexOf(mdStartAnchor);
const mdEndIndex = mdData.indexOf(mdEndAnchor);

if (mdStartIndex !== -1 && mdEndIndex !== -1) {
  const newMdData = mdData.substring(0, mdStartIndex) + mdContent + mdData.substring(mdEndIndex);
  fs.writeFileSync(mdPath, newMdData, 'utf8');
  console.log('Markdown playbook successfully updated!');
} else {
  console.error('Error finding anchors in Markdown file:', { mdStartIndex, mdEndIndex });
}

// Read HTML file
let htmlData = fs.readFileSync(htmlPath, 'utf8');
const htmlStartAnchor = '  <!-- SECCION 3 -->';
const htmlEndAnchor = '  <!-- SECCION 4 -->';

const htmlStartIndex = htmlData.indexOf(htmlStartAnchor);
const htmlEndIndex = htmlData.indexOf(htmlEndAnchor);

if (htmlStartIndex !== -1 && htmlEndIndex !== -1) {
  // We want to keep the page break before section 4, let's check what's there
  // The htmlEndAnchor should be preceded by <div class="page-break"></div> or similar.
  // Let's replace exactly from htmlStartAnchor to the start of section 4, but leaving page-break
  const newHtmlData = htmlData.substring(0, htmlStartIndex) + htmlContent + '\n\n  <div class="page-break"></div>\n\n' + htmlData.substring(htmlEndIndex);
  fs.writeFileSync(htmlPath, newHtmlData, 'utf8');
  console.log('HTML playbook successfully updated!');
} else {
  console.error('Error finding anchors in HTML file:', { htmlStartIndex, htmlEndIndex });
}

