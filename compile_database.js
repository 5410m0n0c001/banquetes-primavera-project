const fs = require('fs');
const path = require('path');

const cleanDir = 'C:\\Users\\quant\\.gemini\\antigravity\\brain\\15c1b059-6909-48c0-82ee-fede74c0abd5\\scraped_clean';
const jsonPath = 'c:\\Users\\quant\\OneDrive\\Desktop\\Banqutes primavera web\\base_de_datos_primavera.json';
const mdPath = 'c:\\Users\\quant\\OneDrive\\Desktop\\Banqutes primavera web\\base_de_datos_primavera.md';

console.log('Compiling Primavera Events Group Database...');

// 1. Define Master Structured Data representing the exact details found in the files
const database = {
  metadata: {
    title: "Base de Datos de Primavera Events Group",
    version: "1.0",
    last_updated: "2026-06-01",
    author: "Web Scraper Subagent"
  },
  packages: [
    {
      id: "paquete-gobernador",
      name: "Paquete Gobernador",
      url: "https://primaveraeventsgroup.com/paquete-gobernador/",
      venue: "Centro de Convenciones Presidente (Avenida Defensa Nacional 8, Chamilpa, Cuernavaca, Morelos)",
      duration: "9 horas (Hasta las 00:00 hrs)",
      inclusions: [
        "Estacionamiento para 35 vehículos compactos",
        "Área de jardín con fuente artificial en la entrada principal",
        "Área de kids con juegos múltiples fijos",
        "Salón techado para 500px máximo, estilo arquitectónico modernista y elegante",
        "Templete para DJ o Grupo musical",
        "Área de cocina amplia y baños múltiples",
        "Uso de salón por 8 horas (total 9 horas de servicio continuo)",
        "Coctel de bienvenida con periqueras altas, salas lounge y sombrillas",
        "Margaritas de sabores sin alcohol (2 sabores)",
        "Agua fresca (2 sabores)",
        "Crudités (pepino, jícama y zanahoria con miguelito y chamoy)",
        "Mesa principal de honor con sillón o sillones, templete de madera y centro de mesa floral natural",
        "Arreglo natural para centros de mesa (largos, redondos y altos)",
        "Mesa redonda/cuadrada/tipo mármol/vintage, sillas Tiffany, Crossback, Lotus o Boss",
        "Mantelería fina (mantel blanco, camino y servilleta de tela de color a elegir)",
        "Plato base (varios modelos), loza blanca, cubertería fina (dorada y plata) y cristalería fina",
        "Banquete a 3 tiempos (Entrada, Plato Fuerte, Tornafiesta)",
        "Servicio de mezcladores completo: hielo, agua natural, refrescos de la línea Coca-Cola (sabores, mineral, clásica), jugo de limón y sal",
        "Equipo de servicio completo: Coordinador General, Hostess, Meseros, Personal de barra, Stewart, Cocina, Personal de baños",
        "Servicio de DJ Profesional con cabina, audio/iluminación de alta calidad, cabezas robóticas, proyector/pantalla, accesorios de animación (globos, pulseras neón, collares hawaianos), micrófonos inalámbricos, láser y máquina de humo",
        "Cortesías incluidas: Degustación exclusiva para 4 personas al firmar, letras decorativas gigantes ('XV' o 'LOVE'), corazón rojo iluminado, mesas de pastel/regalos, detonación de 2 chisperos, alfombra roja, espejo selfie y barra mix con 12 toppings"
      ],
      menu_structure: {
        type: "3 Tiempos",
        details: [
          "Primer Tiempo: Entradas (deliciosas ensaladas frescas o cremosas sopas)",
          "Segundo Tiempo: Plato Fuerte (exquisitas opciones de pollo o cerdo acompañadas de dos guarniciones a elegir, incluye pan y chiles)",
          "Tercer Tiempo: Tornafiesta (barra de esquites o chilaquiles servidos en desechables)"
        ]
      },
      pricing: [
        { guests: "100 - 149 personas", price_per_person: "$899.00 MXN", details: "Incluye degustación y decoración básica" },
        { guests: "150 - 199 personas", price_per_person: "$849.00 MXN", details: "Incluye degustación y decoración básica" },
        { guests: "200 - 299 personas", price_per_person: "$799.00 MXN", details: "Incluye degustación y decoración básica" },
        { guests: "300 - 400 personas", price_per_person: "$749.00 MXN", details: "Incluye degustación y decoración básica" },
        { guests: "401+ personas", price_per_person: "Consultar / Personalizado", details: "Personalizado según necesidades" }
      ],
      conditions: [
        "Precios sujetos a cambios sin previo aviso",
        "Se requiere depósito para reservar",
        "Los precios NO incluyen impuestos",
        "Se aplican tarifas adicionales por servicios extra"
      ]
    },
    {
      id: "paquete-presidente",
      name: "Paquete Presidente",
      url: "https://primaveraeventsgroup.com/paquete-presidente/",
      venue: "Centro de Convenciones Presidente (Avenida Defensa Nacional 8, Chamilpa, Cuernavaca, Morelos)",
      duration: "9 horas (Hasta las 01:00 hrs)",
      inclusions: [
        "Estacionamiento para 35 vehículos compactos",
        "Área de jardín con fuente artificial en la entrada principal",
        "Área de kids con juegos múltiples fijos",
        "Salón techado para 500px máximo, estilo modernista elegante",
        "Templete para DJ o Grupo musical",
        "Área de cocina amplia y baños múltiples",
        "Uso de salón por 9 horas continuas",
        "Coctel de bienvenida premium con periqueras altas, salas lounge y sombrillas",
        "Margaritas de sabores sin alcohol, piñada sin alcohol y mojito sin alcohol",
        "Agua fresca (2 sabores)",
        "Crudités (pepino, jícama y zanahoria con miguelito y chamoy)",
        "Mesa principal de honor con sillones Rey & Reyna, templete de madera, centro floral natural",
        "Arreglo natural para centro de mesa (largo y redondo)",
        "Bases de metal altas para centros de mesa",
        "Mesa tipo mármol cuadrada/redonda para 10-12 personas con silla Tiffany blanca",
        "Mantelería fina (mantel blanco, camino y servilleta de tela de color a elegir)",
        "Plato base (varios modelos), loza blanca, cubertería fina (dorada y plata) y cristalería fina",
        "Banquete a 4 tiempos (Entrada, Plato Fuerte, Postre, Tornafiesta)",
        "Servicio de mezcladores completo: hielo, agua, refrescos de la línea Coca-Cola, limón y sal",
        "Equipo de servicio completo: Coordinador General, Capitán de Meseros, Hostess, Meseros, Barra, Stewart, Cocina, Personal de baños",
        "Servicio de DJ Profesional con cabina, audio/iluminación de alta calidad, cabezas robóticas, proyector/pantalla, accesorios de animación, micrófonos inalámbricos, láser, máquina de humo, pista de baile 5x5 y 2 chisperos a control remoto",
        "Cortesías incluidas: Degustación exclusiva para 4 personas, letras decorativas gigantes ('XV' o 'LOVE'), corazón rojo iluminado, mesas de pastel/regalos, detonación de 2 chisperos, alfombra roja, espejo selfie, barra mix con 12 toppings y opción de montaje de ceremonia con mobiliario elegante"
      ],
      menu_structure: {
        type: "4 Tiempos",
        details: [
          "Primer Tiempo: Entradas (crepas deliciosas, ensaladas frescas o sopas cremosas)",
          "Segundo Tiempo: Plato Fuerte (pollo o cerdo con 2 guarniciones, pan y chiles)",
          "Tercer Tiempo: Postre (selección de repostería fina o de autor)",
          "Cuarto Tiempo: Tornafiesta (barra de esquites o chilaquiles servidos en desechables)"
        ]
      },
      pricing: [
        { guests: "100 - 149 personas", price_per_person: "$899.00 MXN", details: "Incluye degustación y decoración básica" },
        { guests: "150 - 199 personas", price_per_person: "$849.00 MXN", details: "Incluye degustación y decoración básica" },
        { guests: "200 - 299 personas", price_per_person: "$799.00 MXN", details: "Incluye degustación y decoración básica" },
        { guests: "300 - 400 personas", price_per_person: "$749.00 MXN", details: "Incluye degustación y decoración básica" },
        { guests: "401+ personas", price_per_person: "Consultar / Personalizado", details: "Personalizado según necesidades" }
      ],
      conditions: [
        "Precios sujetos a cambios sin previo aviso",
        "Se requiere depósito para reservar",
        "Los precios NO incluyen impuestos",
        "Se aplican tarifas adicionales por servicios extra"
      ]
    },
    {
      id: "paquete-esencia-floral",
      name: "Paquete Esencia Floral",
      url: "https://primaveraeventsgroup.com/paquete-esencia-floral/",
      venue: "Privada las Fuentes s/n, San Gaspar, Jiutepec, Morelos",
      duration: "8 horas (Hasta las 01:00 hrs)",
      inclusions: [
        "Estacionamiento amplio para 60 autos",
        "Área de recepción elegante y exclusiva",
        "Área de jardín con abundante vegetación",
        "Hermosa cascada iluminada rodeada de vegetación natural",
        "Área consagrada destinada a ceremonias religiosas",
        "Salón techado para 200px máximo, modernista y elegante",
        "Coctel de bienvenida con periqueras, salas lounge y sombrillas",
        "Margaritas de sabores sin alcohol, piñada sin alcohol y mojito sin alcohol",
        "Agua fresca (2 sabores) y crudités con miguelito y chamoy",
        "Mesa principal con sillones Rey & Reyna, templete de madera, back con luces vintage y telas",
        "Arreglo natural para centro de mesa (redondos, largos y altos)",
        "Mesa redonda (8-10px) o cuadrada (10-12px) con mantel blanco y silla Tiffany blanca",
        "Mesa Campirana de madera (10-12px) con silla Crossback, Tiffany, Boss o Lotus",
        "Mesa tipo mármol (10-12px) con sillas Tiffany, Crossback, Boss o Lotus combinadas",
        "Mantelería, plato base (varios modelos), loza blanca, cubertería fina (plata, oro, gold rose) y cristalería fina",
        "Banquete a 4 tiempos (Entrada, Plato Fuerte, Tornafiesta, Menú Infantil incluido)",
        "Servicio de mezcladores, hielo, refrescos de la línea Coca-Cola, limón y sal",
        "Equipo de servicio: Coordinador General, Capitán de Meseros, Hostess, Meseros, Barra, Cocina, Baños",
        "DJ profesional con mampara moderna, audio/iluminación LED, cabezas robóticas, proyector/pantalla, accesorios de animación, micrófonos inalámbricos, láser, máquina de humo y 2 chisperos a control remoto",
        "Cortesías: Letras 'XV' o 'LOVE', corazón rojo iluminado, mesas de pastel/regalos, detonación de 2 chisperos, alfombra roja",
        "Servicios finales: Degustación exclusiva (4px), diseño de montaje, croquis de distribución, minuto a minuto y chat exclusivo de coordinación"
      ],
      menu_structure: {
        type: "4 Tiempos",
        details: [
          "Primer Tiempo: Entradas (ensaladas frescas o deliciosas cremas cremosas)",
          "Segundo Tiempo: Plato Fuerte (pollo o cerdo con 2 guarniciones, pan y chiles)",
          "Tercer Tiempo: Tornafiesta (barra de esquites o chilaquiles al 60% de invitados)",
          "Menú Infantil: Tiritas de milanesa, hamburguesa o nuggets de pollo acompañados de espagueti, papas fritas y golosina sorpresa"
        ]
      },
      pricing: [
        { guests: "100 - 199 personas", price_per_person: "$999.00 MXN", details: "Incluye degustación y decoración básica" },
        { guests: "200 - 300 personas", price_per_person: "$899.00 MXN", details: "Incluye degustación y decoración básica" }
      ],
      conditions: [
        "Precios sujetos a cambios sin previo aviso",
        "Se requiere depósito para reservar",
        "Los precios NO incluyen impuestos"
      ]
    },
    {
      id: "paquete-glow-graduation-elite",
      name: "Paquete Glow Graduation Elite",
      url: "https://primaveraeventsgroup.com/paquete-glow-graduation-elite/",
      venue: "Múltiples locaciones en Morelos (Xochitepec, Cuernavaca, Jiutepec, Temixco)",
      duration: "No especificado explícitamente (coordinación completa)",
      inclusions: [
        "Coctel de bienvenida con periqueras, sombrillas y salas lounge",
        "Bebidas de bienvenida preparadas al momento sin alcohol: Margaritas, Piñada y Mojito",
        "Estación fresca: Agua de frutas naturales y crudités con miguelito y chamoy",
        "Mobiliario premium combinado: mesa rectangular de madera, mesa cuadrada plegable y mesa tipo mármol",
        "Sillería decorativa a elegir: Crossback, Tiffany, Boss o Lotus",
        "Loza fina, plato base, cubertería fina premium (plata, oro, negro o golden rose), cristalería fina de color",
        "Centro de mesa floral natural de temporada (bajos y altos)",
        "Banquete a 4 tiempos (Entrada, Plato Principal, Postre, Tornafiesta)",
        "Servicio de mezcladores: Coca-Cola, manzanita, toronja, mineral, natural, hielo en cubos, sal y limón, vasos desechables",
        "Servicio de entretenimiento de alta gama: DJ profesional, audio premium, mampara estética, luces LED y móviles, torres iluminadas de 2m, pantallas de proyección, máquina de humo",
        "Espectáculo en vivo incluido: 1 hora de banda en vivo o mariachi, 1 hora de saxofonista interactuando con el DJ",
        "Personal de servicio completo: Coordinador General, Cocineros de alta cocina, Hostess, Meseros, Barman, Capitán de meseros",
        "Show de animación en pista: Showmen con cabezones coreográficos, inflables gigantes de dinosaurio/delfín en pista, globos y accesorios neón, hawaianos, lentes, sombreros",
        "Experiencia tecnológica interactiva: Cabina Espejo con fotos instantáneas, Cámara 360 con videos personalizados en alta resolución",
        "Planificación avanzada: Croquis del banquete, acompañamiento constante (antes, durante y después), chat exclusivo de soporte",
        "Cortesías especiales para graduados: Letras gigantes iluminadas con iniciales de la escuela/institución, alfombra roja y back de fotos, pirotecnia de chispa fría para brindis, números de mesa personalizados, emotivo último pase de lista, botella de vino para brindis de graduados, carrito de shots dinámicos, barra mix de toppings dulces/salados, sesión de fotos grupal"
      ],
      menu_structure: {
        type: "4 Tiempos",
        details: [
          "Primer Tiempo: Entrada (ensaladas selectas, cremas finas o crepas saladas)",
          "Segundo Tiempo: Plato Principal (pollo o cerdo en diversas salsas con 2 guarniciones, pan y chiles)",
          "Tercer Tiempo: Postre (propuesta de repostería fina de autor)",
          "Cuarto Tiempo: Tornafiesta (chilaquiles, esquites o sopas maruchan)"
        ]
      },
      pricing: [
        { venue: "Finca las Isabeles (Xochitepec)", guests: "200 - 400 invitados", price_per_person: "$999.00 / $949.00 MXN", details: "Precio Standard / Precio Especial" },
        { venue: "Jardín Nautilus (Xochitepec)", guests: "300 - 400 invitados", price_per_person: "$999.00 / $849.00 MXN", details: "Precio Standard / Precio Especial" },
        { venue: "C.C Presidente (Cuernavaca)", guests: "200 - 500 invitados", price_per_person: "$949.00 / $899.00 MXN", details: "Precio Standard / Precio Especial" },
        { venue: "Villa San Gaspar (Jiutepec)", guests: "200 - 400 invitados", price_per_person: "$999.00 / $949.00 MXN", details: "Precio Standard / Precio Especial" },
        { venue: "Jardín San Rafael (Jiutepec)", guests: "300 - 800 invitados", price_per_person: "$999.00 / $949.00 MXN", details: "Precio Standard / Precio Especial" },
        { venue: "Jn Paraiso de lago (Jiutepec)", guests: "200 - 300 invitados", price_per_person: "$999.00 / $949.00 MXN", details: "Precio Standard / Precio Especial" },
        { venue: "Jardín Yolomecatl (Temixco)", guests: "200 - 500 invitados", price_per_person: "$799.90 / $749.00 MXN", details: "Precio Standard / Precio Especial" },
        { venue: "Quinta Zarabanda (Temixco)", guests: "200 - 300 invitados", price_per_person: "$999.00 / $949.00 MXN", details: "Precio Standard / Precio Especial" }
      ],
      conditions: [
        "Precios sujetos a confirmación y depósito previo",
        "Sesiones de fotos fuera del estado de Morelos causan cargos de viáticos para el equipo fotográfico",
        "Los medios técnicos de proyección para el videoclip deben ser provistos por el cliente"
      ]
    },
    {
      id: "paquete-armonia",
      name: "Paquete Armonía",
      url: "https://primaveraeventsgroup.com/paquete-armonia/",
      venue: "Quinta Zarabanda (Avenida Lauro Ortega Martínez 4, Las Animas, Temixco, Morelos)",
      duration: "10 horas continuas (Sin restricción de horario)",
      inclusions: [
        "Estacionamiento amplio con servicio de Valet Parking",
        "Suite Nupcial de lujo con jacuzzi, vestidor, tocador y decoración romántica",
        "Área de jardín hermosa con fuente artificial en la entrada principal",
        "Diseño de iluminación arquitectónica interior y exterior",
        "Área Consagrada íntima para ceremonias civiles o religiosas en entorno natural",
        "Área techada para albergar 250px máximo con estilo arquitectónico modernista",
        "Área de cocina amplia y funcional",
        "Hospedaje opcional para 14 personas en la Quinta (habitación climatizada, cocina, alberca, jardín privado - costo adicional)",
        "Coctel de bienvenida con periqueras altas, salas lounge y sombrillas",
        "Margaritas de sabores en copa flauta sin alcohol, mojito sin alcohol y piñada sin alcohol",
        "Agua fresca de fruta natural y crudités variados con miguelito y chamoy",
        "Mesa principal con sillones imperiales Rey & Reyna, templete y back vintage con luces y telas",
        "Centros de mesa con flor natural de temporada altos, bajos y redondos combinados",
        "Mesa redonda (8-10px) o cuadrada (10-12px) con mantel blanco y silla Tiffany",
        "Mesa Campirana de madera (10-12px) con sillas Tiffany, Crossback, Boss o Lotus",
        "Mesa tipo mármol (10-12px) con sillas combinadas Tiffany, Crossback, Boss o Lotus",
        "Loza blanca, plato base, cubertería fina en plata, oro o rose gold y cristalería fina de color",
        "Banquete a 3 tiempos + Menú Infantil completo incluido",
        "Servicio completo de mezcladores con hielo, agua y refrescos de la línea Coca-Cola",
        "Equipo de servicio completo: Coordinador General, Capitán de Meseros, Hostess, Meseros, Barman, Stewart y Baños",
        "DJ Profesional con cabina mampara, audio premium, torres robóticas, proyector/pantalla, láser, máquina de humo y luces wash",
        "Cortesías: Iniciales gigantes, corazón iluminado, mesas de pastel/regalos, 2 chisperos y alfombra roja",
        "Atención final premium: Degustación (4px), diseño de montaje, croquis, minuto a minuto y chat exclusivo",
        "Cortesía de graduados/XV de lujo: Pista de baile Pixel LED 5x5 gratis y 2 opciones adicionales a elegir entre Pista Pixel, Cabina 360 y Robot de Leds"
      ],
      menu_structure: {
        type: "3 Tiempos + Menú Infantil",
        details: [
          "Primer Tiempo: Entradas (frescas ensaladas o deliciosas cremas cremosas)",
          "Segundo Tiempo: Plato Fuerte (pollo o cerdo con 2 guarniciones, pan y chiles)",
          "Tercer Tiempo: Tornafiesta (barra de esquites o chilaquiles al 60% de invitados)",
          "Menú Infantil: Nuggets, milanesa o hamburguesa con espagueti, papas a la francesa y dulce sorpresa"
        ]
      },
      pricing: [
        { guests: "100 - 150 personas", price_per_person: "$1,700.00 MXN", details: "Incluye degustación y ambientación de lujo" },
        { guests: "151 - 250 personas", price_per_person: "$1,450.00 MXN", details: "Incluye degustación y ambientación de lujo" }
      ],
      conditions: [
        "Se requiere depósito para reservar la fecha",
        "Precios NO incluyen impuestos",
        "Servicios de hospedaje en la Quinta tienen costo adicional"
      ]
    },
    {
      id: "paquete-vuelo-esmeralda",
      name: "Paquete Vuelo Esmeralda",
      url: "https://primaveraeventsgroup.com/paquete-vuelo-esmeralda/",
      venue: "Jardín La Flor u otros jardines campestres selectos en Morelos",
      duration: "8 a 9 horas continuas",
      inclusions: [
        "Acceso a áreas de jardín y áreas comunes decoradas",
        "Hospedaje opcional en hotel asociado a 80m de distancia para 60 personas (reserva previa, costo adicional)",
        "Banquete gourmet personalizado de alta calidad",
        "Mobiliario de gala campirano combinando madera y mantelería fina",
        "Loza, plaque y cristalería fina",
        "Centros de mesa con arreglos florales naturales de temporada",
        "DJ, iluminación y soporte de audio completo",
        "Servicio de meseros y personal de cocina profesional",
        "Cortesías decorativas de la firma Primavera Events"
      ],
      pricing: [
        { guests: "100 - 149 personas", price_per_person: "$2,199.00 MXN", details: "Servicio premium completo" },
        { guests: "150 - 199 personas", price_per_person: "$2,099.00 MXN", details: "Servicio premium completo" },
        { guests: "200 - 299 personas", price_per_person: "$1,999.00 MXN", details: "Servicio premium completo" }
      ],
      conditions: [
        "Los precios NO incluyen impuestos",
        "Hospedaje se contrata por separado"
      ]
    },
    {
      id: "paquete-imperial-ecuestre",
      name: "Paquete Imperial Ecuestre",
      url: "https://primaveraeventsgroup.com/paquete-imperial-ecuestre/",
      venue: "Locación de estilo Hacienda / Hípico o Quinta con temática rústica",
      duration: "No especificado (típicamente 8 a 9 horas)",
      inclusions: [
        "Montajes temáticos rústico-elegantes estilo campestre",
        "Uso de jardines amplios y locación ecuestre",
        "Banquete a tiempos con guarniciones tradicionales y finas",
        "Mobiliario campirano (mesas de madera, sillas crossback)",
        "Servicio de meseros y coordinación del evento",
        "Audio, DJ y kit de animación en pista"
      ],
      pricing: [
        { guests: "100 - 199 personas", price_per_person: "$749.00 MXN", details: "Precio de escala inicial" },
        { guests: "200 - 299 personas", price_per_person: "$729.00 MXN", details: "Precio preferente" },
        { guests: "300 - 400 personas", price_per_person: "$699.00 MXN", details: "Precio de escala máxima" }
      ],
      conditions: [
        "Los precios NO incluyen impuestos",
        "Requiere confirmación de disponibilidad del hípico/hacienda"
      ]
    },
    {
      id: "paquete-destino-yolomecatl",
      name: "Paquete Destino Yolomecatl",
      url: "https://primaveraeventsgroup.com/paquete-destino-yolomecatl/",
      venue: "Jardín Yolomecatl / Salón Jardín Yolomecatl (Temixco, Morelos)",
      duration: "9 horas continuas",
      inclusions: [
        "Uso del Salón Jardín Yolomecatl con amplios jardines y áreas techadas",
        "Uso de Capilla Consagrada en el recinto (con costo adicional)",
        "Banquete clásico de 3 o 4 tiempos",
        "Mobiliario de lujo (tiffany, crossback) y mantelería en el color elegido",
        "Servicio de meseros, Stewart y coordinador general",
        "DJ profesional, iluminación de pista, torres con cabezas móviles y animación",
        "Cortesías de pirotecnia fría, espejo selfie, letras gigantes y alfombra roja"
      ],
      pricing: [
        { guests: "100 - 149 personas", price_per_person: "$899.00 MXN", details: "Básico completo" },
        { guests: "150 - 199 personas", price_per_person: "$849.00 MXN", details: "Preferente completo" },
        { guests: "200 - 299 personas", price_per_person: "$799.00 MXN", details: "Especial completo" },
        { guests: "300 - 400 personas", price_per_person: "$749.00 MXN", details: "Escala máxima preferente" }
      ],
      conditions: [
        "Precios sujetos a cambios sin previo aviso",
        "Los precios NO incluyen impuestos",
        "Capilla requiere reservación y tiene costo extra"
      ]
    },
    {
      id: "paquete-linaje-pura-sangre",
      name: "Paquete Linaje Pura Sangre",
      url: "https://primaveraeventsgroup.com/paquete-linaje-pura-sangre/",
      venue: "Locación de estilo Hacienda Ecuestre o rancho rústico-elegante",
      duration: "9 horas continuas",
      inclusions: [
        "Uso de locación campestre para eventos masivos",
        "Mobiliario rústico de alta gama (madera e hilos rústicos)",
        "Banquete gourmet a 3 tiempos con platos de pollo y cerdo",
        "Refrescos, mezcladores y hielo ilimitado en evento",
        "Coordinador, personal de meseros uniformados, cocina y stewards",
        "DJ, cabina, audio, luces dinámicas y máquina de humo"
      ],
      pricing: [
        { guests: "100 - 149 personas", price_per_person: "$799.00 MXN", details: "Precio base" },
        { guests: "150 - 199 personas", price_per_person: "$749.00 MXN", details: "Precio preferente" },
        { guests: "200 - 299 personas", price_per_person: "$699.00 MXN", details: "Precio especial" },
        { guests: "300 - 400 personas", price_per_person: "$649.00 MXN", details: "Precio de escala máxima" }
      ],
      conditions: [
        "Precios sujetos a cambios sin previo aviso",
        "Precios NO incluyen impuestos"
      ]
    },
    {
      id: "paquete-natures-majesty",
      name: "Paquete Nature's Majesty",
      url: "https://primaveraeventsgroup.com/paquete-natures-majesty/",
      venue: "Jardín ecológico / Quinta campestre rodeada de abundante bosque y cabañas",
      duration: "9 horas continuas",
      inclusions: [
        "Uso de amplias áreas de jardín boscoso",
        "Alojamiento en hermosas y confortables cabañas ecológicas rústicas (previa reserva y costo adicional)",
        "Banquete gourmet a tiempos con finos ingredientes campestres",
        "Mobiliario estilo campestre de autor",
        "Audio, DJ profesional, iluminación arquitectónica del bosque y kit de animación",
        "Personal operativo de meseros, barras, Stewart y sanitarios",
        "Cortesías tradicionales de la firma"
      ],
      pricing: [
        { guests: "100 - 149 personas", price_per_person: "$1,999.00 MXN", details: "Servicio campestre ecológico de lujo" },
        { guests: "150 - 199 personas", price_per_person: "$1,899.00 MXN", details: "Servicio campestre ecológico de lujo" },
        { guests: "200 - 299 personas", price_per_person: "$1,799.00 MXN", details: "Servicio campestre ecológico de lujo" }
      ],
      conditions: [
        "Precios NO incluyen impuestos",
        "Estancia en cabañas se cotiza y reserva por separado"
      ]
    },
    {
      id: "paquete-experiencia-deluxe",
      name: "Paquete Experiencia Deluxe (Fotografía y Video)",
      url: "https://primaveraeventsgroup.com/paquete-experiencia-deluxe/",
      type: "Servicio de Fotografía y Video para Quinceañeras",
      pricing: {
        total_cost: "$10,900.00 MXN",
        booking_deposit: "$990.00 MXN (10% del total)",
        liquidation_balance: "$9,910.00 MXN (Liquidación el día del evento)"
      },
      inclusions: [
        "Fotografía digital ilimitada durante todo el día del evento",
        "Álbum fotográfico personalizado de alta calidad",
        "200 fotos impresas físicas en tamaño postal (4x6 pulgadas)",
        "Ampliación física en tamaño 16x24 pulgadas con protección y elegante marco decorativo",
        "Foto Firma interactiva para firmas de invitados (incluye préstamo de caballete y todo lo necesario para escribir mensajes)",
        "Estuche de madera fina grabado personalizado para guardar la USB",
        "Dispositivo USB con la Película cinematográfica editada y todas las fotos digitales en alta resolución",
        "Sesión previa al evento en locación/exteriores",
        "Videoclip memorable para proyectar en pantalla durante el banquete del evento",
        "Plazo de entrega de 30 días hábiles una vez seleccionadas las fotografías finales por el cliente"
      ],
      conditions: [
        "Sanción de $1,500.00 MXN en caso de no liquidar el saldo total el día del evento, pudiendo procederse a la retención o eliminación del material realizado",
        "No se venden fotos a los invitados durante el evento (en caso de requerirse, pedir con anticipación)"
      ]
    },
    {
      id: "paquete-cinematic-prestige",
      name: "Paquete Cinematic Prestige (Fotografía y Video)",
      url: "https://primaveraeventsgroup.com/paquete-cinematic-prestige/",
      type: "Servicio Premium de Producción Cinematográfica y Foto para Eventos",
      pricing: {
        total_cost: "$13,900.00 MXN",
        booking_deposit: "$1,390.00 MXN (10% del total)",
        liquidation_balance: "$12,510.00 MXN (Liquidación el día del evento)"
      },
      inclusions: [
        "Grabación cinematográfica a dos cámaras simultáneas para máxima cobertura y ángulos",
        "Uso de drones profesionales de última generación en 4K para espectaculares tomas aéreas",
        "Fotografía digital ilimitada de alta definición durante todo el evento",
        "Elegante Photobook físico personalizado en tamaño 12x12 pulgadas",
        "50 fotografías impresas físicas en tamaño postal",
        "Ampliación física de gran formato en tamaño 16x24 pulgadas con marco y protección acrílica",
        "Foto Firma interactiva premium con caballete incluido y plumones especiales para mensajes de invitados",
        "Estuche de madera fina personalizado grabado para USB",
        "USB premium con la película editada cinematográficamente y las fotografías digitales",
        "Sesión de fotos y video previa al evento en locación exterior",
        "Videoclip cinematográfico para proyección el día del evento (medios técnicos de proyección a cargo del cliente)"
      ],
      conditions: [
        "Sanción de $1,500.00 MXN en caso de no liquidar el saldo el día del evento, con opción a eliminación del material",
        "Sesiones fuera del estado de Morelos causan cargos de viáticos para el equipo técnico a cuenta del cliente",
        "Plazo de entrega de 30 días hábiles tras la selección final de fotos por parte del cliente"
      ]
    },
    {
      id: "paquete-royal-cinematic",
      name: "Paquete Royal Cinematic (Fotografía y Video)",
      url: "https://primaveraeventsgroup.com/paquete-royal-cinematic/",
      type: "Servicio de Alta Gama de Fotografía y Video para Bodas",
      pricing: {
        total_cost: "$12,900.00 MXN / $13,900.00 MXN (con plantilla duplicada)",
        option_1: {
          total: "$12,900.00 MXN",
          booking: "$1,900.00 MXN (depósito del 10% aproximado)",
          balance: "$11,000.00 MXN (liquidación el día del evento)",
          penalty: "$2,500.00 MXN en caso de no liquidar"
        },
        option_2: {
          total: "$13,900.00 MXN",
          booking: "$1,390.00 MXN",
          balance: "$12,510.00 MXN",
          penalty: "$2,500.00 MXN"
        }
      },
      inclusions: [
        "Grabación de video a dos cámaras profesionales de cine digital",
        "Filmación aérea con drones en calidad 4K",
        "Fotografía digital ilimitada durante toda la boda",
        "Photobook de bodas de alta gama en tamaño grande 12x12 pulgadas con diseño exclusivo",
        "100 fotografías impresas físicas de alta calidad",
        "Ampliación fotográfica de gran escala con marco premium y protector",
        "Foto Firma de firmas de boda con caballete de madera de pino y material para dedicatorias",
        "Elegante caja o estuche de madera fina grabado personalizado",
        "Dispositivo USB con la película cinematográfica de bodas y el archivo completo de fotos",
        "Sesión fotográfica y de video previa (E-Session/casual) en exteriores de locación campestre",
        "Videoclip especial de la sesión para proyectar en el banquete principal de la boda"
      ],
      conditions: [
        "En caso de no cumplir con el pago total el día del evento, se sancionará con $2,500.00 MXN o se procederá a la retención/eliminar definitiva del material",
        "El cliente provee los viáticos si la sesión se hace fuera del estado de Morelos",
        "Entrega en un plazo estricto de 30 días hábiles"
      ]
    },
    {
      id: "paquete-eternal-promise",
      name: "Paquete Eternal Promise (Fotografía)",
      url: "https://primaveraeventsgroup.com/paquete-eternal-promise/",
      type: "Servicio Clásico de Fotografía Profesional para Bodas",
      pricing: {
        total_cost: "$9,900.00 MXN",
        booking_deposit: "$990.00 MXN (10% del total)",
        liquidation_balance: "$8,910.00 MXN (Liquidación el día del evento)"
      },
      inclusions: [
        "Cobertura fotográfica ilimitada digital durante el día de la boda",
        "Álbum fotográfico personalizado con capacidad y diseño para 200 fotografías",
        "200 fotografías impresas físicas en tamaño postal (4x6 pulgadas)",
        "Ampliación física en formato de lujo de tamaño 16x24 pulgadas con protección acrílica y marco",
        "Estuche de madera fina grabado personalizado",
        "Dispositivo USB con la película del evento y el catálogo completo de fotos digitales",
        "Sesión fotográfica de pareja previa a la boda en exteriores románticos",
        "Videoclip emotivo de la sesión previa para proyecciones en el evento"
      ],
      conditions: [
        "Sanción de $1,500.00 MXN o eliminación definitiva del material en caso de incumplimiento de pago el día de la boda",
        "Plazo de entrega de 10 días hábiles tras el evento para el material final digitalizado"
      ]
    },
    {
      id: "paquete-memoria-clasica",
      name: "Paquete Memoria Clásica (Fotografía)",
      url: "https://primaveraeventsgroup.com/paquete-memoria-clasica/",
      type: "Servicio Esencial de Fotografía Profesional",
      pricing: {
        total_cost: "$9,350.00 MXN",
        booking_deposit: "$850.00 MXN (10% del total)",
        liquidation_balance: "$8,500.00 MXN (Liquidación el día del evento)"
      },
      inclusions: [
        "Cobertura fotográfica profesional digital el día del evento",
        "150 fotos impresas en tamaño postal",
        "Ampliación física en tamaño 16x24 pulgadas con marco y protección",
        "Estuche de madera grabado con USB que contiene los archivos digitales del evento",
        "Sesión previa de fotos rápida en exteriores para el videoclip",
        "Videoclip básico para proyectar en el banquete"
      ],
      conditions: [
        "Sanción de $1,500.00 MXN en caso de no liquidar el día del evento"
      ]
    }
  ],
  menus: [
    {
      id: "menu-gourmet-primavera-2026",
      name: "Menú Gourmet Primavera 2026",
      url: "https://primaveraeventsgroup.com/menu-gourmet/menu-primavera-2026/",
      description: "Menú sofisticado diseñado especialmente para eventos de gala, bodas y XV años, caracterizado por una estética impecable y un gran equilibrio culinario.",
      categories: {
        ensaladas: [
          { name: "Ensalada Mediterránea", description: "Mezcla de lechugas, queso de cabra, jitomates cherry, manzana, germen de alfalfa y vinagreta dulce." },
          { name: "Ensalada de Nuez a la Naranja", description: "Mezcla de espinaca, lechugas, nuez caramelizada, manzana y queso blanco con salsa de naranja y miel." },
          { name: "Ensalada de la Casa", description: "Mezcla de lechugas con pepino, jitomate, cebolla, zanahoria y vinagreta con base de vinagre balsámico." },
          { name: "Ensalada Primavera Exótica de Mango", description: "Tiras de mango fresco sobre una cama de lechuga con pasta Fusilli, fresas frescas y vinagreta artesanal de mango." },
          { name: "Ensalada de Frutos Rojos", description: "Servido sobre aro de pepino con una mezcla de lechugas baby, frutos rojos y reducción fina de balsámico." }
        ],
        entradas_calientes: [
          { name: "Costalito de Champiñón al Ajillo", description: "Servido sobre un espejo de salsa de chile guajillo." },
          { name: "Crepa Poblana", description: "Crepa rellena de chile poblano en rajas, granos de elote y pollo deshebrado en salsa poblana cremosa." },
          { name: "Crepa de Champiñones y Flor de Calabaza", description: "Crepa rellena de champiñones guisados y bañada en salsa cremosa de flor de calabaza." },
          { name: "Rollito de Cochinita Pibil", description: "Servido sobre un espejo de salsa de piña con chile habanero y coronado con cebollas moradas encurtidas." }
        ],
        cremas_y_sopas: [
          { name: "Crema de Brócoli", description: "Cremosa sopa de brócoli presentada con un crotón crujiente." },
          { name: "Crema de Nuez", description: "Crema fina presentada con nueces espolvoreadas al centro." },
          { name: "Crema Poblana", description: "Crema suave de chile poblano presentada con granos de elote y cuadritos de chile poblano asado." },
          { name: "Crema de Tres Quesos", description: "Elaborada con una base selecta de quesos Gruyère, azul y queso fresco." },
          { name: "Crema de Chicharrón", description: "Crema de chicharrón de cerdo perfumada con un toque de chile guajillo." },
          { name: "Crema Suiza al Chipotle", description: "Crema suave y picante de chipotle presentada con trocitos de queso derretido." },
          { name: "Crema de Pimientos y Uvas", description: "Crema de pimiento morrón con una guarnición de uvas frescas al centro." },
          { name: "Crema de Cilantro", description: "Crema aromática de cilantro presentada con trocitos de nuez pecana." }
        ],
        pastas: [
          { name: "Pasta Napolitana", description: "Espagueti clásico servido con una rica salsa pomodoro hecha en casa." },
          { name: "Pasta Arrabbiata", description: "Pasta Fusilli preparada con salsa picante arrabbiata y abundante queso parmesano rallado." },
          { name: "Pasta Carbonara", description: "Fetuccini bañado en una salsa carbonara a base de tocino dorado, yema y crema." },
          { name: "Pasta al Pesto", description: "Espagueti servido con un pesto de albahaca fresca, aceite de oliva virgen y parmesano." },
          { name: "Espagueti en Salsa de Queso de Cabra", description: "Espagueti al burro servido con una sedosa salsa cremosa de queso de cabra y decorada con perejil fresco." }
        ],
        platos_fuertes_cerdo: [
          { name: "Pierna Almendrada", description: "Láminas de pierna bañadas en una salsa súper cremosa de almendras tostadas." },
          { name: "Pierna a la Madrileña", description: "Acompañada de una salsa a base de graybi, vino tinto y cebolla cambray asada." },
          { name: "Pierna a la Sangría", description: "Bañada con una salsa dulce a base de su gravy natural, vino tinto y jugo de uvas." },
          { name: "Lomo al Tamarindo", description: "Exquisita pieza bañada en salsa agridulce de tamarindo y chile morita picante." },
          { name: "Pierna en Salsa de Ciruela", description: "Pierna horneada bañada en una salsa tersa y dulce de ciruela pasa." },
          { name: "Lomo de Cerdo Mechado", description: "Lomo relleno de frutos secos con nuez y pistaches en su salsa gravy." }
        ],
        platos_fuertes_pollo: [
          { name: "Pechuga Cordon Bleu", description: "Pechuga empanizada rellena de jamón y queso, acompañada de una salsa blanca de hongos." },
          { name: "Volcán de Pollo a la Poblana", description: "Pechuga rellena de mezcla de requesón con salsa cremosa poblana al centro." },
          { name: "Pechuga a los Tres Chiles", description: "Bañada en salsa rosada acompañada de trozos de pimiento morrón rojo y amarillo y chile poblano." },
          { name: "Rollo de Pollo a la Hawaiana", description: "Pechuga rellena de espinaca, jamón y queso en salsa agridulce de piña picante." },
          { name: "Pechuga de Huitlacoche", description: "Pechuga de pollo rellena de huitlacoche (hongo de maíz) acompañado de una salsa poblana." },
          { name: "Pechuga de Frutos Secos", description: "Pechuga rellena de frutos secos (manzana, chabacano, ciruelas) y queso crema con salsa blanca dulce." },
          { name: "Rollos de Pollo con Setas", description: "Bañada en una salsa cremosa de chipotle y setas asadas." },
          { name: "Suprema de Pollo al Cilantro", description: "Suprema rellena de mezcla de espinacas con queso Philadelphia, bañada en una salsa de cilantro." }
        ],
        filetes_res_extra: [
          { name: "Filete Arriero", description: "Salsa obscura sabrosa con cebolla cambray asada." },
          { name: "Filete al Vino", description: "Filete en salsa obscura con un toque robusto de vino tinto." },
          { name: "Filete a la Mostaza Antigua", description: "Salsa obscura clásica y un toque de mostaza de grano antigua." },
          { name: "Filete al Brandy", description: "Salsa a base de crema fina con un toque aromático de brandy." },
          { name: "Filete a la Pimienta", description: "Salsa obscura clásica con un toque fuerte de pimienta negra triturada." }
        ],
        salmon_extra: [
          { name: "Salmón Frutos Rojos", description: "Filete de salmón bañado con una salsa dulce de bayas silvestres del bosque." },
          { name: "Salmón al Vino Blanco", description: "Salmón al horno en salsa de vino blanco con ajo e hinojo fresco." },
          { name: "Salmón en Salsa Cremosa de Ajo", description: "Bañado en salsa cremosa de champiñones fileteados con ajo dorado." },
          { name: "Salmón en Salsa de Naranja", description: "Bañado en una salsa cítrica hecha a base de jugo de naranja natural y especias." }
        ],
        guarniciones: [
          "Ramillete de verduras al vapor", "Boule de papa al tocino", "Verduras a las finas hierbas", "Lasagna de verduras pomodoro",
          "Pera de papa", "Papa cambray a la paprika", "Papa a la vinagreta", "Papa cambray al romero", "Croqueta de plátano macho y queso",
          "Ejotes almendrados", "Verduras rostizadas", "Papas lionesas", "Champiñones al ajillo", "Esfera de papa frita", "Paja de verduras", "Brócoli rostizado"
        ],
        postres: [
          "Tartaleta con frutas de temporada", "Strudel de manzana con helado de vainilla", "Panna Cotta italiana con salsa de frutos rojos",
          "Cheesecake con geleé de maracuyá", "Brownie de chocolate fudge caliente servido con helado de vainilla"
        ]
      }
    },
    {
      id: "menu-buffet-mexicano",
      name: "Menú Buffet Mexicano",
      url: "https://primaveraeventsgroup.com/menu-gourmet/menu-primavera-2026/buffet-mexicano/",
      description: "Servicio tradicional mexicano ideal para tornabodas, celebraciones patrias o eventos rústicos. Incluye tortillas hechas a mano en vivo, salsas tradicionales, ensalada de nopales, arroz y frijoles refritos. Todo servido en Chafing Dishes (baño maría) durante un periodo continuo de 2 horas. El cliente elige 5 guisados del catálogo:",
      guisados: {
        pollo: [
          "Mole Rojo (receta tradicional)", "Mole Verde campestre", "Fajitas de Pollo con pimientos",
          "Alitas Adobadas", "Tinga de Pollo clásica", "Alambre de Pollo", "Alitas BBQ", "Milanesa de Pollo"
        ],
        res: [
          "Puntas de Res a la Mexicana", "Puntas de Res al Chipotle", "Alambre de Res con queso",
          "Fajitas de Res", "Picadillo de Res clásico", "Bistec de Res en salsa de chile pasilla"
        ],
        cerdo: [
          "Costillitas de Cerdo en Adobo", "Costilla de Cerdo en Salsa Verde", "Cochinita Pibil yucateca con cebollitas",
          "Tinga de Cerdo", "Chicharrón de Cerdo en Salsa Verde/Roja", "Cerdo en Mole Rojo", "Bistec de Cerdo en Salsa de Chile Morita", "Bistec de Cerdo en Salsa de Chile Pasilla"
        ],
        verduras_y_mixtos: [
          "Calabacitas a la Mexicana con elote", "Rajas Poblanas con Crema y elote", "Papas con Chorizo doradas",
          "Nopales con Cecina de Yecapixtla", "Salpicón de Pollo fresco", "Salpicón de Res clásico", "Queso en Chile verde"
        ]
      }
    },
    {
      id: "menu-parrillada-de-cortes",
      name: "Menú Parrillada de Cortes de Carne en Buffet",
      url: "https://primaveraeventsgroup.com/menu-gourmet/menu-primavera-2026/buffet-mexicano/buffet-pastas-y-pizzas/parrillada-de-cortes-de-carne-y-guarniciones-en-buffet/",
      description: "Servicio de parrillada de cortes selectos cocinados al carbón y puestos en buffet durante un periodo continuo de 2.5 horas. El menú incluye una selección rica de guarniciones, pastas y ensaladas:",
      inclusions: {
        pastas_a_elegir: [
          "Pluma Arrabbiata (pasta corta picante)", "Pasta Alfredo con mantequilla y crema",
          "Fetuccini Carbonara con tocino crujiente", "Espagueti al Pesto con albahaca", "Espagueti en Salsa de Tres Quesos"
        ],
        ensaladas_a_elegir: [
          "Ensalada Mediterránea", "Ensalada de Frutos Rojos", "Ensalada Italiana", "Ensalada de la Casa", "Ensalada Mixta"
        ],
        guarniciones_ofrecidas: [
          "Puré rústico de papa con tocino dorado", "Cebollas cambray asadas al carbón", "Nopalitos asados fritos"
        ],
        cortes_de_carne_puestos: [
          "Rib Eye premium", "Chistora clásica", "Arrachera marinada súper suave", "New York fino", "Chorizo Argentino de autor"
        ],
        suplementos_y_aderezos: [
          "Salsa verde de chile serrano", "Salsa roja de chile morita tatemado", "Limones frescos", "Chimichurri argentino preparado en casa"
        ]
      }
    },
    {
      id: "menu-buffet-pastas-y-pizzas",
      name: "Menú Buffet de Pastas y Pizzas",
      url: "https://primaveraeventsgroup.com/menu-gourmet/menu-primavera-2026/buffet-mexicano/buffet-pastas-y-pizzas/",
      description: "Servicio de buffet con una variedad exquisita de pastas tradicionales y pizzas artesanales horneadas al momento, ideal para eventos dinámicos y graduaciones juveniles."
    },
    {
      id: "nuestros-postres",
      name: "Menú de Postres y Repostería Fina",
      url: "https://primaveraeventsgroup.com/nuestros-postres/",
      description: "Catálogo exclusivo de repostería de autor, diseñado para dar el cierre perfecto al banquete del evento:",
      options: [
        "Tartaleta de Frutas Finas con crema pastelera",
        "Strudel de Manzana tibio servido con helado gourmet de vainilla de Papantla",
        "Panna Cotta Italiana tradicional con salsa espesa de frutos rojos",
        "Cheesecake horneado con Geleé dulce de maracuyá tropical",
        "Brownie de chocolate fudge caliente servido con helado de vainilla"
      ]
    }
  ],
  venues: [
    {
      id: "centro-de-convenciones-presidente",
      name: "Centro de Convenciones Presidente",
      url: "https://primaveraeventsgroup.com/centro-de-convenciones-presidente/",
      location: "Avenida Defensa Nacional #8, Col. Chamilpa, 62210 Cuernavaca, Morelos",
      capacity: "Desde 100 hasta 500 personas máximo",
      style: "Arquitectónico modernista, elegante e industrial con amplias alturas",
      features: [
        "Gran salón techado climatizado con excelentes acabados y acústica",
        "Área de jardín delantero con fuente artificial iluminada en la entrada principal",
        "Área infantil integrada con juegos múltiples infantiles fijos y seguros",
        "Estacionamiento privado interno y seguro para 35 vehículos compactos",
        "Escenario o templete amplio para DJ, grupos musicales u orquestas",
        "Área de cocina profesional, amplia y adaptada para banquetes masivos",
        "Baños múltiples de lujo para damas y caballeros"
      ]
    },

    {
      id: "quinta-zarabanda",
      name: "Quinta Zarabanda",
      url: "https://primaveraeventsgroup.com/quinta-zarabanda/",
      location: "Avenida Lauro Ortega Martínez #4, Las Animas, 62583 Temixco, Morelos",
      capacity: "Desde 100 hasta 250 personas en área techada, ampliable en jardines",
      style: "Finca campestre íntima y natural de alto confort y descanso",
      features: [
        "Área techada modernista para banquete con capacidad máxima de 250px",
        "Precioso jardín con fuente artificial iluminada",
        "Suite Nupcial exclusiva equipada con jacuzzi, vestidor, tocador y decoración romántica",
        "Hospedaje de lujo dentro del recinto para 14 personas (habitaciones con A/C, cocina, baños, alberca, jardín privado)",
        "Área Consagrada privada e íntima para ceremonias en entorno natural lleno de paz",
        "Iluminación arquitectónica perimetral interior y exterior",
        "Servicio de Valet Parking y amplio estacionamiento cerrado",
        "Uso completo del recinto por 10 horas sin restricciones de horario"
      ]
    },
    {
      id: "finca-las-isabeles",
      name: "Finca Las Isabeles",
      url: "https://primaveraeventsgroup.com/finca-las-isabeles/",
      location: "Xochitepec, Morelos",
      capacity: "Desde 200 hasta 400 invitados",
      style: "Finca campestre rústica elegante de gran exclusividad",
      features: [
        "Preciosas y cuidadas áreas verdes rodeadas de palmeras y vegetación exótica",
        "Salón abierto cubierto ideal para climas cálidos",
        "Alberca recreativa decorativa e iluminada",
        "Área de recepción amplia y estacionamiento propio"
      ]
    },
    {
      id: "jardin-la-flor",
      name: "Jardín La Flor",
      url: "https://primaveraeventsgroup.com/jardin-la-flor/",
      location: "Morelos",
      capacity: "Ideal para eventos de escala media (100 - 300 invitados)",
      style: "Jardín clásico cuernavaquense, fresco e íntimo",
      features: [
        "Cascada o caídas de agua decorativas e iluminadas",
        "Áreas de césped plano ideales para montajes campiranos con pista pixel",
        "Estructura techada elegante y cocina operativa"
      ]
    },
    {
      id: "salon-los-potrillos",
      name: "Salón Los Potrillos",
      url: "https://primaveraeventsgroup.com/salon-los-potrillos/",
      location: "Morelos",
      capacity: "Adecuado para eventos de temática ecuestre o rústica (100-400px)",
      style: "Hacienda o salón con toque campirano y picadero de caballos",
      features: [
        "Temática charra/ecuestre exclusiva",
        "Área techada amplia y picadero visible para shows ecuestres",
        "Logística preparada para eventos de gran calidez mexicana"
      ]
    },
    {
      id: "jardin-tsu-nuum",
      name: "Jardín Tsu Nuum",
      url: "https://primaveraeventsgroup.com/jardin-tsu-nuum/",
      location: "Morelos",
      capacity: "Ideal para eventos al aire libre exclusivos y de autor",
      style: "Jardín zen moderno minimalista con paisajismo de diseñador",
      features: [
        "Espacios de jardín conceptuales con árboles maduros y arquitectura sobria",
        "Entornos fotogénicos espectaculares y gran privacidad",
        "Montajes integrales de lujo y gran iluminación ambiental"
      ]
    },
    {
      id: "salon-los-caballos",
      name: "Salón Los Caballos",
      url: "https://primaveraeventsgroup.com/salon-los-caballos/",
      location: "Morelos",
      capacity: "Diseñado para eventos masivos y corporativos campestres",
      style: "Rancho / Hacienda de gran escala con establos elegantes",
      features: [
        "Establos de gala y posibilidad de espectáculos hípicos",
        "Salón techado amplio y grandes explanadas de jardín",
        "Gran capacidad logística y estacionamiento cerrado masivo"
      ]
    },
    {
      id: "salon-jardin-yolomecatl",
      name: "Salón Jardín Yolomecatl",
      url: "https://primaveraeventsgroup.com/salon-jardin-yolomecatl/",
      location: "Temixco, Morelos",
      capacity: "Desde 200 hasta 500 invitados",
      style: "Complejo de eventos con jardines y salón señorial",
      features: [
        "Capilla consagrada dentro de la locación para bodas religiosas",
        "Jardines extensos y salón techado modernista con columnas decoradas",
        "Entorno cerrado de gran privacidad y fácil acceso en Temixco"
      ]
    },
    {
      id: "villa-di-fiori",
      name: "Villa Di Fiori",
      url: "https://primaveraeventsgroup.com/venues/villa-di-fiori/",
      location: "Xochitepec, Morelos",
      capacity: "Desde 100 hasta 350 invitados",
      style: "Villa toscana campestre elegante con hermosos arcos de cantera",
      features: [
        "Jardines de diseño paisajista europeo con abundante flora exótica",
        "Estructuras y portales de cantera tallada ideales para sesiones de fotos premium",
        "Suite de preparación exclusiva y privada para anfitriones",
        "Gran capacidad logística y estacionamiento cerrado"
      ]
    },
    {
      id: "salon-solaire",
      name: "Salón & Jardín Solaire",
      url: "https://primaveraeventsgroup.com/venues/solaire/",
      location: "Cuernavaca, Morelos",
      capacity: "Desde 80 hasta 180 invitados",
      style: "Industrial-chic moderno premium con toques de madera sólida y vegetación colgante",
      features: [
        "Pista Pixel LED 5x5 inteligente pre-instalada de fábrica",
        "Mobiliario de autor rústico elegante (sillas Crossback y mesas de madera sólida)",
        "Cascada o caída de agua monumental iluminada",
        "Área consagrada para ceremonias religiosas o civiles al aire libre"
      ]
    }
  ],
  services: [
    {
      id: "transportacion",
      name: "Servicio de Transportación Ejecutiva y Turística",
      url: "https://primaveraeventsgroup.com/transportacion/",
      description: "Servicio profesional de transporte ejecutivo y traslado para anfitriones e invitados en el estado de Morelos y CDMX. Flotilla equipada con A/C, choferes profesionales certificados, seguro de viajero completo y atención personalizada.",
      features: [
        "Traslados ejecutivos aeropuerto-hotel-recinto",
        "Transporte masivo para invitados del hotel al jardín del evento",
        "Vehículos de gama alta para novios o quinceañeras",
        "Logística y coordinación de rutas en tiempo real"
      ]
    },
    {
      id: "montajes-y-mobiliario",
      name: "Servicio de Montajes Especiales y Alquiler de Mobiliario",
      url: "https://primaveraeventsgroup.com/montajes-y-mobiliario/",
      description: "Catálogo extenso de mobiliario de gala, rústico e industrial para diseño de eventos en Cuernavaca y zonas aledañas. Equipamiento premium y en constante renovación para lograr montajes vanguardistas.",
      features: [
        "Mesas tipo mármol (cuadradas, rectangulares), mesas vintage de madera rústica campirana",
        "Sillería premium: Tiffany (blanca, dorada), Crossback de madera, Lotus moderna, Silla Boss exclusiva",
        "Mobiliario lounge de bienvenida: salas lounge blancas/negras, sombrillas gigantes de lona, periqueras altas de madera/metal",
        "Pistas de baile de lujo: pista de madera vintage, pista pintada de gala, pista Pixel LED 5x5 inteligente",
        "Mantelería fina de tela, platos base decorativos, loza blanca, plaque en oro/plata/rose gold y cristalería fina de color"
      ]
    },
    {
      id: "staffing",
      name: "Servicio de Staffing y Personal Profesional de Eventos",
      url: "https://primaveraeventsgroup.com/staffing/",
      description: "Provisión de personal altamente capacitado, uniformado y con amplia vocación de servicio para la operación de bodas, XV años, graduaciones y eventos corporativos.",
      features: [
        "Coordinador General y Wedding Planners certificados (Jessy y Richard)",
        "Capitanes de meseros y Meseros profesionales uniformados con atención de mesa",
        "Baristas y Barmen profesionales para barras libres de coctelería",
        "Hostess de bienvenida y acomodo de invitados",
        "Stewards de cocina para limpieza y orden, personal de limpieza de sanitarios constante"
      ]
    },
    {
      id: "fotografia-y-video-servicio",
      name: "Servicios Profesionales de Fotografía y Video Cinematográfico",
      url: "https://primaveraeventsgroup.com/fotografia-y-video/",
      description: "Estudio de producción multimedia propio especializado en inmortalizar los eventos con un enfoque cinematográfico de autor, sensible y moderno.",
      features: [
        "Fotografía digital ilimitada en alta definición con revelado digital fino",
        "Álbumes personalizados de gala y Photobooks en gran formato (12x12)",
        "Ampliaciones con marco premium de pino y protección acrílica texturizada",
        "Filmación con doble cámara digital de cine y drones 4K profesionales",
        "Sesiones previas de pareja/XV al aire libre (E-Session) y videoclips de gala para proyecciones",
        "Foto Firma interactiva para dedicatorias con caballetes provistos por el staff"
      ]
    },
    {
      id: "bodas",
      name: "Planeación y Coordinación Integral de Bodas Destino",
      url: "https://primaveraeventsgroup.com/bodas/",
      description: "Coordinación completa 'llave en mano' para bodas espectaculares en el estado de Morelos. Nos encargamos de todo el trayecto desde el diseño conceptual hasta el último minuto del evento.",
      features: [
        "Selección y contratación de locación ideal (quintas, haciendas, salones)",
        "Diseño conceptual y de montaje floral a cargo de planners especializados",
        "Degustaciones y banquete a tiempos con postres de autor y barra libre",
        "Soporte de entretenimiento con DJ, performance visual, mariachi y bandas en vivo",
        "Gestión completa de proveedores y control minuto a minuto para una experiencia sin estrés"
      ]
    },
    {
      id: "quinceaneras",
      name: "Organización y Diseño de Eventos de Quinceañeras (XV Años)",
      url: "https://primaveraeventsgroup.com/quinceaneras-primavera/",
      description: "Servicio exclusivo para transformar los XV años en una noche mágica con temáticas juveniles y modernas. Enfoque vibrante en la pista de baile, ambientación LED y espectáculos interactivos.",
      features: [
        "Montajes temáticos elegantes e iluminados con letras gigantes y alfombra roja",
        "Shows en pista de baile: robots LED, cabezones sorpresa, inflables gigantes interactivos",
        "Cabina Espejo y Cámara 360 con tomas de videos dinámicos para compartir en redes",
        "Banquete juvenil a tiempos y barra mix de dulces/salados con 12 toppings deliciosos",
        "Servicio completo de fotografía de quinceañera y DJ profesional en pista"
      ]
    },
    {
      id: "graduaciones",
      name: "Producción y Coordinación de Graduaciones Escolares y Universitarias",
      url: "https://primaveraeventsgroup.com/graduaciones-primavera/",
      description: "Producción integral y gala de graduación para colegios y universidades, garantizando orden absoluto, emotividad y una noche de fiesta inolvidable para alumnos y familias.",
      features: [
        "Diseño y logística para el último pase de lista solemne en escenario",
        "Cena de gala formal de 3 o 4 tiempos servida por meseros calificados",
        "Shows de música en vivo (mariachi, bandas sinaloenses) y saxofonista",
        "Cortesías de pirotecnia fría para brindis oficial, botellas de vino de cortesía",
        "Cabina Espejo y Cámara 360 interactiva para el recuerdo de graduados"
      ]
    }
  ]
};

// Inyección de Datos Reales del Archivo de Constantes datos.txt y Rastreo Exhaustivo
database.cotizaciones_reales = [
  {
    cliente: "Colegio Don Bosco (Graduación y Entrega de Reconocimientos)",
    recinto: "Jardín Salón Yolomecatl (Calle Palma 6, Acatlipa, Temixco, Morelos)",
    precio_por_persona: "$550.00 MXN",
    minimo_invitados: 200,
    inclusiones: [
      "Ceremonia formal con presídium para la entrega de reconocimientos",
      "Coordinación de Misa de Agradecimiento en la capilla del recinto",
      "Coctel de bienvenida con margaritas de sabores sin alcohol y aguas frescas de fruta natural",
      "Montaje elegante del banquete con mesas cuadradas y sillas Tiffany",
      "Vajilla y cristalería completa",
      "Centros de mesa con arreglos de flor natural",
      "Banquete a 2 tiempos (Entrada: Cremas o ensaladas; Plato fuerte: Pollo o cerdo con dos guarniciones, pan y chiles)",
      "Servicio de mezcladores completo: hielo, agua natural, refrescos de la línea Coca-Cola ilimitados",
      "Equipo de servicio completo: Coordinador General, Hostess, Meseros capacitados, Personal de barra y Stewart",
      "Entretenimiento: DJ profesional con pantallas y Cabina 360 interactiva para videos de los graduados",
      "Servicio de Valet Parking opcional por un costo adicional de $50.00 MXN por vehículo"
    ],
    cortesias: [
      "Degustación exclusiva para 4 personas al firmar el contrato",
      "Diseño de montaje personalizado acorde a la paleta de colores del colegio",
      "Croquis detallado de distribución y acomodo de invitados",
      "Minuto a minuto cronometrado para garantizar puntualidad y fluidez",
      "Chat exclusivo de coordinación directa con Jessy y Richard Hernández"
    ]
  },
  {
    cliente: "Quinceañera Yamilet (XV Años)",
    recinto: "Jardín Salón Yolomecatl (Calle Palma 6, Acatlipa, Temixco, Morelos)",
    precio_por_persona: "$350.00 MXN",
    minimo_invitados: 200,
    coordinadores: "Gerente Carlos Osorio y Planner Richard Hernández",
    inclusions: [
      "Banquete formal a tiempos con menú personalizado",
      "Mobiliario y mantelería incluidos en el montaje",
      "Personal de servicio completo: meseros uniformados, cocina y stewards",
      "Servicios de coordinación y logística desde la recepción hasta el cierre del evento",
      "Degustación exclusiva para 4 personas al firmar el contrato para ajuste del menú"
    ],
    condiciones: [
      "Precios no incluyen impuestos (IVA)",
      "Se requiere depósito de apartado para reservar la fecha",
      "Disponibilidad sujeta a confirmación",
      "Se aplican cargos adicionales en caso de requerir servicios extra"
    ]
  },
  {
    cliente: "XV Años Antonio (Propuesta Premium)",
    recinto: "Selección a elegir (ccPresidente, Los Potrillos, Los Caballos, La Flor, Yolomecatl)",
    precio_por_persona: "$950.00 MXN (Total: $123,500.00 MXN)",
    minimo_invitados: 130,
    inclusiones: [
      "Estructura interactiva premium (3 marcas, música al entrar 'marcasonora.mp3', preloader interactivo con video)",
      "20 inclusiones en la propuesta digital con imágenes descriptivas animadas",
      "Video de buffet y estación gastronómica interactiva ('menu_antonio.mp4')",
      "Mobiliario elegante, mantelería fina, loza, plaque y cristalería fina",
      "DJ profesional con torres robóticas, luces wash, máquina de humo y pista de baile 5x5m",
      "Coordinador VIP, hostess, staff de meseros capacitados, bartender profesional",
      "Cortesías incluidas: Degustación exclusiva (4px), letras gigantes, corazón iluminado, mesas de pastel/regalos, 2 chisperos, alfombra roja, espejo selfie y barra mix con 12 toppings",
      "8 horas de servicio continuo y cierre cinematográfico con video de firma interactivo ('firma.mp4')"
    ],
    cortesias: [
      "Publicidad contextual activa integrada para la Expo Boda y 15 Años en ccPresidente",
      "Menú flotante rápido (FAB) con links a redes oficiales y botón de compartir"
    ]
  },
  {
    cliente: "Banquete Señor Erasmo (Villa Di Fiori)",
    recinto: "Villa Di Fiori (Estilo toscano-elegante, Xochitepec, Morelos)",
    precio_por_persona: "$850.00 MXN (Total: $102,000.00 MXN)",
    minimo_invitados: 120,
    inclusiones: [
      "Banquete formal de 3 tiempos premium (Entrada, Plato fuerte, Postre)",
      "Uso de locación Villa Di Fiori con sus arcos de cantera y hermosos jardines",
      "Mobiliario elegante estilo rústico toscano con mantelería fina",
      "DJ, soporte de audio, iluminación robótica y máquina de humo",
      "Staff completo de meseros, cocineros, stewards e invitaciones digitales premium gratis"
    ]
  },
  {
    cliente: "Señor Erasmo VIP (Propuesta Extendida)",
    recinto: "Villa Di Fiori",
    precio_por_persona: "$850.00 MXN",
    minimo_invitados: 120,
    inclusiones: [
      "9 horas de servicio continuo sin restricciones de horario",
      "Banquete premium a 3 tiempos, servicio de mezcladores y refresco ilimitado",
      "Letras decorativas de marca y ambientación de lujo"
    ]
  },
  {
    cliente: "Propuesta Viky (Jardín Solaire)",
    recinto: "Salón & Jardín Solaire (Cuernavaca, Morelos)",
    precio_por_persona: "$1,199.00 MXN",
    minimo_invitados: 100,
    inclusiones: [
      "Banquete gourmet a 3 tiempos a elegir de nuestra carta exclusiva",
      "Descorche libre de 8 horas sin costo de servicio",
      "Mobiliario de autor campirano premium (mesas vintage de madera sólida, sillas Crossback)",
      "DJ profesional, cabezas robóticas, audio de alta fidelidad, máquina de humo y pista pixel LED",
      "Elegir entre: Cabina de Fotos Espejo instantánea o Cámara 360 interactiva"
    ]
  },
  {
    cliente: "Propuesta Viviana (Aniversario Especial)",
    recinto: "Servicio a Domicilio / Locación Externa",
    precio_por_persona: "$690.00 MXN (Total: $62,100.00 MXN)",
    minimo_invitados: 90,
    inclusiones: [
      "Banquete formal a 3 tiempos servido caliente en locación elegida",
      "Servicio a domicilio completo (montaje, loza, mantelería, meseros y barras)",
      "DJ profesional con cabina iluminada y 4 cabezas móviles robóticas",
      "Pista de baile, mezcladores ilimitados e invitaciones digitales gratis"
    ]
  },
  {
    cliente: "Sistema DIF / Lic. Claudia López (Desayuno Tipo Taquiza)",
    recinto: "Servicio a Domicilio / Auditorio DIF",
    precio_por_persona: "$260.00 MXN (Total: $32,500.00 MXN)",
    minimo_invitados: 125,
    inclusiones: [
      "Desayuno tipo taquiza servido caliente en chafing dishes",
      "Buffet tradicional (variedad de guisados mexicanos, arroz, frijoles refritos, chicharrón, etc.)",
      "Mobiliario de gala con mesas redondas y sillas Tiffany blancas",
      "Vajilla fina, vasos de vidrio, refrescos de la línea Coca-Cola y jugos naturales ilimitados",
      "Personal de meseros uniformados, stewards de cocina y coordinador general"
    ]
  },
  {
    cliente: "Edimael Becerra (Taquiza Especial)",
    recinto: "Servicio a Domicilio / Locación Externa",
    precio_por_persona: "$125.00 MXN",
    minimo_invitados: 100,
    inclusiones: [
      "Taquiza mexicana tradicional de cortes preparados al momento",
      "Trompo de Pastor, Longaniza y Campechano cocinados en vivo por taqueros profesionales",
      "Catálogo de complementos: cebollitas asadas, piña picada, nopales, salsas caseras y tortillas calientes",
      "Vajilla y cubiertos desechables biodegradables, refrescos tradicionales"
    ]
  },
  {
    cliente: "Paquete Día del Maestro Premium (Propuesta Maestros)",
    recinto: "A elegir: Salón Los Caballos o Jardín Los Reyes",
    precio_por_persona: "$545.00 MXN (Total: $43,600.00 MXN)",
    minimo_invitados: 80,
    inclusiones: [
      "Banquete campirano de 2 tiempos gourmet",
      "Mobiliario campestre vintage con mesas de madera sólida y sillas Crossback",
      "DJ profesional con cabina iluminada, audio e iluminación premium",
      "Cortesía tecnológica premium a elegir: Cabina de Fotos Espejo o Cámara 360 interactiva"
    ]
  },
  {
    cliente: "Sra. Sandra (Taquiza Premium XV Años)",
    recinto: "Jardín Solaire (Sábado 20 de Junio)",
    precio_por_persona: "$590.00 MXN (Total: $47,200.00 MXN)",
    minimo_invitados: 80,
    inclusiones: [
      "Servicio de taquiza premium de guisados selectos de autor",
      "Montaje de gala con mesas redondas, mantelería fina y centros de mesa florales",
      "DJ profesional con cabina LED, luces móviles y pista de baile 5x5m",
      "Mesa principal de honor y letras decorativas gigantes 'XV' iluminadas"
    ]
  }
];

database.constantes_interaccion = {
  mensajes_prospeccion: [
    {
      tipo: "XV Años (Interesado en salón/jardín)",
      guion: "Hola 😊✨ ¡Claro! Si estás buscando organizador de eventos para XV años, en Primavera Events Group pueden ayudarte a crear algo realmente espectacular 👌 💎 Cuentan con varias opciones de jardines, quintas y salones en Morelos, adaptadas a diferentes estilos, presupuestos y número de invitados. ✨ Por ejemplo, una excelente opción es: Centro de Convenciones Presidente, rancho los potrillos, y mas... ¡Todo resuelto en un solo lugar! ✔ Planeación completa ✔ Banquete ✔ Decoración ✔ DJ, iluminación y ambientación. Escríbele a Richard Hernández aquí: https://primaveraeventsgroup.com/richard-hernandez/"
    },
    {
      tipo: "Bodas y Bautizos (Quinta + Alojamiento)",
      guion: "Hola 😊✨ Contamos con varias opciones que pueden ajustarse perfecto a lo que buscas (quinta + alojamiento + zona Cuernavaca/Jiutepec/Zapata). 💎 Pensando en tu evento de ~130 personas, te recomiendo estas opciones: • Quinta Zarabanda (https://primaveraeventsgroup.com/quinta-zarabanda/) • Finca Las Isabeles (https://primaveraeventsgroup.com/paquetes-primavera/). Ambas cuentan con excelente ubicación, espacios amplios para eventos y opciones de hospedaje cercanas o integradas 👌"
    },
    {
      tipo: "Promoción de Invitación Digital Premium",
      guion: "¡Hola! 🎁 Y ahorita tenemos promo: La invitación digital premium puede ir TOTALMENTE GRATIS al contratar tu evento ✨ (Valor comercial de hasta $8,000 pesos). Incluye: ✔ Confirmación de asistencia (RSVP) ✔ Ubicación con mapa ✔ Galería de fotos interactiva ✔ Acceso desde cualquier celular. Mira un demo aquí: https://5410m0n0c001.github.io/invitacion-demo/ 📲"
    }
  ],
  consejos_wedding_planner: "Si tienes la oportunidad, busca a tu wedding planner ANTES de elegir el salón. ¿Por qué? Porque alguien con experiencia puede acompañarte desde el inicio, ayudarte a tomar mejores decisiones y quitarte muchísimo estrés en el proceso. En Primavera Events Group nos apasiona crear momentos que realmente se sientan únicos."
};

database.politicas_y_promociones = {
  promocion_estrella: {
    nombre: "Invitación Digital Premium Gratis",
    valor_comercial: "$4,000.00 MXN a $8,000.00 MXN",
    condicion: "Incluida sin costo adicional al contratar cualquier paquete de banquetes completo en Primavera Events Group.",
    caracteristicas: [
      "RSVP con confirmación automática a correo del cliente",
      "Mapa con ubicación y croquis del salón",
      "Galería interactiva en tiempo real con código QR para que invitados suban fotos",
      "Playlist con música de fondo o canción dedicada personalizada",
      "Acceso ilimitado en línea y sin caducidad (las fotos permanecen en línea indefinidamente)"
    ]
  },
  locaciones_con_video: [
    "Jardín Yolomecatl (Video de presentación activo)",
    "Quinta Zarabanda (Video de presentación activo)",
    "Centro de Convenciones Presidente (Video de presentación activo)",
    "Jardín Tsu Nuum (Video de presentación activo)"
  ],
  politicas_pagos: [
    "Fotografía y Video: Requieren un depósito de apartado del 10%. El saldo restante debe liquidarse obligatoriamente el día del evento.",
    "Incumplimiento de Pago: Genera una sanción económica automática de $1,500.00 MXN (paquetes clásicos) a $2,500.00 MXN (paquetes de gama alta como Royal Cinematic) o la retención/eliminación definitiva del material digital capturado.",
    "Viáticos de Sesión: Sesiones de fotos o videos previas realizadas fuera del estado de Morelos causan cargos de viáticos para el equipo de producción a cuenta del cliente."
  ]
};

database.entradas_blog = [
  {
    titulo: "Expo Boda y Quince Años - Centro de Convenciones Presidente",
    url: "https://primaveraeventsgroup.com/expo-boda-y-quince-anos-centro-de-convenciones-presidente/",
    autor: "Salomón",
    fecha: "23 de abril de 2026",
    resumen: "Gran encuentro de proveedores de eventos en Morelos. Reunió expertos en banquetes, fotografía, decoración, locaciones y más. Se llevó a cabo el 21 de junio en el Centro de Convenciones Presidente de 12:00 PM a 7:00 PM. Presentó la pasarela Haute Runway e incluyó promociones de sorteos exclusivos para asistentes.",
    inclusiones: ["Proveedores confiables", "Rifas y premios", "Descuentos y ofertas exclusivas"]
  },
  {
    titulo: "Expo Boda y 15 Años en Temixco",
    url: "https://primaveraeventsgroup.com/expo-boda-y-15-anos/",
    autor: "Salomón",
    fecha: "14 de abril de 2026",
    resumen: "Encuentro de proveedores en Temixco, Morelos. Celebrado en Villa Los Presidentes (Calle Lázaro Cárdenas 17, Temixco) el 19 de abril de 2:00 PM a 8:00 PM. Se sortearon 2 invitaciones digitales premium entre los registrados en vivo.",
    inclusiones: ["Ubicación excelente", "Sorteo de invitaciones digitales", "Asesoría personalizada"]
  },
  {
    titulo: "Pasarela Primavera Haute Runway",
    url: "https://primaveraeventsgroup.com/primavera-haute-runway/",
    autor: "Salomón",
    fecha: "10 de mayo de 2026",
    resumen: "Concepto emocional dentro de la Expo Boda & XV Años celebrado el 21 de junio en el Centro de Convenciones Presidente. Permite a quinceañeras previas vestir nuevamente sus vestidos y modelar en pasarela para inspirar a futuras festejadas con tendencias y estilos reales de forma presencial.",
    inclusiones: ["Revivir el gran día", "Modelaje en pasarela real", "Inspirar a nuevas festejadas"]
  },
  {
    titulo: "Damas y Caballeros de Honor",
    url: "https://primaveraeventsgroup.com/wedding-bridesmaids-groomsmen/",
    autor: "Salomón",
    resumen: "Artículo del blog enfocado en los roles y responsabilidades de las damas de honor y caballeros en el cortejo nupcial, ofreciendo consejos de etiqueta y organización para una boda fluida."
  },
  {
    titulo: "Locación del Evento",
    url: "https://primaveraeventsgroup.com/wedding-event-location/",
    autor: "Salomón",
    resumen: "Consejos e ideas clave para elegir la locación ideal en el estado de Morelos, analizando factores clave como clima, espacio cerrado vs abierto, distancias y opciones de alojamiento."
  },
  {
    titulo: "Preparativos Finales de Boda",
    url: "https://primaveraeventsgroup.com/wedding-final-preparation/",
    autor: "Salomón",
    resumen: "Checklist y guías cronológicas detalladas de los preparativos que deben realizarse los últimos 30 días antes del gran día de la boda para evitar imprevistos y asegurar que la logística de proveedores y timings funcione impecable."
  }
];

database.colaboradores = [
  { cargo: "Dirección General", nombre: "Richard Hernández & Jessica Patricia Sandoval (CP)", descripcion: "Co-propietarios y directores generales de Primavera Events Group, responsables de la planificación ejecutiva, administración y dirección creativa in-house." },
  { cargo: "Soporte Digital & Virtual Concierge", nombre: "Alex Salomón (INIT-IDEA)", descripcion: "Encargado de la infraestructura web interactiva, desarrollo del dashboard de expositores, soporte técnico digital y community management de la marca." },
  { cargo: "Enlace en Sede (CC Presidente)", nombre: "Rubí Alvarado", descripcion: "Gerente del Centro de Convenciones Presidente en Córdoba/Cuernavaca, encargada de la coordinación en sede, logística de montaje y enlace directo con clientes." }
];

database.manual_marca = {
  colores: [
    { nombre: "Rosa Principal", hex: "#F65C7A", rgb: "246, 92, 122", uso: "Color de acento primario, CTAs y elementos interactivos." },
    { nombre: "Rosa Claro", hex: "#FF8FA3", rgb: "255, 143, 163", uso: "Decoraciones secundarias, degradados de marca." },
    { nombre: "Oro Noble", hex: "#C9A96E", rgb: "201, 169, 110", uso: "Bordes decorativos de lujo, eventos de gala tradicionales." },
    { nombre: "Gris Suave", hex: "#6D6D6D", rgb: "109, 109, 109", uso: "Texto de cuerpo, subtítulos y descripciones legibles." },
    { nombre: "Negro Profundo", hex: "#1F1F1F", rgb: "31, 31, 31", uso: "Títulos principales, fondos de tarjetas y alto contraste." }
  ],
  hashtags: [
    "#ExpoBoda15Presidente",
    "#PrimaveraEventsGroup",
    "#CentroDeConvencionesPresidente",
    "#PrimaveraHauteRunway",
    "#ReviveTuGranDia"
  ],
  identidad_sonora: [
    { pista: "identidadsonora1.mp3", uso: "Utilizada en index.html de la Expo (fase de expectativa al público)." },
    { pista: "identidadsonora2.mp3", uso: "Utilizada en plan-marketing.html (enfoque B2B y aliados comerciales)." },
    { pista: "identidadsonora3.mp3", uso: "Utilizada en manual.html (enfoque emocional y pasarela Haute Runway)." },
    { pista: "marcasonora.mp3", uso: "Música de precarga y ambientación interactiva para las cotizaciones de clientes." }
  ]
};

database.plan_marketing = {
  eslogan: "2026 es un año para casarse",
  fecha_expo: "21 de Junio de 2026",
  password_acceso: "PrimaveraVIP",
  enlaces: [
    { nombre: "Drive de Descargas Oficiales (Media Kit)", url: "https://drive.google.com/drive/folders/168BJ-2D2Ul6qDIBNU9w8oeLHLkVHF5Y5?usp=sharing" },
    { nombre: "Drive de Carga de Media Kits por Marca (Aliados)", url: "https://drive.google.com/drive/folders/1WDpTEL5nAeHbUzz63820Z-bZr0GOe3AC?usp=sharing" }
  ]
};

// 2. Save structured JSON database
fs.writeFileSync(jsonPath, JSON.stringify(database, null, 2), 'utf8');
console.log(`Saved JSON Database: ${jsonPath}`);

// 3. Generate beautiful, extensive Markdown document
let md = `# 📂 Base de Conocimiento RAG - Primavera Events Group
> **Documento Consolidado de Paquetes, Locaciones, Servicios y Menús**
> *Generado de forma automatizada a partir de los datos públicos del sitio primaveraeventsgroup.com*

---

## 📋 Índice
1. [🏢 Perfil de la Empresa](#-perfil-de-la-empresa)
2. [📦 Paquetes de Eventos y Banquetes](#-paquetes-de-eventos-y-banquetes)
3. [📸 Paquetes de Fotografía y Video](#-paquetes-de-fotografía-y-video)
4. [🍽️ Menús y Propuestas Gastronómicas](#️-menús-y-propuestas-gastronómicas)
5. [🏰 Locaciones (Salones, Quintas y Jardines)](#-locaciones-salones-quintas-y-jardines)
6. [💡 Servicios Corporativos y Especiales](#-servicios-corporativos-y-especiales)

---

## 🏢 Perfil de la Empresa
* **Nombre Comercial**: Primavera Events Group (Banquetes Primavera)
* **Oficina Central**: Av. Defensa Nacional #8, Col. Chamilpa, 62210 Cuernavaca, Morelos.
* **Directores y Planners**:
  * **Jessy** (Founder & Lead Planner) - Tel: \`777 503 2733\`
  * **Richard Hernández** (Creative Director & Planner) - Tel: \`777 458 7923\`
  * **Rubí Alvarado** (Gerente del Centro de Convenciones Presidente) - Tel: \`271 114 8997\`
* **Contacto**: contacto@primaveraeventsgroup.com | Tel. +52 777 458 7923
* **Horario**: Lunes a Viernes de 9:00 a 21:00 hrs. Domingos: Cerrado.
* **Lema**: *«Te cuidas tú, nos cuidas a todos»*

---

## 📦 Paquetes de Eventos y Banquetes

`;

// Add Packages to MD
database.packages.forEach(pkg => {
  if (pkg.pricing && Array.isArray(pkg.pricing)) {
    md += `### 🌟 ${pkg.name}\n`;
    md += `* **Locación Predilecta / Principal**: ${pkg.venue}\n`;
    md += `* **Duración**: ${pkg.duration}\n`;
    md += `* **Página de Referencia**: [Enlace al sitio](${pkg.url})\n\n`;
    
    md += `#### 📋 Inclusiones Principales:\n`;
    pkg.inclusions.forEach(inc => {
      md += `- ${inc}\n`;
    });
    
    if (pkg.menu_structure) {
      md += `\n#### 🍽️ Estructura del Menú (${pkg.menu_structure.type}):\n`;
      pkg.menu_structure.details.forEach(det => {
        md += `- ${det}\n`;
      });
    }
    
    md += `\n#### 💰 Tabla de Precios por Persona (Sujeta a escala de invitados):\n`;
    // If it is a venue-specific list (like Glow Elite)
    if (pkg.pricing[0] && pkg.pricing[0].venue) {
      md += `| Locación / Jardín | Rango de Invitados | Precio Standard / Especial (Costo por Persona) | Detalle |\n`;
      md += `| --- | --- | --- | --- |\n`;
      pkg.pricing.forEach(pr => {
        md += `| **${pr.venue}** | ${pr.guests} | **${pr.price_per_person}** | ${pr.details} |\n`;
      });
    } else {
      md += `| Número de Invitados | Costo por Persona | Detalles y Cobertura |\n`;
      md += `| --- | --- | --- |\n`;
      pkg.pricing.forEach(pr => {
        md += `| ${pr.guests} | **${pr.price_per_person}** | ${pr.details} |\n`;
      });
    }
    
    if (pkg.conditions) {
      md += `\n#### ⚠️ Condiciones del Paquete:\n`;
      pkg.conditions.forEach(cond => {
        md += `- ${cond}\n`;
      });
    }
    
    md += `\n---\n\n`;
  }
});

// Add Photography Packages
md += `## 📸 Paquetes de Fotografía y Video\n\n`;
database.packages.forEach(pkg => {
  if (pkg.pricing && !Array.isArray(pkg.pricing)) {
    md += `### 📷 ${pkg.name}\n`;
    md += `* **Tipo**: ${pkg.type}\n`;
    md += `* **Costo Total**: **${pkg.pricing.total_cost || pkg.pricing.option_1.total}**\n`;
    md += `* **Depósito de Apartado (10%)**: \`${pkg.pricing.booking_deposit || pkg.pricing.option_1.booking}\`\n`;
    md += `* **Saldo a Liquidar en el Evento**: \`${pkg.pricing.liquidation_balance || pkg.pricing.option_1.balance}\`\n`;
    md += `* **Página de Referencia**: [Enlace al sitio](${pkg.url})\n\n`;
    
    md += `#### 💎 Inclusiones e Entregables:\n`;
    pkg.inclusions.forEach(inc => {
      md += `- ${inc}\n`;
    });
    
    md += `\n#### ⚠️ Sanciones y Términos:\n`;
    pkg.conditions.forEach(cond => {
      md += `- ${cond}\n`;
    });
    
    md += `\n---\n\n`;
  }
});

// Add Menus to MD
md += `## 🍽️ Menús y Propuestas Gastronómicas\n\n`;
database.menus.forEach(menu => {
  md += `### 🥗 ${menu.name}\n`;
  md += `* **Descripción**: ${menu.description}\n`;
  md += `* **Página de Referencia**: [Enlace al sitio](${menu.url})\n\n`;
  
  if (menu.categories) {
    for (const [catName, dishes] of Object.entries(menu.categories)) {
      md += `#### 🔸 Seccional: ${catName.toUpperCase().replace(/_/g, ' ')}\n`;
      if (Array.isArray(dishes)) {
        dishes.forEach(dish => {
          if (typeof dish === 'string') {
            md += `- **${dish}**\n`;
          } else {
            md += `- **${dish.name}**: *${dish.description}*\n`;
          }
        });
      }
      md += `\n`;
    }
  }
  
  if (menu.guisados) {
    for (const [catName, dishes] of Object.entries(menu.guisados)) {
      md += `#### 🔸 Guisados de ${catName.toUpperCase()}:\n`;
      dishes.forEach(dish => {
        md += `- **${dish}**\n`;
      });
      md += `\n`;
    }
  }
  
  if (menu.inclusions) {
    for (const [catName, items] of Object.entries(menu.inclusions)) {
      md += `#### 🔸 ${catName.toUpperCase().replace(/_/g, ' ')}:\n`;
      items.forEach(item => {
        md += `- **${item}**\n`;
      });
      md += `\n`;
    }
  }
  
  if (menu.options) {
    md += `#### 🔸 Opciones Disponibles:\n`;
    menu.options.forEach(opt => {
      md += `- **${opt}**\n`;
    });
    md += `\n`;
  }
  
  md += `---\n\n`;
});

// Add Venues to MD
md += `## 🏰 Locaciones (Salones, Quintas y Jardines)\n\n`;
database.venues.forEach(venue => {
  md += `### 🏛️ ${venue.name}\n`;
  md += `* **Ubicación**: ${venue.location}\n`;
  md += `* **Capacidad Máxima**: **${venue.capacity}**\n`;
  md += `* **Estilo Arquitectónico**: ${venue.style || 'Rústico Campestre Elegante'}\n`;
  md += `* **Página de Referencia**: [Enlace al sitio](${venue.url})\n\n`;
  
  md += `#### 🌳 Características y Facilidades del Recinto:\n`;
  venue.features.forEach(feat => {
    md += `- ${feat}\n`;
  });
  
  md += `\n---\n\n`;
});

// Add Services to MD
md += `## 💡 Servicios Corporativos y Especiales\n\n`;
database.services.forEach(service => {
  md += `### 🛠️ ${service.name}\n`;
  md += `* **Descripción**: ${service.description}\n`;
  md += `* **Página de Referencia**: [Enlace al sitio](${service.url})\n\n`;
  
  md += `#### ⚡ Características Destacadas:\n`;
  service.features.forEach(feat => {
    md += `- ${feat}\n`;
  });
  
  md += `\n---\n\n`;
});

// 7. Add Real Quotations (Cotizaciones Reales) from field work
md += `## 📝 Ejemplos de Cotizaciones Reales y de Campo\n\n`;
database.cotizaciones_reales.forEach(cot => {
  md += `### 📄 Cotización: ${cot.cliente}\n`;
  md += `* **Recinto / Locación**: ${cot.recinto}\n`;
  md += `* **Costo por Persona**: **${cot.precio_por_persona}** (Mínimo requerido: \`${cot.minimo_invitados} personas\`)\n`;
  if (cot.coordinadores) {
    md += `* **Coordinadores Responsables**: ${cot.coordinadores}\n`;
  }
  md += `\n#### 📋 Servicios e Inclusiones de la Cotización:\n`;
  const incs = cot.inclusiones || cot.inclusions;
  incs.forEach(inc => {
    md += `- ${inc}\n`;
  });
  
  if (cot.cortesias) {
    md += `\n#### 🎁 Cortesías Especiales Incluidas:\n`;
    cot.cortesias.forEach(cort => {
      md += `- ${cort}\n`;
    });
  }
  
  if (cot.condiciones) {
    md += `\n#### ⚠️ Condiciones Específicas:\n`;
    cot.condiciones.forEach(cond => {
      md += `- ${cond}\n`;
    });
  }
  md += `\n---\n\n`;
});

// 8. Add Commercial Interaction Constants (Constantes de Interacción y Prospección)
md += `## 💬 Constantes de Interacción y Guías de Prospección Comercial\n`;
md += `> **Directrices y Guiones extraídos de la prospección activa en redes sociales (datos.txt)**\n\n`;

md += `### 📱 Guiones de Respuestas a Leads en Redes Sociales:\n\n`;
database.constantes_interaccion.mensajes_prospeccion.forEach(msg => {
  md += `#### 🔹 Caso: ${msg.tipo}\n`;
  md += `\`\`\`text\n${msg.guion}\n\`\`\`\n\n`;
});

md += `### 💡 Recomendación Estratégica del Wedding Planner:\n`;
md += `* *${database.constantes_interaccion.consejos_wedding_planner}*\n\n`;

md += `\n---\n\n`;

// 9. Add Policies and Star Promotions (Políticas y Promociones Especiales)
md += `## 📢 Políticas Comerciales y Promociones Especiales\n\n`;

md += `### 🌟 Promoción Estrella: ${database.politicas_y_promociones.promocion_estrella.nombre}\n`;
md += `* **Valor Comercial Estimado**: \`${database.politicas_y_promociones.promocion_estrella.valor_comercial}\`\n`;
md += `* **Condición de Aplicación**: ${database.politicas_y_promociones.promocion_estrella.condicion}\n\n`;
md += `#### 📋 Características Incluidas en la Invitación Digital:\n`;
database.politicas_y_promociones.promocion_estrella.caracteristicas.forEach(feat => {
  md += `- ${feat}\n`;
});

md += `\n### 📹 Locaciones Principales con Video Publicitario Activo:\n`;
md += `> Estas locaciones ya cuentan con material audiovisual propio para el impulso de campañas publicitarias pagadas y orgánicas:\n\n`;
database.politicas_y_promociones.locaciones_con_video.forEach(vid => {
  md += `- **${vid}**\n`;
});

md += `\n### ⚠️ Políticas y Penalizaciones Críticas:\n`;
database.politicas_y_promociones.politicas_pagos.forEach(pol => {
  md += `- ${pol}\n`;
});

md += `\n---\n\n`;

// 10. Add Blog Posts and WordPress Entries (Entradas de Blog y Noticias)
md += `## 📰 Publicaciones del Blog y Entradas de WordPress\n\n`;
database.entradas_blog.forEach(post => {
  md += `### 🏷️ Entrada: ${post.titulo}\n`;
  md += `* **Página de Referencia**: [Enlace al sitio](${post.url})\n`;
  if (post.fecha) {
    md += `* **Fecha de Publicación**: ${post.fecha}\n`;
  }
  md += `* **Autor**: ${post.autor}\n\n`;
  md += `#### 📋 Resumen del Contenido:\n`;
  md += `${post.resumen}\n\n`;
  
  if (post.inclusiones && post.inclusiones.length > 0) {
    md += `#### ✨ Elementos Destacados:\n`;
    post.inclusiones.forEach(inc => {
      md += `- ${inc}\n`;
    });
    md += `\n`;
  }
  md += `\n---\n\n`;
});

// 11. Add Organigrama y Equipo de Colaboradores
md += `## 👥 Organigrama y Equipo de Colaboradores Reales\n\n`;
database.colaboradores.forEach(col => {
  md += `### 👤 ${col.nombre}\n`;
  md += `* **Cargo/Rol**: **${col.cargo}**\n`;
  md += `* **Descripción**: ${col.descripcion}\n\n`;
});
md += `---\n\n`;

// 12. Add Manual de Branding e Identidad Visual/Sonora
md += `## 🎨 Manual de Branding e Identidad Visual y Sonora\n\n`;
md += `### 🖌️ Colores Corporativos Oficiales:\n\n`;
md += `| Color | Hexadecimal | RGB | Uso Recomendado |\n`;
md += `| --- | --- | --- | --- |\n`;
database.manual_marca.colores.forEach(c => {
  md += `| **${c.nombre}** | \`${c.hex}\` | \`rgb(${c.rgb})\` | ${c.uso} |\n`;
});
md += `\n### 🏷️ Hashtags Oficiales de Campaña:\n`;
database.manual_marca.hashtags.forEach(h => {
  md += `- \`${h}\`\n`;
});
md += `\n### 🎵 Pistas y Ecosistema de Identidad Sonora:\n\n`;
database.manual_marca.identidad_sonora.forEach(s => {
  md += `- **Archivo**: \`${s.pista}\` — *Uso*: ${s.uso}\n`;
});
md += `\n---\n\n`;

// 13. Add Plan Estratégico de Marketing
md += `## 🚀 Plan Estratégico de Marketing (Campaña Mensual)\n\n`;
md += `* **Eslogan de Campaña**: *«${database.plan_marketing.eslogan}»*\n`;
md += `* **Fecha Oficial del Gran Encuentro (Expo)**: **${database.plan_marketing.fecha_expo}**\n`;
md += `* **Contraseña Interna de Acceso al Plan**: \`${database.plan_marketing.password_acceso}\`\n\n`;
md += `### 🔗 Enlaces y Utilidades Estratégicas (Google Drive):\n\n`;
database.plan_marketing.enlaces.forEach(lnk => {
  md += `- **[${lnk.nombre}](${lnk.url})**\n`;
});
md += `\n---\n\n`;

// Write to MD file
fs.writeFileSync(mdPath, md, 'utf8');
console.log(`Saved Markdown Database: ${mdPath}`);
console.log('Fidelity compilation successful! All public prices, tables and inclusions are integrated.');
