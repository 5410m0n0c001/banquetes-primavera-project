# 📊 Lógica de Calificación y Scoring de Leads - Primavera Events Group

Este documento establece las reglas algorítmicas y semánticas que debe seguir el motor del chatbot para evaluar y clasificar automáticamente el nivel de interés y la urgencia de los prospectos (leads) capturados en redes sociales o WhatsApp.

---

## 1. Criterios de Evaluación (Matriz de Puntos)

La calificación final de un lead se calcula de forma acumulativa en base a los datos proporcionados durante la conversación.

| Criterio | Información Proporcionada | Puntos Asignados |
| :--- | :--- | :--- |
| **Tipo de Evento** | Definido (Boda / XV Años / Graduación) | +15 pts |
| **Número de Invitados** | Rango de invitados definido | +15 pts |
| **Fecha del Evento** | Fecha exacta / Mes definido en 2026-2027 | +20 pts |
| **Fecha del Evento** | Rango aproximado (ej. "el próximo año") | +10 pts |
| **Presupuesto** | Rango de inversión por persona o total definido | +20 pts |
| **Locación/Venue** | Tiene locación seleccionada o preferencia clara | +15 pts |
| **Estado de Decisión** | Listo para reservar / Desea degustación inmediata | +15 pts |

---

## 2. Clasificación de Niveles de Lead

### 🔵 Lead FRÍO (Puntuación: 0 - 30 pts)
*   **Perfil**: Prospecto que solo pide "información general" o precios sin proporcionar detalles. Suele iniciar con mensajes automáticos tipo *"Me interesa"* o *¿Qué precio tiene?"*.
*   **Acción del Bot**: Nutrir de forma educada con los precios base p/p (ej. *"Nuestros paquetes van desde $749 p/p..."*), enviar el catálogo general e intentar obtener al menos dos criterios (tipo de evento e invitados). No intentar agendar llamada o degustación.

### 🟡 Lead TIBIO (Puntuación: 31 - 65 pts)
*   **Perfil**: Conoce el tipo de evento y tiene un número de invitados estimado, además de una fecha tentativa (ej. *"Boda para 150 personas en octubre del otro año"*), pero no ha definido presupuesto o está evaluando múltiples proveedores.
*   **Acción del Bot**: Presentar 2 opciones de paquetes (ej. Paquete Gobernador y Esencia Floral), detallar las inclusiones de forma atractiva y hacer la pregunta de cierre para elevar la temperatura: *¿Les gustaría agendar una llamada breve de 5 minutos con Richard para diseñar una cotización personalizada sin costo?"*.

### 🔴 Lead CALIENTE (Puntuación: 66 - 85 pts)
*   **Perfil**: Tiene definido el tipo de evento, fecha exacta o mes específico, número de invitados, un presupuesto aproximado compatible con las tarifas de PEG y muestra interés por conocer un jardín o agendar degustación.
*   **Acción del Bot**: Presentar una propuesta formal estimada basada en el RAG, sugerir agendar una visita al recinto de su interés (ej. *Jardín Solaire* o *Centro de Convenciones Presidente*) y transferir de forma prioritaria la conversación a Richard Hernández en el CRM.

### 🔥 Lead URGENTE (Puntuación: 86 - 100 pts)
*   **Perfil**: Reúne todos los criterios definidos y la fecha de su evento es en **menos de 90 días**, o indica explícitamente que ya tiene el presupuesto listo para realizar el depósito de apartado de fecha.
*   **Acción del Bot**: Omitir explicaciones largas. Ofrecer agendar una llamada directa inmediata o reunión presencial en oficina, proporcionar el enlace directo de WhatsApp de Richard Hernández y alertar por canal prioritario al equipo comercial.

---

## 3. Guía de Respuestas Rápidas para el Scoring

El Bot Madre debe realizar los análisis en tiempo real basándose en la conversación y guardar los datos estructurados en la metadata del lead en la base de datos de Supabase.

```json
{
  "lead_scoring": {
    "points": 80,
    "classification": "Caliente",
    "event_type": "boda",
    "guests": 150,
    "event_date": "2027-03-20",
    "budget_pp": 950,
    "venue_preference": "Jardín Solaire",
    "escalated_to": "Richard Hernández"
  }
}
```
