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
    fortalezas: "Gran salón climatizado, área infantil con juegos fijos, estacionamiento interno para 35 autos, cocina profesional gigante y baños múltiples de lujo.",
    pagina: "https://primaveraeventsgroup.com/centro-de-convenciones-presidente/",
    restricciones: "Cierre de evento a las 00:00 AM (Gobernador) o 01:00 AM (Presidente).",
    packages: [
      {
        name: "Paquete Gobernador",
        estacionamiento: "Capacidad para 35 vehículos compactos en estacionamiento interno vigilado.",
        hospedaje: "No disponible en el recinto. Se cuenta con convenios especiales con hoteles de Cuernavaca (a 5-10 minutos).",
        suiteNupcial: "No disponible en el recinto. Se puede gestionar suite externa en hotel asociado con costo preferencial.",
        areaJardin: "Jardín ornamental de bienvenida con fuente artificial iluminada en la entrada principal.",
        iluminacion: "Iluminación arquitectónica básica en la fachada y luces decorativas en el acceso principal.",
        areaConsagrada: "No disponible dentro del recinto. Se recomienda realizar ceremonias en iglesias cercanas de Cuernavaca.",
        areaTechada: "Salón principal techado y climatizado para albergar un máximo de 500 personas con estilo modernista y elegante.",
        areaCocina: "Cocina profesional gigante y área para banquete de gran escala.",
        usoRecinto: "Uso del salón por 8 horas operativas (total 9 horas de servicio continuas de staff).",
        coctel: "Coctel de bienvenida con periqueras altas, salas lounge y sombrillas. Incluye margaritas de sabores sin alcohol (2 sabores), agua fresca (2 sabores) y crudités (pepino, jícama y zanahoria con miguelito y chamoy).",
        montaje: "Mesa principal de honor con sillón o sillones, templete de madera y centro de mesa floral natural. Centros de mesa florales naturales (redondos/altos/bajos). Mesas redondas o cuadradas con mantelería fina (mantel blanco, camino y servilletas de tela a elegir). Sillas Tiffany blancas. Plato base (variados modelos), loza blanca, cubertería fina plateada y cristalería clásica.",
        menu: "Banquete formal a 3 tiempos:<br>• **Primer Tiempo (Entrada):** Deliciosas ensaladas frescas o cremosas sopas.<br>• **Segundo Tiempo (Plato Fuerte):** Exquisitas opciones de pollo o cerdo, acompañadas de dos guarniciones a elegir, pan y chiles al centro.<br>• **Tercer Tiempo (Tornafiesta):** Barra de esquites o chilaquiles servidos en desechables (calculado al 60% de invitados).",
        menuInfantil: "Menú infantil opcional disponible a solicitud ($220.00 MXN extra por niño) con tiritas de milanesa, hamburguesas o nuggets con papas y espagueti.",
        mezcladores: "Servicio completo de mezcladores: hielo en cubos ilimitado, agua natural, refrescos de la línea Coca-Cola (sabores, mineral, clásica), limón y sal.",
        equipo: "Coordinador General del evento, Hostess de recepción, Meseros capacitados (1 cada 15-20 invitados), Personal de barra, Stewart de limpieza y Personal de mantenimiento de baños.",
        dj: "DJ profesional con cabina, audio de alta fidelidad, iluminación robótica móvil, pantalla con proyector, globos, pulseras neón y collares hawaianos (corbatas/velos en bodas), micrófonos inalámbricos, láser y máquina de humo.",
        cortesias: "Degustación para 4 personas al firmar. Letras decorativas gigantes 'XV' o 'LOVE', corazón rojo iluminado, mesas especiales de pastel y regalos, detonación de 2 chisperos, alfombra roja de entrada, espejo selfie y barra mix con 12 toppings dulces/salados.",
        duracion: "9 horas continuas totales de servicio.",
        detalles: "Coordinación y planeación integral de la logística del evento desde la recepción hasta el cierre.",
        calidad: "Compromiso de alta calidad de alimentos y servicio garantizado por contrato.",
        costos: "• **100 – 149 personas:** $899.00 MXN por persona<br>• **150 – 199 personas:** $849.00 MXN por persona<br>• **200 – 299 personas:** $799.00 MXN por persona<br>• **300 – 400 personas:** $749.00 MXN por persona<br>• **401+ personas:** Consultar tarifa personalizada.",
        cortesiasAdic: "Degustación de platillos y decoración básica del salón.",
        condiciones: "Se requiere un depósito de apartado para reservar la fecha y firma de contrato.",
        beneficios: "Atención personalizada de los Wedding Planners oficiales de Primavera Events Group.",
        opcionesAdic: "Montaje de ceremonia en el área de jardín ornamental ($3,500.00 MXN) y Barra de bebidas premium.",
        requisitos: "Confirmación final de invitados (10 días antes) y selección de menú y decoración.",
        notas: "Precios NO incluyen impuestos (IVA del 16% si se requiere factura). Se aplican tarifas adicionales por servicios extra o tiempo extra.",
        notaFinal: "Degustación exclusiva para 4 personas al firmar el contrato. Diseño de montaje de acuerdo a la paleta de colores. Croquis detallado de invitados. Minuto a minuto detallado del evento. Chat de coordinación exclusivo. Planner Richard Hernández y Gerente Rubí Alvarado (Tels: 2711148997 - 7774587923)."
      },
      {
        name: "Paquete Presidente",
        estacionamiento: "Capacidad para 35 vehículos compactos en estacionamiento interno vigilado.",
        hospedaje: "No disponible en el recinto. Se cuenta con convenios especiales con hoteles de Cuernavaca (a 5-10 minutos).",
        suiteNupcial: "No disponible en el recinto. Se puede gestionar suite externa en hotel asociado con costo preferencial.",
        areaJardin: "Jardín ornamental de bienvenida con fuente artificial iluminada en la entrada principal.",
        iluminacion: "Iluminación arquitectónica básica en la fachada y luces decorativas en el acceso principal.",
        areaConsagrada: "No disponible dentro del recinto. Se recomienda realizar ceremonias en iglesias cercanas de Cuernavaca.",
        areaTechada: "Salón principal techado y climatizado para albergar un máximo de 500 personas con estilo modernista y elegante.",
        areaCocina: "Cocina profesional gigante y área para banquete de gran escala.",
        usoRecinto: "Uso del salón por 9 horas operativas.",
        coctel: "Coctel de bienvenida premium extendido con periqueras altas, salas lounge y sombrillas. Incluye margaritas de sabores sin alcohol (2 sabores), piñadas sin alcohol, mojitos sin alcohol, agua fresca (2 sabores) y crudités (pepino, jícama y zanahoria con miguelito y chamoy).",
        montaje: "Mesa principal de honor con sillones imperiales Rey & Reyna, templete de madera y centro de mesa floral natural. Centros de mesa florales naturales (redondos/altos/bajos). Bases de metal altas para centros de mesa. Mesas tipo mármol cuadradas para 10 personas o redondas para 10-12 personas con sillas Tiffany blancas. Mantelería fina (mantel blanco, camino y servilletas de tela a elegir). Plato base (variados modelos), loza blanca, cubertería fina plateada o dorada y cristalería fina.",
        menu: "Banquete formal a 4 tiempos:<br>• **Primer Tiempo (Entrada):** Deliciosas crepas, frescas ensaladas o cremosas sopas.<br>• **Segundo Tiempo (Plato Fuerte):** Exquisitas opciones de pollo o cerdo, acompañadas de dos guarniciones a elegir, pan y chiles al centro.<br>• **Tercer Tiempo (Postre):** Selección de postres de repostería fina o de autor.<br>• **Cuarto Tiempo (Tornafiesta):** Barra de esquites o chilaquiles servidos en desechables (calculado al 60% de invitados).",
        menuInfantil: "Menú infantil opcional disponible a solicitud ($220.00 MXN extra por niño) con tiritas de milanesa, hamburguesas o nuggets con papas y espagueti.",
        mezcladores: "Servicio completo de mezcladores: hielo en cubos ilimitado, agua natural, refrescos de la línea Coca-Cola (sabores, mineral, clásica), limón y sal.",
        equipo: "Coordinador General del evento, Capitán de Meseros, Hostess de recepción, Meseros capacitados (1 cada 15-20 invitados), Personal de barra, Stewart de limpieza y Personal de mantenimiento de baños.",
        dj: "DJ profesional con cabina, audio de alta fidelidad, iluminación robótica móvil, pantalla con proyector, globos, pulseras neón y collares hawaianos (corbatas/velos en bodas), micrófonos inalámbricos, láser, máquina de humo, pista pixel de baile 5x5m y 2 chisperos a control remoto.",
        cortesias: "Degustación para 4 personas al firmar. Letras decorativas gigantes 'XV' o 'LOVE', corazón rojo iluminado, mesas especiales de pastel y regalos, detonación de 2 chisperos, alfombra roja de entrada, espejo selfie, barra mix con 12 toppings dulces/salados y opción de montaje de ceremonia con mobiliario elegante.",
        duracion: "9 horas continuas totales de servicio.",
        detalles: "Coordinación y planeación integral de la logística del evento desde la recepción hasta el cierre.",
        calidad: "Compromiso de alta calidad de alimentos y servicio garantizado por contrato.",
        costos: "• **130 – 149 personas:** $899.00 MXN por persona<br>• **150 – 199 personas:** $849.00 MXN por persona<br>• **200 – 299 personas:** $799.00 MXN por persona<br>• **300 – 400 personas:** $749.00 MXN por persona<br>• **401+ personas:** Consultar tarifa personalizada.",
        cortesiasAdic: "Degustación de platillos y decoración básica del salón.",
        condiciones: "Se requiere un depósito de apartado para reservar la fecha y firma de contrato.",
        beneficios: "Atención personalizada de los Wedding Planners oficiales de Primavera Events Group.",
        opcionesAdic: "Montaje de ceremonia en el área de jardín ornamental (incluido en cortesía) y Barra de bebidas premium.",
        requisitos: "Confirmación final de invitados (10 días antes) y selección de menú y decoración.",
        notas: "Precios NO incluyen impuestos (IVA del 16% si se requiere factura). Se aplican tarifas adicionales por servicios extra o tiempo extra.",
        notaFinal: "Degustación exclusiva para 4 personas al firmar el contrato. Diseño de montaje de acuerdo a la paleta de colores. Croquis detallado de invitados. Minuto a minuto detallado del evento. Chat de coordinación exclusivo. Planner Richard Hernández y Gerente Rubí Alvarado (Tels: 2711148997 - 7774587923)."
      }
    ]
  },
  {
    id: "bloque-2",
    name: "Bloque 2: Quinta Zarabanda",
    ubicacion: "Avenida Lauro Ortega Martínez #4, Las Animas, 62583 Temixco, Morelos.",
    capacidad: "100 a 250 personas en área techada.",
    estilo: "Finca campestre natural de alto confort, rodeada de abundante flora y áreas de descanso.",
    fortalezas: "Suite nupcial de lujo con jacuzzi y vestidor. Hospedaje interno climatizado para 14 personas con alberca privada y cocina. Área consagrada para ceremonias. Uso completo por 10 horas sin restricciones de horario.",
    pagina: "https://primaveraeventsgroup.com/quinta-zarabanda/",
    restricciones: "Ninguna. 10 horas de servicio continuo sin restricción de horario nocturno.",
    packages: [
      {
        name: "Paquete Armonía",
        estacionamiento: "Amplia capacidad con servicio de Valet Parking incluido.",
        hospedaje: "Espacio privado con capacidad para 14 personas. Cuenta con cocina, baños, área de jardín, alberca privada, habitaciones amplias con aire acondicionado y estacionamiento propio (costo adicional por estancia).",
        suiteNupcial: "Espacio exclusivo con jacuzzi, vestidor, tocador elegante y romántico diseñado para brindar confort y privacidad en ese día especial (habitación incluida para novios).",
        areaJardin: "Jardines amplios y maduros con fuente artificial iluminada en la entrada principal.",
        iluminacion: "Diseño de luz arquitectónica interior y exterior que realza la belleza de cada espacio, resaltando detalles tanto en interiores como en exteriores.",
        areaConsagrada: "Espacio íntimo y armonioso, ideal para ceremonias y momentos especiales en un entorno natural y lleno de paz.",
        areaTechada: "Salón abierto cubierto con capacidad para albergar hasta 250 personas, con estilo arquitectónico modernista y elegante.",
        areaCocina: "Amplia y funcional cocina equipada para el servicio de banquetes.",
        usoRecinto: "10 horas de servicio continuo sin restricción de horario.",
        coctel: "Coctel de bienvenida con periqueras altas, salas lounge y sombrillas. Incluye margaritas de sabores servidas en copa flauta sin alcohol, agua fresca de fruta natural, crudités (pepino, jícama y zanahoria con miguelito y chamoy), mojito sin alcohol y piñada sin alcohol.",
        montaje: "Mesa principal con sillones imperiales Rey & Reyna. Arreglo natural para centro de mesa con elegante flor natural de temporada (diseños redondos, altos y bajos). Mesa redonda para 8 o 10 personas con silla Tiffany blanca. Mesa cuadrada de 10 a 12 personas con mantel blanco. Mesa Campirana de 10 a 12 personas (rectangular de madera con silla crossback, Tiffany blanca, boss o lotus). Mesa tipo mármol para 10 a 12 personas (rectangular con acabado tipo mármol con combinación de sillas). Mantelería de tela (mantel, camino y servilleta) en el color de su elección. Plato base (varios modelos), loza blanca de alta calidad, cubertería fina (plata, dorado y gold rose) y cristalería (copas transparentes y de color, vaso cubero y tequilero).",
        menu: "Banquete formal a 3 tiempos:<br>• **Primer Tiempo (Entradas):** Frescas ensaladas o deliciosas cremas ideales para iniciar tu experiencia gastronómica.<br>• **Segundo Tiempo (Plato Fuerte):** Exquisitas opciones de pollo o cerdo, acompañadas de dos guarniciones a elegir, pan y chiles al centro.<br>• **Tercer Tiempo (Tornafiesta):** Barra de esquites o chilaquiles servidos en desechables (calculado al 60% de invitados).",
        menuInfantil: "Menú infantil completo incluido con tiritas de milanesa, hamburguesa o nuggets de pollo acompañadas de espagueti, papas a la francesa y una golosina sorpresa.",
        mezcladores: "Nuestra oferta de mezcladores incluye un servicio completo de hielo en cubos, agua natural y una variedad de refrescos de la línea Coca-Cola (manzana, toronja, agua mineral y la clásica Coca-Cola, además de limón y sal).",
        equipo: "Coordinador General, Capitán de Meseros, Hostess de bienvenida, Meseros capacitados para el servicio, Personal de barra y Personal de baños.",
        dj: "DJ profesional con amplia experiencia. Incluye mampara DJ, audio e iluminación de alta calidad, torres iluminadas con cabezas robóticas, pantalla con proyector, globos multicolores, collares hawaianos (corbatas y velos para boda), lámpara led wash, micrófono inalámbrico, tramoya para iluminación y máquina de humo.",
        cortesias: "Letras decorativas a elegir 'XV' o 'LOVE', corazón rojo decorativo iluminado, mesa especial para pastel, mesa especial para regalos, detonación de dos chisperos de pirotecnia en frío y alfombra roja para la entrada.",
        duracion: "10 horas continuas de servicio.",
        detalles: "La planificación y ejecución de su evento incluye un servicio integral que cubre desde la llegada de los invitados hasta el final de la celebración.",
        calidad: "Nos comprometemos a ofrecer un servicio de alta calidad, asegurando que cada evento sea único y memorable.",
        costos: "• **100 – 150 personas:** $1,700.00 MXN por persona<br>• **151 – 250 personas:** $1,450.00 MXN por persona",
        cortesiasAdic: "Pista pixel LED 5x5m de cortesía.<br>A elegir 2 opciones adicionales: Pista pixel, cabina 360 o robot leds.",
        condiciones: "Se requiere un depósito de apartado para reservar la fecha.",
        beneficios: "Atención personalizada y coordinación integral del evento.",
        opcionesAdic: "Montaje de ceremonia en el área consagrada y barra de bebidas premium.",
        requisitos: "Confirmación de invitados y selección de menú.",
        notas: "Los precios NO incluyen impuestos. Se aplican tarifas adicionales por servicios extra.",
        notaFinal: "Al firmar el contrato: Degustación exclusiva (4 personas), diseño de montaje de acuerdo a la paleta de colores, croquis de distribución detallada de invitados, minuto a minuto (cronograma detallado del evento) y chat exclusivo de comunicación directa. Planner Richard Hernández y C.P. Jessica Rodríguez (Tels: 7774587923 - 7773012421)."
      }
    ]
  },
  {
    id: "bloque-3",
    name: "Bloque 3: Finca Las Isabeles",
    ubicacion: "Xochitepec, Morelos.",
    capacidad: "200 a 400 invitados.",
    estilo: "Finca campestre rústica elegante tropical rodeada de abundante naturaleza.",
    fortalezas: "Áreas verdes rodeadas de palmeras exóticas, salón abierto cubierto ideal para climas cálidos y alberca iluminada.",
    pagina: "https://primaveraeventsgroup.com/finca-las-isabeles/",
    restricciones: "Ninguna. 10 horas de servicio sin restricción de horario nocturno.",
    packages: [
      {
        name: "Paquete Nature's Majesty",
        estacionamiento: "Amplia capacidad para autos con servicio de valet parking incluido.",
        hospedaje: "Disfrute de una estancia cómoda y tranquila en nuestras cabañas, diseñadas para brindar descanso, privacidad y un ambiente acogedor en medio de la naturaleza. Ideal para complementar su evento o prolongar la experiencia con una noche especial (Previa reserva y costo adicional).",
        suiteNupcial: "Espacio exclusivo en un ambiente romántico para ese día tan especial (habitación incluida para los novios).",
        areaJardin: "Variedad de escenarios naturales y elegantes con cascada e iluminación.",
        iluminacion: "Diseño de luz arquitectónica interior y exterior que realza la belleza de cada espacio, creando ambientes sofisticados y resaltando detalles tanto en interiores como en exteriores.",
        areaConsagrada: "Espacio íntimo y armonioso, ideal para ceremonias y momentos especiales en un entorno natural y lleno de paz.",
        areaTechada: "Salón abierto para albergar un máximo de 400 personas, de estilo arquitectónico modernista y elegante.",
        areaCocina: "Amplia y funcional área de cocina para preparación culinaria.",
        usoRecinto: "Uso de la Quinta por 10 Horas de servicio sin restricción de horario.",
        coctel: "Coctel de bienvenida con periqueras altas, salas lounge y sombrillas. Incluye margaritas de sabores servidas en copa flauta sin alcohol, agua fresca de fruta natural, crudités (pepino, jícama y zanahoria con miguelito y chamoy), mojito sin alcohol y piñada (sin alcohol).",
        montaje: "Mesa principal con sillones Rey & Reyna (mesa de honor equipada con sillones, templete de madera y back decorado con luces vintage y telas). Arreglo natural para centro de mesa con flor de temporada. Mesa redonda para 8 o 10 personas con silla Tiffany blanca. Mesa cuadrada de 10 a 12 personas con mantel blanco. Mesa Campirana de 10 a 12 personas (rectangular de madera con silla crossback, Tiffany blanca, boss o lotus). Mesa tipo mármol para 10 a 12 personas (rectangular con acabado tipo mármol con combinación de sillas). Mantelería de tela (mantel, camino y servilleta) en el color de su elección. Plato base (varios modelos), loza blanca de alta calidad, cubertería fina plateada o dorada/gold rose y cristalería fina.",
        menu: "Banquete formal a 3 tiempos:<br>• **Primer Tiempo (Entradas):** Frescas ensaladas o deliciosas cremas ideales para iniciar tu experiencia gastronómica.<br>• **Segundo Tiempo (Plato Fuerte):** Exquisitas opciones de pollo o cerdo, acompañadas de dos guarniciones a elegir, pan y chiles al centro de la mesa.<br>• **Tercer Tiempo (Tornafiesta):** Barra de esquites o chilaquiles servidos en desechables para cerrar con broche de oro (se considera al 60% de invitados).",
        menuInfantil: "Menú Infantil completo incluido con tiritas de milanesa, hamburguesa o nuggets de pollo acompañadas de espagueti, papas a la francesa y una golosina sorpresa.",
        mezcladores: "Nuestra oferta de mezcladores incluye un servicio completo de hielo en cubos, agua natural y una variedad de refrescos de la línea Coca-Cola (manzana, toronja, agua mineral y la clásica Coca-Cola, además de limón y sal).",
        equipo: "Coordinador General, Capitán de Meseros, Hostess de bienvenida, Meseros capacitados para el servicio de alimentos y bebidas, Personal de barra y Personal de baños.",
        dj: "DJ profesional con amplia experiencia. Incluye mampara DJ, audio e iluminación de alta calidad, torres iluminadas con cabezas robóticas, pantalla con proyector, globos multicolores, collares hawaianos (corbatas y velos para boda), lámpara led wash, micrófono inalámbrico, tramoya para iluminación y máquina de humo.",
        cortesias: "Letras decorativas a elegir 'XV' o 'LOVE', corazón rojo decorativo iluminado, mesa especial para pastel, mesa especial para regalos, detonación de dos chisperos de pirotecnia en frío y alfombra roja para la entrada.",
        duracion: "10 horas continuas de servicio.",
        detalles: "La planificación y ejecución de su evento incluye un servicio integral que cubre desde la llegada de los invitados hasta el final de la celebración.",
        calidad: "Nos comprometemos a ofrecer un servicio de alta calidad, asegurando que cada evento sea único y memorable.",
        costos: "• **100 – 200 personas:** $1,999.00 MXN por persona<br>• **201 – 300 personas:** $1,899.00 MXN por persona<br>• **301 – 400 personas:** $1,799.00 MXN por persona",
        cortesiasAdic: "• **Escala 100-200 px:** Pista leds 5x5m de cortesía.<br>• **Escala 201-300 px:** A elegir 2 opciones: pista leds 5x5, cabina 360, robot leds o show men performance.<br>• **Escala 301-400 px:** A elegir 3 opciones: pista leds 5x5, cabina 360, robot leds o show men performance.",
        condiciones: "Se requiere un depósito de apartado para reservar la fecha.",
        beneficios: "Atención personalizada y coordinación integral del evento por parte de Primavera Events Group.",
        opcionesAdic: "Montaje de ceremonia en el área consagrada y barra de bebidas premium.",
        requisitos: "Confirmación de invitados y selección de menú.",
        notas: "Los precios NO incluyen impuestos. Se aplican tarifas adicionales por servicios extra.",
        notaFinal: "Al firmar el contrato: Degustación exclusiva (4 personas), diseño de montaje de acuerdo a la paleta de colores, croquis de distribución, minuto a minuto (cronograma detallado) y chat exclusivo de comunicación. Responsables: Jessy y Richard (Tels: 7774587923 - 7773012421)."
      }
    ]
  },
  {
    id: "bloque-4",
    name: "Bloque 4: Jardín La Flor",
    ubicacion: "Privada las Fuentes s/n, San Gaspar, Jiutepec, Morelos.",
    capacidad: "100 a 300 invitados.",
    estilo: "Jardín clásico de Cuernavaca, fresco, romántico e íntimo.",
    fortalezas: "Explanada para montajes con cascada monumental de bienvenida con iluminación y área consagrada para ceremonias al aire libre.",
    pagina: "https://primaveraeventsgroup.com/jardin-la-flor/",
    restricciones: "Cierre de música a la 01:00 AM.",
    packages: [
      {
        name: "Paquete Esencia Floral",
        estacionamiento: "Amplio estacionamiento interno que alberga hasta 60 autos de forma segura.",
        hospedaje: "No disponible en el recinto. Convenios con hoteles cercanos en Jiutepec.",
        suiteNupcial: "Área de camerino o suite privada de preparación disponible para los anfitriones.",
        areaJardin: "Entorno natural y jardín plano con abundante vegetación que aporta frescura y amplitud.",
        iluminacion: "Iluminación perimetral decorativa y hermosa cascada iluminada rodeada de vegetación natural.",
        areaConsagrada: "Área consagrada destinada a ceremonias religiosas con solemnidad en un ambiente íntimo y espiritual.",
        areaTechada: "Salón techado y abierto para albergar un máximo de 200 personas, con estilo arquitectónico modernista y elegante.",
        areaCocina: "Amplia y funcional cocina equipada para catering profesional.",
        usoRecinto: "Uso del salón por 8 horas (servicio disponible hasta la 01:00 AM).",
        coctel: "Coctel de bienvenida con periqueras altas, salas lounge y sombrillas. Incluye margaritas de sabores sin alcohol (2 sabores), piñadas sin alcohol, mojitos sin alcohol, agua fresca (2 sabores) y crudités (pepino, jícama y zanahoria con miguelito y chamoy).",
        montaje: "Mesa principal de honor con sillones Rey & Reyna, templete de madera, back con luces vintage y telas, y centro floral natural. Arreglo natural para centro de mesa (diseños redondos, largos y altos con flor de temporada). Mesa redonda para 8 o 10 personas con silla Tiffany blanca. Mesa cuadrada de 10 a 12 personas con mantel blanco. Mesa Campirana de 10 a 12 personas (rectangular de madera con silla crossback, Tiffany blanca, boss o lotus). Mesa tipo mármol para 10 a 12 personas (rectangular con acabado tipo mármol con combinación de sillas). Mantelería, plato base (varios modelos), loza blanca de alta calidad, cubertería fina en tonos plata/dorado/gold rose y cristalería fina.",
        menu: "Banquete formal a 4 tiempos:<br>• **Primer Tiempo (Entrada):** Frescas ensaladas o deliciosas cremas cremosas para iniciar.<br>• **Segundo Tiempo (Plato Fuerte):** Exquisitas opciones de pollo o cerdo, acompañadas de dos guarniciones a elegir, pan y chiles al centro de la mesa.<br>• **Tercer Tiempo (Tornafiesta):** Barra de esquites o chilaquiles servidos en desechables (calculado al 60% de invitados).<br>• **Cuarto Tiempo (Postre):** Selección de postres finos de autor.",
        menuInfantil: "Menú infantil completo incluido con tiritas de milanesa, hamburguesa o nuggets de pollo acompañadas de espagueti, papas a la francesa y una golosina sorpresa.",
        mezcladores: "Servicio completo de mezcladores: hielo en cubos, agua natural y refrescos de la línea Coca-Cola (sabores, mineral, clásica), limón y sal.",
        equipo: "Coordinador General, Capitán de Meseros, Hostess de bienvenida, Meseros capacitados, Personal de barra, Cocineros profesionales, Personal de mantenimiento de sanitarios.",
        dj: "DJ profesional con mampara moderna, audio e iluminación de alta calidad, torres iluminadas con cabezas robóticas, pantalla con proyector, globos multicolores, pulseras neón y collares hawaianos (corbatas y velos para boda), 2 chisperos a control remoto, micrófonos inalámbricos, láser y máquina de humo.",
        cortesias: "Letras decorativas a elegir 'XV' o 'LOVE', corazón rojo decorativo iluminado, mesa especial para pastel, mesa especial para regalos, detonación de dos chisperos de pirotecnia en frío y alfombra roja.",
        duracion: "8 horas de servicio continuo.",
        detalles: "La planificación y ejecución de su evento incluye un servicio de planeación integral paso a paso.",
        calidad: "Compromiso de alta calidad de alimentos y servicio garantizado por la firma Primavera Events Group.",
        costos: "• **100 – 199 personas:** $999.00 MXN por persona<br>• **200 – 300 personas:** $899.00 MXN por persona",
        cortesiasAdic: "Degustación de platillos, diseño de montaje y croquis de distribución de invitados.",
        condiciones: "Se requiere un depósito de apartado para reservar la fecha.",
        beneficios: "Atención personalizada de los Wedding Planners y Dirección Creativa de Primavera.",
        opcionesAdic: "Montaje de ceremonia en el área consagrada y barra de bebidas premium.",
        requisitos: "Confirmación final de invitados y selección de menú y decoración.",
        notas: "Precios NO incluyen impuestos (IVA). Se aplican tarifas adicionales por servicios extra.",
        notaFinal: "Al firmar el contrato: Degustación exclusiva (4 personas), diseño de montaje de acuerdo a la paleta de colores, croquis de distribución detallada de invitados, minuto a minuto y chat exclusivo de coordinación directa. Planner Richard Hernández y W.P. Jessica Rodríguez (Tels: 7774587923 / 7773012421)."
      }
    ]
  },
  {
    id: "bloque-5",
    name: "Bloque 5: Salón Los Potrillos",
    ubicacion: "Francisco I. Madero 23, Tepetzingo, 62767 Crucero Tezoyuca, Morelos.",
    capacidad: "100 a 500 invitados.",
    estilo: "Rústico ecuestre campirano tradicional estilo rancho elegante.",
    fortalezas: "Picadero visible para espectáculos de charros, gran calidez tradicional, área al aire libre con alberca y palapa gigante.",
    pagina: "https://primaveraeventsgroup.com/salon-los-potrillos/",
    restricciones: "Cierre de música a la 01:00 AM.",
    packages: [
      {
        name: "Paquete Linaje Pura Sangre",
        estacionamiento: "Amplio estacionamiento cerrado con capacidad para 100 vehículos compactos.",
        hospedaje: "No disponible en el recinto. Convenios con hoteles cercanos en Tezoyuca/Xochitepec.",
        suiteNupcial: "No disponible en el recinto. Se cuenta con camerino privado de uso básico.",
        areaJardin: "Área de jardín plano con puente rústico y fuente artificial en la entrada principal.",
        iluminacion: "Iluminación perimetral decorativa básica.",
        areaConsagrada: "No disponible dentro del recinto. Se recomienda realizar ceremonias en iglesias locales.",
        areaTechada: "Salón techado y abierto para albergar un máximo de 400 personas, con estilo modernista y elegante.",
        areaCocina: "Amplia y funcional área de cocina y baños múltiples para invitados.",
        usoRecinto: "Uso de salón por 8 Horas sin restricción de horario (tiempo extra disponible).",
        coctel: "Coctel de bienvenida con periqueras altas, salas lounge y sombrillas. Incluye margaritas de sabores sin alcohol (2 sabores), piñada sin alcohol, mojito sin alcohol, agua fresca (2 sabores) y crudités (pepino, jícama y zanahoria con miguelito y chamoy).",
        montaje: "Mesa principal de honor con sillón o sillones, templete de madera y centro de mesa floral natural de temporada. Arreglos naturales para centros de mesa (largo y redondo). Bases de metal altas para centros de mesa. Mesa tipo mármol cuadrada para 10 personas con silla Tiffany blanca. Mesa redonda para 10 o 12 personas con silla Tiffany blanca. Mantelería fina (mantel blanco, camino y servilleta de tela de color a elegir). Plato base (varios modelos), loza blanca, cubertería fina plateada o dorada y cristalería fina.",
        menu: "Banquete formal a 3 tiempos:<br>• **Primer Tiempo (Entradas):** Deliciosas crepas, frescas ensaladas o cremosas sopas.<br>• **Segundo Tiempo (Plato Fuerte):** Exquisitas opciones de pollo o cerdo, acompañadas de dos guarniciones a elegir, pan y chiles al centro de la mesa.<br>• **Tercer Tiempo (Tornafiesta):** Barra de esquites o chilaquiles servidos en desechables.",
        menuInfantil: "Menú infantil disponible bajo cotización separada ($220.00 MXN).",
        mezcladores: "Nuestra oferta de mezcladores incluye un servicio completo de hielo en cubos, agua natural y una variedad de refrescos de la línea Coca-Cola (manzana, toronja, agua mineral y la clásica Coca-Cola, además de limón y sal).",
        equipo: "Coordinador General, Capitán de Meseros, Hostess de bienvenida, Meseros capacitados, Personal de barra, Cocineros y Personal de baños.",
        dj: "DJ profesional con cabina, audio de alta fidelidad, iluminación robótica móvil, pantalla con proyector, globos, pulseras neón y collares hawaianos (corbatas/velos en bodas), 2 chisperos a control remoto, micrófonos inalámbricos, láser y máquina de humo.",
        cortesias: "Letras decorativas gigantes 'XV' o 'LOVE', corazón rojo decorativo, mesa especial para pastel, mesa especial para regalos, detonación de dos chisperos de pirotecnia en frío y alfombra roja.",
        duracion: "9 horas de servicio continuo.",
        detalles: "Logística y planeación integral de la boda o evento por parte de Primavera Events Group.",
        calidad: "Compromiso de alta calidad de alimentos y servicio garantizado por contrato.",
        costos: "• **100 – 199 personas:** $799.00 MXN por persona<br>• **200 – 299 personas:** $749.00 MXN por persona<br>• **300 – 399 personas:** $699.00 MXN por persona<br>• **400 – 500 personas:** $649.00 MXN por persona<br>• **501+ personas:** Consultar tarifa personalizada.",
        cortesiasAdic: "Degustación de platillos y decoración básica del salón.",
        condiciones: "Precios sujetos a cambios sin previo aviso. Se requiere depósito de reserva.",
        beneficios: "Atención personalizada y coordinación integral.",
        opcionesAdic: "Montaje de ceremonia al aire libre y barra de bebidas premium.",
        requisitos: "Confirmación de invitados y selección de menú.",
        notes: "Los precios NO incluyen impuestos. Se aplican tarifas adicionales por servicios extra.",
        notaFinal: "Al firmar el contrato: Degustación exclusiva (4 personas), diseño de montaje, croquis de distribución detallada de invitados, minuto a minuto y chat exclusivo de comunicación directa. Planner Richard Hernández y W.P. Jessica Rodríguez."
      }
    ]
  },
  {
    id: "bloque-6",
    name: "Bloque 6: Jardín Tsu Nuum",
    ubicacion: "Carretera a Aeropuerto de Cuernavaca, KM 0.5, Xochitepec, Morelos, México.",
    capacidad: "100 a 250 invitados.",
    estilo: "Zen moderno y minimalista con paisajismo internacional de autor.",
    fortalezas: "Alta privacidad, escenarios fotogénicos únicos y gran iluminación ambiental nocturna en los árboles maduros. Cercanía al aeropuerto de Cuernavaca y suite privada.",
    pagina: "https://primaveraeventsgroup.com/jardin-tsu-nuum/",
    restricciones: "Ninguna. 10 horas sin restricciones de horario nocturno.",
    packages: [
      {
        name: "Paquete Vuelo Esmeralda",
        estacionamiento: "Amplia capacidad de autos con servicio de valet parking incluido.",
        hospedaje: "Hotel con capacidad para 60 personas a tan solo 80 metros del jardín, reservación previa (costo adicional por estancia).",
        suiteNupcial: "Suite privada. Espacio íntimo y elegante diseñado para brindar confort, privacidad y un ambiente lleno de encanto. Ideal tanto para los novios como para quinceañeras, ofrece el escenario perfecto para relajarse, prepararse y culminar su celebración con una estancia especial.",
        areaJardin: "Jardines zen de diseño paisajista con abundante flora exótica y fuente artificial en la entrada principal.",
        iluminacion: "Diseño de luz arquitectónica interior y exterior que realza la belleza de cada espacio, creando ambientes sofisticados y resaltando detalles tanto en interiores como en exteriores.",
        areaConsagrada: "Espacio íntimo y armonioso, ideal para ceremonias y momentos especiales en un entorno natural y lleno de paz.",
        areaTechada: "Área techada para albergar hasta 250 personas, con estilo arquitectónico modernista y elegante.",
        areaCocina: "Amplia y funcional cocina equipada para el servicio de banquetes.",
        usoRecinto: "Uso de la locación por 10 Horas de servicio continuo sin restricción de horario.",
        coctel: "Coctel de bienvenida con periqueras altas, salas lounge y sombrillas. Incluye margaritas de sabores servidas en copa flauta sin alcohol, agua fresca de fruta natural, crudités (pepino, jícama y zanahoria con miguelito y chamoy), mojito sin alcohol y piñada (sin alcohol).",
        montaje: "Mesa principal con sillones Rey & Reyna (mesa de honor equipada con sillones, templete de madera y back decorado con luces vintage y telas). Arreglo natural para centro de mesa con elegante flor natural de temporada. Mesa redonda para 8 o 10 personas con silla Tiffany blanca. Mesa cuadrada de 10 a 12 personas con mantel blanco. Mesa Campirana de 10 a 12 personas (rectangular de madera con silla crossback, Tiffany blanca, boss o lotus). Mesa tipo mármol para 10 a 12 personas (rectangular con acabado tipo mármol con combinación de sillas). Mantelería de tela (mantel, camino y servilleta) en el color de su elección. Plato base (varios modelos), loza blanca de alta calidad, cubertería fina plateada o dorada/gold rose y cristalería fina.",
        menu: "Banquete formal a 3 tiempos:<br>• **Primer Tiempo (Entradas):** Frescas ensaladas o deliciosas cremas ideales para iniciar tu experiencia gastronómica.<br>• **Segundo Tiempo (Plato Fuerte):** Exquisitas opciones de pollo o cerdo, acompañadas de dos guarniciones a elegir, pan y chiles al centro de la mesa.<br>• **Tercer Tiempo (Tornafiesta):** Barra de esquites o chilaquiles servidos en desechables para cerrar con broche de oro (se considera al 60% de invitados).",
        menuInfantil: "Menú Infantil completo incluido con tiritas de milanesa, hamburguesa o nuggets de pollo acompañadas de espagueti, papas a la francesa y una golosina sorpresa.",
        mezcladores: "Nuestra oferta de mezcladores incluye un servicio completo de hielo en cubos, agua natural y una variedad de refrescos de la línea Coca-Cola (manzana, toronja, agua mineral y la clásica Coca-Cola, además de limón y sal).",
        equipo: "Coordinador General, Capitán de Meseros, Hostess de bienvenida, Meseros capacitados, Personal de barra y Personal de baños.",
        dj: "DJ profesional con amplia experiencia. Incluye mampara DJ, audio e iluminación de alta calidad, torres iluminadas con cabezas robóticas, pantalla con proyector, globos multicolores, collares hawaianos (corbatas y velos para boda), lámpara led wash, micrófono inalámbrico, tramoya para iluminación y máquina de humo.",
        cortesias: "Letras decorativas a elegir 'XV' o 'LOVE', corazón rojo decorativo iluminado, mesa especial para pastel, mesa especial para regalos, detonación de dos chisperos de pirotecnia en frío y alfombra roja.",
        duracion: "10 horas continuas de servicio.",
        detalles: "La planificación y ejecución de su evento incluye un servicio integral que cubre desde la llegada de los invitados hasta el final de la celebración.",
        calidad: "Nos comprometemos a ofrecer un servicio de alta calidad, asegurando que cada evento sea único y memorable.",
        costos: "• **100 – 150 personas:** $2,199.00 MXN por persona<br>• **151 – 200 personas:** $2,099.00 MXN por persona<br>• **201 – 250 personas:** $1,999.00 MXN por persona",
        cortesiasAdic: "Pista pixel LED 5x5m de cortesía.<br>• **Escala 151-200 px:** Elegir 1: pista pixel 5x5, robot leds, cabina 360 o barra mix con dulces y salados durante el coctel.<br>• **Escala 201-250 px:** Elegir 2: pista pixel 5x5, robot leds, cabina 360 o cabina inflable.",
        condiciones: "Firma de contrato y depósito para apartado de fecha.",
        beneficios: "Atención personalizada, Coordinación integral y Dirección Creativa Top-Tier.",
        opcionesAdic: "Montaje de ceremonia en el área consagrada y barra de bebidas premium.",
        requisitos: "Confirmación y entrega de lista de invitados.",
        notas: "Los precios NO incluyen impuestos. Se aplican tarifas adicionales por servicios extra. Todo lo anterior.",
        notaFinal: "Al firmar el contrato: Degustación exclusiva (4 personas), diseño de montaje de acuerdo a la paleta de colores, croquis de distribución, minuto a minuto y chat exclusivo de comunicación. Responsables: Jessy y Richard. Richard H (Founder & Creative Director) y Jessy R (Founder & Lead Planner) (Tels: 7774587923)."
      }
    ]
  },
  {
    id: "bloque-7",
    name: "Bloque 7: Salón Los Caballos",
    ubicacion: "Calle Zaragoza 1107, Ocotepec, Cuernavaca, Morelos.",
    capacidad: "100 a 300 invitados.",
    estilo: "Hacienda con establos elegantes de exhibición y cantera tallada.",
    fortalezas: "Gran capacidad logística, estacionamiento cerrado masivo e ideal para graduaciones y eventos masivos corporativos.",
    pagina: "https://primaveraeventsgroup.com/salon-los-caballos/",
    restricciones: "Cierre de música a la 01:00 AM.",
    packages: [
      {
        name: "Paquete Imperial Ecuestre",
        estacionamiento: "Amplio estacionamiento cerrado con capacidad para autos de los invitados.",
        hospedaje: "No disponible en el recinto. Convenios con hoteles cercanos en Cuernavaca norte.",
        suiteNupcial: "No disponible en el recinto. Se cuenta con camerino privado de uso básico.",
        areaJardin: "Área de jardín plano con fuente artificial en la entrada principal.",
        iluminacion: "Sistema de iluminación arquitectónica estratégica interna y externa que realza la arquitectura y detalles del espacio.",
        areaConsagrada: "No disponible dentro del recinto. Se recomienda realizar ceremonias en iglesias locales.",
        areaTechada: "Salón techado y cerrado para albergar un máximo de 300 personas, con estilo arquitectónico modernista y elegante.",
        areaCocina: "Amplia y funcional cocina equipada para el catering.",
        usoRecinto: "Uso del salón por 8 horas de servicio hasta la 01:00 am.",
        coctel: "Coctel de bienvenida con periqueras altas, salas lounge y sombrillas. Incluye margaritas de sabores servidas en copa flauta sin alcohol, agua fresca, crudités (pepino, jícama y zanahoria con miguelito y chamoy), mojito sin alcohol y piñada sin alcohol.",
        montaje: "Mesa principal de honor con sillón o sillones, templete de madera y centro de mesa floral natural. Arreglos naturales para centros de mesa. Bases de metal altas para centros de mesa. Montaje en mesa cuadrada y rectangular de madera con sillería Tiffany blanca o crossback. Mantelería fina (mantel blanco, camino y servilleta de tela de color a elegir). Plato base (varios modelos), loza blanca, cubertería fina plateada o dorada y cristalería fina.",
        menu: "Banquete formal a 4 tiempos:<br>• **Primer Tiempo (Entrada):** Frescas ensaladas o cremosas sopas.<br>• **Segundo Tiempo (Plato Fuerte):** Exquisitas opciones de pollo o cerdo, acompañadas de dos guarniciones a elegir, pan y chiles al centro de la mesa.<br>• **Tercer Tiempo (Tornafiesta):** Barra de esquites o chilaquiles servidos en desechables (calculado al 60% de invitados).",
        menuInfantil: "Menú infantil completo incluido con tiritas de milanesa, hamburguesa o nuggets de pollo acompañadas de pasta, papas a la francesa y una golosina sorpresa.",
        mezcladores: "Nuestra oferta de mezcladores incluye un servicio completo de hielo en cubos, agua natural y una variedad de refrescos de la línea Coca-Cola (manzana, toronja, agua mineral y la clásica Coca-Cola, además de jugo de limón y sal).",
        equipo: "Coordinador General, Capitán de Meseros, Hostess de bienvenida, Meseros capacitados, Personal de barra, Cocineros y Personal de baños.",
        dj: "DJ profesional con cabina, audio de alta fidelidad, iluminación robótica móvil, pantalla gigante o 2 pantallas, globos, pulseras neón y collares hawaianos (corbatas/velos en bodas), lámparas led wash, micrófonos inalámbricos, láser y máquina de humo.",
        cortesias: "Letras decorativas gigantes 'XV' o 'LOVE', corazón rojo decorativo, mesa especial para pastel, mesa especial para regalos, detonación de dos chisperos de pirotecnia en frío y alfombra roja.",
        duracion: "9 horas de servicio continuo.",
        detalles: "La planificación y ejecución de su evento incluye un servicio integral por parte de Primavera Events Group.",
        calidad: "Nos comprometemos a ofrecer un servicio de alta calidad, asegurando que cada evento sea único y memorable.",
        costos: "• **100 – 150 personas:** $749.00 MXN por persona<br>• **151 – 200 personas:** $729.00 MXN por persona<br>• **201 – 300 personas:** $699.00 MXN por persona",
        cortesiasAdic: "• **Escala 100-150 px:** Pista leds 5x5m de cortesía.<br>• **Escala 151-200 px:** Pista leds 5x5m y robot leds de cortesía.<br>• **Escala 201-300 px:** Pista leds 5x5m, robot leds y cabezones coreográficos de cortesía.",
        condiciones: "Se requiere depósito para reservar la fecha.",
        beneficios: "Atención personalizada y coordinación integral del evento.",
        opcionesAdic: "Montaje de ceremonia, tiempo extra de servicio y renta de limosinas.",
        requisitos: "Confirmación de invitados, selección de menú y elección de decoración.",
        notas: "Los precios NO incluyen impuestos. Se aplican tarifas adicionales por servicios extra. Disponibilidad sujeta a confirmación.",
        notaFinal: "Al firmar tu contrato: Degustación exclusiva (4 personas), diseño de montaje de acuerdo a la paleta de colores, croquis de distribución, minuto a minuto y chat exclusivo de comunicación directa. Responsables: Jessy y Richard."
      }
    ]
  },
  {
    id: "bloque-8",
    name: "Bloque 8: Salón Jardín Yolomecatl",
    ubicacion: "Calle Palma #6, Acatlipa, Temixco, Morelos.",
    capacidad: "200 a 500 invitados.",
    estilo: "Complejo señorial cerrado con amplios jardines y salón techado.",
    fortalezas: "Capilla consagrada in-situ para ceremonias de validez oficial y gran privacidad.",
    pagina: "https://primaveraeventsgroup.com/salon-jardin-yolomecatl/",
    restricciones: "Cierre de música a la 01:00 AM.",
    packages: [
      {
        name: "Paquete Destino Yolomecatl",
        estacionamiento: "Capacidad para 35 vehículos compactos en estacionamiento interno vigilado.",
        hospedaje: "No disponible en el recinto. Se cuenta con convenios especiales con hoteles de Temixco y Cuernavaca.",
        suiteNupcial: "No disponible en el recinto. Se puede gestionar suite externa en hotel asociado con costo preferencial.",
        areaJardin: "Jardines amplios y maduros con fuente artificial iluminada en la entrada principal.",
        iluminacion: "Diseño de luz arquitectónica básica en exteriores e interiores.",
        areaConsagrada: "Capilla consagrada dentro del recinto (para ceremonias religiosas con validez oficial, disponible por un costo adicional).",
        areaTechada: "Salón principal techado para albergar hasta 400 personas, con estilo modernista y elegante.",
        areaCocina: "Amplia y funcional cocina equipada para el servicio de banquetes.",
        usoRecinto: "9 horas de servicio continuo hasta la 01:00 am.",
        coctel: "Coctel de bienvenida con periqueras altas, salas lounge y sombrillas. Incluye margaritas de sabores sin alcohol (2 sabores), piñada sin alcohol, mojito sin alcohol, agua fresca (2 sabores) y crudités (pepino, jícama y jícama y zanahoria con miguelito y chamoy).",
        montaje: "Mesa principal de honor con sillón o sillones, templete de madera y centro de mesa floral natural. Arreglos naturales para centros de mesa (largo y redondo). Bases de metal altas para centros de mesa. Mesa tipo mármol cuadrada para 10 personas con silla Tiffany blanca. Mesa redonda para 10 o 12 personas con silla Tiffany blanca. Mantelería fina (mantel blanco, camino y servilleta de tela de color a elegir). Plato base (varios modelos), loza blanca, cubertería fina plateada o dorada y cristalería fina.",
        menu: "Banquete formal a 4 tiempos:<br>• **Primer Tiempo (Entrada):** Deliciosas crepas, frescas ensaladas o cremosas sopas.<br>• **Segundo Tiempo (Plato Fuerte):** Exquisitas opciones de pollo o cerdo, acompañadas de dos guarniciones a elegir, pan y chiles al centro de la mesa.<br>• **Tercer Tiempo (Postre):** Selección de postres que endulzarán tu evento, desde pasteles hasta postres de autor.<br>• **Cuarto Tiempo (Tornafiesta):** Barra de esquites o chilaquiles servidos en desechables (calculado al 60% de invitados).",
        menuInfantil: "Menú infantil opcional disponible a solicitud ($220.00 MXN extra por niño) con tiritas de milanesa, hamburguesas o nuggets con papas y espagueti.",
        mezcladores: "Nuestra oferta de mezcladores incluye un servicio completo de hielo en cubos, agua natural y una variedad de refrescos de la línea Coca-Cola (manzana, toronja, agua mineral y la clásica Coca-Cola, además de limón y sal).",
        equipo: "Coordinador General, Capitán de Meseros, Hostess de bienvenida, Meseros capacitados, Personal de barra, Stewart de limpieza, Cocineros y Personal de baños.",
        dj: "DJ profesional con cabina, audio e iluminación de alta calidad, torres iluminadas con cabezas robóticas, pantalla con proyector, globos, pulseras neón y collares hawaianos (corbatas/velos en bodas), 2 chisperos a control remoto, micrófonos inalámbricos, láser, máquina de humo y pista pixel de baile 5x5m.",
        cortesias: "Degustación para 4 personas al firmar. Letras decorativas gigantes 'XV' o 'LOVE', corazón rojo iluminado, mesas especiales de pastel y regalos, detonación de 2 chisperos, alfombra roja de entrada, espejo selfie, barra mix con 12 toppings dulces/salados y opción de montaje de ceremonia con mobiliario elegante.",
        duracion: "9 horas continuas totales de servicio.",
        detalles: "La planificación y ejecución de su evento incluye un servicio integral que cubre desde la llegada de los invitados hasta el final de la celebración.",
        calidad: "Nos comprometemos a ofrecer un servicio de alta calidad, asegurando que cada evento sea único y memorable.",
        costos: "• **100 – 149 personas:** $899.00 MXN por persona<br>• **150 – 199 personas:** $849.00 MXN por persona<br>• **200 – 299 personas:** $799.00 MXN por persona<br>• **300 – 400 personas:** $749.00 MXN por persona<br>• **401+ personas:** Consultar tarifa personalizada.",
        cortesiasAdic: "Degustación de platillos y decoración básica del salón.",
        condiciones: "Precios sujetos a cambios sin previo aviso. Se requiere depósito de reserva.",
        beneficios: "Atención personalizada de los Wedding Planners y Dirección de Primavera.",
        opcionesAdic: "Montaje de ceremonia en la capilla consagrada (costo extra) y barra de bebidas premium.",
        requisitos: "Confirmación final de invitados y selección de menú y decoración.",
        notes: "Los precios NO incluyen impuestos. Se aplican tarifas adicionales por servicios extra.",
        notaFinal: "Al firmar el contrato: Degustación exclusiva para 4 personas, diseño de montaje, croquis de distribución, minuto a minuto y chat exclusivo de comunicación. Planner Richard Hernández y Gerente Carlos Osorio (Tels: 7774587923)."
      }
    ]
  },
  {
    id: "bloque-9",
    name: "Bloque 9: Villa Di Fiori",
    ubicacion: "Xochitepec, Morelos.",
    capacidad: "100 a 350 invitados.",
    estilo: "Finca de arquitectura Toscana con imponentes arcos de cantera tallada.",
    fortalezas: "Paisajismo europeo, suite de preparación y fachadas perfectas para fotografía de alta gama.",
    pagina: "https://primaveraeventsgroup.com/venues/villa-di-fiori/",
    restricciones: "Cierre de música a la 01:00 AM.",
    packages: [
      {
        name: "Paquete Esencia Floral (Edición Toscana)",
        estacionamiento: "Amplio estacionamiento cerrado con alta capacidad logística.",
        hospedaje: "No disponible en el recinto. Convenios con hoteles cercanos en Xochitepec.",
        suiteNupcial: "Suite de preparación exclusiva y privada para anfitriones y quinceañeras con acabados elegantes.",
        areaJardin: "Jardines de diseño paisajista europeo con abundante flora exótica y explanada para banquetes.",
        iluminacion: "Iluminación perimetral decorativa y hermosa cascada iluminada rodeada de vegetación natural.",
        areaConsagrada: "Área consagrada al aire libre destinada a ceremonias religiosas con solemnidad en un ambiente íntimo y espiritual.",
        areaTechada: "Salón techado y abierto para albergar un máximo de 200 personas (y estructuras portantes en jardines para hasta 350 personas), con arcos de cantera tallada.",
        areaCocina: "Amplia y funcional cocina equipada para catering profesional.",
        usoRecinto: "Uso del salón por 8 horas (servicio disponible hasta la 01:00 AM).",
        coctel: "Coctel de bienvenida con periqueras altas, salas lounge y sombrillas. Incluye margaritas de sabores sin alcohol (2 sabores), piñadas sin alcohol, mojitos sin alcohol, agua fresca (2 sabores) y crudités (pepino, jícama y zanahoria con miguelito y chamoy).",
        montaje: "Mesa principal de honor con sillones Rey & Reyna, templete de madera, back con luces vintage y telas, y centro floral natural. Arreglo natural para centro de mesa (diseños redondos, largos y altos con flor de temporada). Mesa redonda para 8 o 10 personas con silla Tiffany blanca. Mesa cuadrada de 10 a 12 personas con mantel blanco. Mesa Campirana de 10 a 12 personas (rectangular de madera con silla crossback, Tiffany blanca, boss o lotus). Mesa tipo mármol para 10 a 12 personas (rectangular con acabado tipo mármol con combinación de sillas). Mantelería, plato base (varios modelos), loza blanca de alta calidad, cubertería fina en tonos plata/dorado/gold rose y cristalería fina.",
        menu: "Banquete formal a 4 tiempos:<br>• **Primer Tiempo (Entrada):** Frescas ensaladas o deliciosas cremas cremosas para iniciar.<br>• **Segundo Tiempo (Plato Fuerte):** Exquisitas opciones de pollo o cerdo, acompañadas de dos guarniciones a elegir, pan y chiles al centro de la mesa.<br>• **Tercer Tiempo (Tornafiesta):** Barra de esquites o chilaquiles servidos en desechables (calculado al 60% de invitados).<br>• **Cuarto Tiempo (Postre):** Selección de postres finos de autor.",
        menuInfantil: "Menú infantil completo incluido con tiritas de milanesa, hamburguesa o nuggets de pollo acompañadas de espagueti, papas a la francesa y una golosina sorpresa.",
        mezcladores: "Servicio completo de mezcladores: hielo en cubos, agua natural y refrescos de la línea Coca-Cola (sabores, mineral, clásica), limón y sal.",
        equipo: "Coordinador General, Capitán de Meseros, Hostess de bienvenida, Meseros capacitados, Personal de barra, Cocineros profesionales, Personal de mantenimiento de sanitarios.",
        dj: "DJ profesional con mampara moderna, audio e iluminación de alta calidad, torres iluminadas con cabezas robóticas, pantalla con proyector, globos multicolores, pulseras neón y collares hawaianos (corbatas y velos para boda), 2 chisperos a control remoto, micrófonos inalámbricos, láser y máquina de humo.",
        cortesias: "Letras decorativas a elegir 'XV' o 'LOVE', corazón rojo decorativo iluminado, mesa especial para pastel, mesa especial para regalos, detonación de dos chisperos de pirotecnia en frío y alfombra roja.",
        duracion: "8 horas de servicio continuo.",
        detalles: "La planificación y ejecución de su evento incluye un servicio de planeación integral paso a paso.",
        calidad: "Compromiso de alta calidad de alimentos y servicio garantizado por la firma Primavera Events Group.",
        costos: "• **100 – 199 personas:** $999.00 MXN por persona<br>• **200 – 300 personas:** $899.00 MXN por persona",
        cortesiasAdic: "Degustación de platillos, diseño de montaje y croquis de distribución de invitados.",
        condiciones: "Se requiere un depósito de apartado para reservar la fecha.",
        beneficios: "Atención personalizada de los Wedding Planners y Dirección de Primavera.",
        opcionesAdic: "Montaje de ceremonia en el área consagrada y barra de bebidas premium.",
        requisitos: "Confirmación final de invitados y selección de menú y decoración.",
        notas: "Precios NO incluyen impuestos (IVA). Se aplican tarifas adicionales por servicios extra.",
        notaFinal: "Al firmar el contrato: Degustación exclusiva (4 personas), diseño de montaje de acuerdo a la paleta de colores, croquis de distribución detallada de invitados, minuto a minuto y chat exclusivo de coordinación directa. Planner Richard Hernández y W.P. Jessica Rodríguez (Tels: 7774587923 / 7773012421)."
      }
    ]
  },
  {
    id: "bloque-10",
    name: "Bloque 10: Salón & Jardín Solaire",
    ubicacion: "Cuernavaca, Morelos.",
    capacidad: "80 a 180 invitados.",
    estilo: "Industrial-chic moderno con toques de madera sólida y cascada monumental.",
    fortalezas: "Pista Pixel LED 5x5 inteligente pre-instalada y mobiliario de autor campestre. Cascada monumental en la entrada y área consagrada al aire libre.",
    pagina: "https://primaveraeventsgroup.com/venues/solaire/",
    restricciones: "Cierre de música a la 01:00 AM.",
    packages: [
      {
        name: "Paquete Solaire (Propuesta Viky)",
        estacionamiento: "Estacionamiento privado con capacidad adecuada para los invitados del recinto.",
        hospedaje: "No disponible en el recinto. Convenios con hoteles cercanos en Cuernavaca.",
        suiteNupcial: "No disponible en el recinto. Camerino privado básico para los anfitriones.",
        areaJardin: "Jardín de ambientación industrial-chic moderno con vegetación colgante y cascada monumental de bienvenida.",
        iluminacion: "Iluminación perimetral decorativa e iluminación del recinto de última generación.",
        areaConsagrada: "Área consagrada al aire libre para ceremonias solemnes en un ambiente sofisticado.",
        areaTechada: "Salón techado estilo industrial con acabados de madera sólida y vegetación colgante.",
        areaCocina: "Cocina funcional equipada para el catering.",
        usoRecinto: "Uso del salón por 8 horas operativas.",
        coctel: "Coctel de bienvenida con periqueras altas, salas lounge y sombrillas. Incluye margaritas de sabores sin alcohol, agua fresca y crudités.",
        montaje: "Mesa principal de honor con sillón o sillones, templete de madera y centro de mesa floral natural. Mobiliario de autor campirano premium (mesas vintage de madera sólida, sillas Crossback). Mantelería fina, loza, cubertería y cristalería fina.",
        menu: "Banquete formal gourmet a 3 tiempos:<br>• **Primer Tiempo (Entrada):** Ensaladas frescas o deliciosas cremas cremosas.<br>• **Segundo Tiempo (Plato Fuerte):** Exquisitas opciones de pollo o cerdo, acompañadas de dos guarniciones a elegir, pan y chiles al centro.<br>• **Tercer Tiempo (Tornafiesta):** Barra de esquites o chilaquiles servidos en desechables (calculado al 60% de invitados).",
        menuInfantil: "Menú infantil opcional disponible a solicitud ($220.00 MXN extra por niño).",
        mezcladores: "Descorche libre de 8 horas sin costo de servicio (sin cargo por botella). Servicio completo de hielo en cubos y refrescos de la línea Coca-Cola.",
        equipo: "Coordinador General, Capitán de Meseros, Hostess de bienvenida, Meseros capacitados, Personal de barra y Personal de baños.",
        dj: "DJ profesional con audio de alta fidelidad, iluminación robótica móvil, cabezas móviles, máquina de humo y pista pixel LED 5x5m inteligente pre-instalada.",
        cortesias: "Cortesía tecnológica premium a elegir entre: Cabina de Fotos Espejo instantánea o Cámara 360 interactiva.",
        duracion: "8 horas de servicio continuo.",
        detalles: "La planificación y ejecución de su evento incluye un servicio integral de logística.",
        calidad: "Compromiso de alta calidad de alimentos y servicio garantizado por contrato.",
        costos: "• **Banquete Gourmet 3 Tiempos:** $1,199.00 MXN por persona<br>• **Taquiza Premium:** $590.00 MXN por persona",
        cortesiasAdic: "Pista Pixel LED 5x5m y descorche libre de cortesía.",
        condiciones: "Se requiere un depósito de apartado para reservar la fecha y firma de contrato.",
        beneficios: "Atención personalizada de los Wedding Planners oficiales de Primavera.",
        opcionesAdic: "Montaje de ceremonia en el área consagrada y barra de bebidas premium.",
        requisitos: "Confirmación final de invitados (10 días antes) y selección de menú y decoración.",
        notas: "Precios NO incluyen impuestos (IVA). Se aplican tarifas adicionales por servicios extra.",
        notaFinal: "Al firmar el contrato: Degustación exclusiva (4 personas), diseño de montaje de acuerdo a la paleta de colores, croquis de distribución, minuto a minuto y chat exclusivo de comunicación. Responsables: Jessy y Richard."
      }
    ]
  }
];

// ----------------------------------------------------
// 2. GENERATE MARKDOWN SECTION 3
// ----------------------------------------------------

let mdContent = `## 3. Catálogo de Locaciones (Venues) y Paquetes por Bloque

A continuación se detalla toda la información comercial estructurada por **bloque de locación**. Para cada locación se describe su ficha técnica y se desglosa el paquete asociado en detalle completo, siguiendo la estructura oficial de la empresa.

`;

recintos.forEach(recinto => {
  mdContent += `### ${recinto.name}\n\n`;
  mdContent += `#### 🏛️ Ficha Técnica del Venue\n`;
  mdContent += `*   **Ubicación:** ${recinto.ubicacion.replace('<br>', ' ')}\n`;
  mdContent += `*   **Capacidad:** ${recinto.capacidad}\n`;
  mdContent += `*   **Estilo:** ${recinto.estilo}\n`;
  mdContent += `*   **Fortalezas:** ${recinto.fortalezas}\n`;
  mdContent += `*   **Página de Referencia:** [Enlace al sitio](${recinto.pagina})\n`;
  if (recinto.restricciones) {
    mdContent += `*   **Restricciones:** ${recinto.restricciones}\n`;
  }
  mdContent += `\n#### 📦 Paquete(s) Asociado(s):\n\n`;

  recinto.packages.forEach(pkg => {
    mdContent += `##### 🌟 ${pkg.name}\n\n`;
    mdContent += `*   **➢ Estacionamiento**\n    ${pkg.estacionamiento}\n\n`;
    mdContent += `*   **➢ Hospedaje**\n    ${pkg.hospedaje}\n\n`;
    mdContent += `*   **➢ Suite nupcial**\n    ${pkg.suiteNupcial}\n\n`;
    mdContent += `*   **➢ Área de jardín**\n    ${pkg.areaJardin}\n\n`;
    mdContent += `*   **➢ Iluminación arquitectónica interior y exterior**\n    ${pkg.iluminacion}\n\n`;
    mdContent += `*   **➢ Área Consagrada**\n    ${pkg.areaConsagrada}\n\n`;
    mdContent += `*   **➢ Área techada**\n    ${pkg.areaTechada}\n\n`;
    mdContent += `*   **➢ Área de cocina**\n    ${pkg.areaCocina}\n\n`;
    mdContent += `*   **➢ Uso del Recinto / Quinta**\n    ${pkg.usoRecinto}\n\n`;
    mdContent += `*   **La mejor manera de iniciar: Coctel de bienvenida**\n    ${pkg.coctel}\n\n`;
    mdContent += `*   **y Para Decorar y Ambientar: Montaje banquete**\n    ${pkg.montaje}\n\n`;
    mdContent += `*   **Menú de Banquete**\n    ${pkg.menu.replace(/<br>/g, '\n    ')}\n\n`;
    mdContent += `*   **Menú Infantil**\n    ${pkg.menuInfantil}\n\n`;
    mdContent += `*   **Mezcladores Disponibles**\n    ${pkg.mezcladores}\n\n`;
    mdContent += `*   **Equipo de Servicio**\n    ${pkg.equipo}\n\n`;
    mdContent += `*   **Servicios de DJ Profesional**\n    ${pkg.dj}\n\n`;
    mdContent += `*   **Servicios Complementarios: Cortesías Incluidas**\n    ${pkg.cortesias}\n\n`;
    mdContent += `*   **Duración del Servicio**\n    ${pkg.duracion}\n\n`;
    mdContent += `*   **Detalles del Servicio**\n    ${pkg.detalles}\n\n`;
    mdContent += `*   **Compromiso de Calidad**\n    ${pkg.calidad}\n\n`;
    mdContent += `*   **Cotización de Costos (Precios por Persona)**\n    ${pkg.costos.replace(/<br>/g, '\n    ')}\n\n`;
    if (pkg.cortesiasAdic) {
      mdContent += `*   **Cortesías Adicionales**\n    ${pkg.cortesiasAdic.replace(/<br>/g, '\n    ')}\n\n`;
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
    <h2 class="section-title">3. Catálogo de Locaciones (Venues) y Paquetes por Bloque</h2>
    <p>A continuación se detallan las fichas comerciales de las 10 locaciones oficiales de Primavera Events Group, agrupando la información del recinto y su(s) paquete(s) exclusivo(s) asociado(s).</p>
`;

recintos.forEach(recinto => {
  htmlContent += `    
    <!-- ${recinto.name.toUpperCase()} -->
    <div class="venue-block">
      <div class="venue-title">${recinto.name}</div>
      <p><strong>Ubicación:</strong> ${recinto.ubicacion}</p>
      <p><strong>Capacidad:</strong> ${recinto.capacidad}</p>
      <p><strong>Estilo:</strong> ${recinto.estilo}</p>
      <p><strong>Fortalezas:</strong> ${recinto.fortalezas}</p>
      <p><strong>Página de Referencia:</strong> <a href="${recinto.pagina}" target="_blank">Enlace al sitio</a></p>
`;
  if (recinto.restricciones) {
    htmlContent += `      <p><strong>Restricciones:</strong> ${recinto.restricciones}</p>\n`;
  }

  recinto.packages.forEach(pkg => {
    htmlContent += `
      <div class="package-box">
        <h4>🌟 ${pkg.name}</h4>
        <p><strong>➢ Estacionamiento:</strong> ${pkg.estacionamiento}</p>
        <p><strong>➢ Hospedaje:</strong> ${pkg.hospedaje}</p>
        <p><strong>➢ Suite nupcial:</strong> ${pkg.suiteNupcial}</p>
        <p><strong>➢ Área de jardín:</strong> ${pkg.areaJardin}</p>
        <p><strong>➢ Iluminación arquitectónica:</strong> ${pkg.iluminacion}</p>
        <p><strong>➢ Área Consagrada:</strong> ${pkg.areaConsagrada}</p>
        <p><strong>➢ Área techada:</strong> ${pkg.areaTechada}</p>
        <p><strong>➢ Área de cocina:</strong> ${pkg.areaCocina}</p>
        <p><strong>➢ Uso del Recinto / Quinta:</strong> ${pkg.usoRecinto}</p>
        <p><strong>La mejor manera de iniciar (Coctel):</strong> ${pkg.coctel}</p>
        <p><strong>y Para Decorar y Ambientar (Montaje):</strong> ${pkg.montaje}</p>
        <p><strong>Menú de Banquete:</strong> ${pkg.menu}</p>
        <p><strong>Menú Infantil:</strong> ${pkg.menuInfantil}</p>
        <p><strong>Mezcladores Disponibles:</strong> ${pkg.mezcladores}</p>
        <p><strong>Equipo de Servicio:</strong> ${pkg.equipo}</p>
        <p><strong>DJ Profesional:</strong> ${pkg.dj}</p>
        <p><strong>Cortesías Incluidas:</strong> ${pkg.cortesias}</p>
        <p><strong>Duración del Servicio:</strong> ${pkg.duracion}</p>
        <p><strong>Detalles del Servicio:</strong> ${pkg.detalles}</p>
        <p><strong>Compromiso de Calidad:</strong> ${pkg.calidad}</p>
        <p><strong>Cotización de Costos (Persona):</strong><br>${pkg.costos}</p>
`;
    if (pkg.cortesiasAdic) {
      htmlContent += `        <p><strong>Cortesías Adicionales:</strong><br>${pkg.cortesiasAdic}</p>\n`;
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
const mdStartAnchor = '## 3. Catálogo de Locaciones (Venues) y Paquetes por Bloque';
const mdEndAnchor = '## 4. Catálogo de Paquetes de Graduación';

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
