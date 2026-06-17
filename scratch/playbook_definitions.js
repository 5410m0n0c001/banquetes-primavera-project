const fs = require('fs');
const path = require('path');

// Detailed package content definitions
const CC_PRESIDENTE_DETAILS = `
*   **Ubicación:** Avenida Defensa Nacional #8, Col. Chamilpa, 62210 Cuernavaca, Morelos.
*   **Capacidad:** 100 a 500 invitados.
*   **Estilo:** Modernista, elegante e industrial con amplias alturas y acabados de lujo.
*   **Fortalezas:** Gran salón climatizado, área infantil con juegos fijos, estacionamiento interno para 35 autos, cocina profesional gigante y baños múltiples de lujo.
*   **Página de Referencia:** [Enlace al sitio](https://primaveraeventsgroup.com/centro-de-convenciones-presidente/)
*   **Restricciones:** Cierre de evento a las 00:00 AM (Gobernador) o 01:00 AM (Presidente).
`;

const QUINTA_ZARABANDA_DETAILS = `
*   **Ubicación:** Avenida Lauro Ortega Martínez #4, Las Animas, 62583 Temixco, Morelos.
*   **Capacidad:** 100 a 250 personas en área techada (ampliable en jardines).
*   **Estilo:** Finca campestre íntima y natural de alto confort y descanso.
*   **Fortalezas:** Suite nupcial de lujo con jacuzzi y vestidor. Hospedaje interno climatizado para 14 personas con alberca privada y cocina. Área consagrada para ceremonias. Uso completo por 10 horas sin restricciones de horario.
*   **Página de Referencia:** [Enlace al sitio](https://primaveraeventsgroup.com/quinta-zarabanda/)
`;

const FINCA_ISABELES_DETAILS = `
*   **Ubicación:** Xochitepec, Morelos.
*   **Capacidad:** 200 a 400 invitados.
*   **Estilo:** Finca campestre rústica elegante tropical.
*   **Fortalezas:** Áreas verdes rodeadas de palmeras exóticas, salón abierto cubierto ideal para climas cálidos y alberca iluminada.
*   **Página de Referencia:** [Enlace al sitio](https://primaveraeventsgroup.com/finca-las-isabeles/)
`;

const JARDIN_LA_FLOR_DETAILS = `
*   **Ubicación:** Privada las Fuentes s/n, San Gaspar, Jiutepec, Morelos.
*   **Capacidad:** 100 a 300 invitados.
*   **Estilo:** Jardín clásico de Cuernavaca, fresco, romántico e íntimo.
*   **Fortalezas:** Explanada para montajes con cascada monumental de bienvenida con iluminación y área consagrada para ceremonias al aire libre.
*   **Página de Referencia:** [Enlace al sitio](https://primaveraeventsgroup.com/jardin-la-flor/)
`;

const SALON_POTRILLOS_DETAILS = `
*   **Ubicación:** Francisco I. Madero 23, Tepetzingo, 62767 Crucero Tezoyuca, Morelos.
*   **Capacidad:** 100 a 500 invitados.
*   **Estilo:** Rústico ecuestre campirano tradicional.
*   **Fortalezas:** Picadero visible para espectáculos de charros, gran calidez e ideal para menús rústicos tradicionales y amplios jardines con alberca y palapa.
*   **Página de Referencia:** [Enlace al sitio](https://primaveraeventsgroup.com/salon-los-potrillos/)
`;

const JARDIN_TSU_NUUM_DETAILS = `
*   **Ubicación:** Carretera a Aeropuerto de Cuernavaca, KM 0.5, Xochitepec, Morelos.
*   **Capacidad:** 100 a 250 invitados.
*   **Estilo:** Zen moderno y minimalista con paisajismo de autor.
*   **Fortalezas:** Alta privacidad, entornos fotogénicos únicos y gran iluminación ambiental nocturna en los árboles maduros. Cercanía al aeropuerto de Cuernavaca y suite privada.
*   **Página de Referencia:** [Enlace al sitio](https://primaveraeventsgroup.com/jardin-tsu-nuum/)
`;

const SALON_CABALLOS_DETAILS = `
*   **Ubicación:** Calle Zaragoza 1107, Ocotepec, Cuernavaca, Morelos.
*   **Capacidad:** 100 a 300 invitados.
*   **Estilo:** Hacienda de gran escala con establos elegantes de exhibición.
*   **Fortalezas:** Gran capacidad logística, estacionamiento cerrado masivo, acabados en cantera e iluminación arquitectónica del recinto.
*   **Página de Referencia:** [Enlace al sitio](https://primaveraeventsgroup.com/salon-los-caballos/)
`;

const SALON_YOLOMECATL_DETAILS = `
*   **Ubicación:** Calle Palma #6, Acatlipa, Temixco, Morelos.
*   **Capacidad:** 200 a 500 invitados.
*   **Estilo:** Complejo señorial cerrado con amplios jardines y salón techado.
*   **Fortalezas:** Capilla consagrada in-situ para ceremonias de validez oficial y gran privacidad.
*   **Página de Referencia:** [Enlace al sitio](https://primaveraeventsgroup.com/salon-jardin-yolomecatl/)
`;

const VILLA_DI_FIORI_DETAILS = `
*   **Ubicación:** Xochitepec, Morelos.
*   **Capacidad:** 100 a 350 invitados.
*   **Estilo:** Finca de arquitectura Toscana con arcos de cantera tallada.
*   **Fortalezas:** Jardines de diseño europeo con flores exóticas, suites privadas de preparación y fachadas perfectas para fotografía de alta gama.
*   **Página de Referencia:** [Enlace al sitio](https://primaveraeventsgroup.com/venues/villa-di-fiori/)
`;

const SALON_SOLAIRE_DETAILS = `
*   **Ubicación:** Cuernavaca, Morelos.
*   **Capacidad:** 80 a 180 invitados.
*   **Estilo:** Industrial-chic moderno con toques de madera sólida y cascada monumental.
*   **Fortalezas:** Pista Pixel LED 5x5 inteligente pre-instalada y mobiliario de autor campestre. Cascada monumental en la entrada y área consagrada al aire libre.
*   **Página de Referencia:** [Enlace al sitio](https://primaveraeventsgroup.com/venues/solaire/)
`;

// Helper to write the packages sections
console.log('Definitions ready.');
