# 📖 Meta Ads · Playbook de Conversiones (Sales Objective) — Referencia Oficial

> Fuente: "Sales Objective Playbook" de Meta (PDF oficial de Meta for Business, 8 páginas de contenido dentro de un documento de 43 páginas de diseño). Recibido de Salo el 2026-08-09 y transcrito íntegro aquí como directriz de referencia para campañas pagadas de PEG en Facebook/Instagram Ads.
>
> Este documento son **prácticas validadas por Meta**, no diagnóstico de PEG. Para el diagnóstico real de la cuenta y las decisiones ya tomadas sobre pauta, ver `primavera-marketing-estrategia.md` (repo `alexros-brain`, sección 5 "Meta Ads").

---

## 1. Buenas prácticas avanzadas para subir desempeño y bajar CPA

### 1.1 Consolidar ad sets similares
Combinar campañas/ad sets con creativo similar en lugar de fragmentarlos ayuda a gastar el presupuesto de forma más eficiente y reduce el CPA (costo por acción).

**Checklist:**
- Combinar ad sets que compartan creativo similar — acelera resultados.
- Evitar audiencias que se traslapen entre ad sets de la misma campaña.

**Dato Meta:** small businesses con estructura de cuenta simplificada lograron **18% menos CPA** en promedio vs. cuentas fragmentadas.¹

### 1.2 Combinar targeting amplio (broad) con Custom Audiences
Usar las recomendaciones de targeting más recientes de Meta.

**Checklist:**
- Usar targeting **broad** de al menos **2 millones de personas**, y activar **Advantage detailed targeting** si el negocio tiene una audiencia muy nicho.
- Al usar Lookalike + Custom Audiences juntas, incluir también una audiencia más amplia en los ad sets, y activar **Advantage campaign budget** para maximizar conversiones.

**Dato Meta:** negocios que usaron targeting amplio (sin restringir por ubicación, edad o género) lograron **12% menos CPA** en promedio vs. los que sí restringieron.²

### 1.3 Usar video mobile-friendly
La mayoría de los clientes navegan Facebook/Instagram desde el celular.

**Checklist:**
- Video **vertical** (no horizontal), aspecto **9:16** para Reels/Historias.
- Experimentar con audio: sonido original o música libre de regalías.
- Capturar atención con la marca o mensaje clave en los **primeros 3 segundos**.
- Agregar video a campañas que solo tienen imagen — mezclar estático + video en el mismo ad set ayuda a que la campaña aparezca en más ubicaciones (placements).

**Dato Meta:** negocios que usaron creativo mobile-friendly lograron **12% menos costo por conversión web** en promedio.³

### 1.4 Usar la herramienta de A/B testing de Meta Ads Manager
Compara dos versiones de un anuncio para identificar qué estrategia funciona mejor.

**Checklist:**
- Probar variables como creativo, call-to-action o audiencia.
- Probar **una sola variable a la vez** para que el resultado sea claro.
- Correr la prueba **mínimo 2 semanas**.

**Dato Meta:** negocios que corrieron A/B tests vieron **30% menos costo por resultado** en los anuncios ganadores vs. los perdedores.⁴

### 1.5 Usar la Conversions API (API de Conversiones)
Optimización de targeting menos dependiente de la tecnología del navegador que el Meta Pixel solo. Ayuda a mejorar el desempeño hoy y a proteger el desempeño conforme el tracking por navegador se vuelve menos confiable.

**Checklist:**
- Usar la Conversions API **junto con** el Pixel (no en sustitución) — ayuda al sistema de entrega a bajar el CPA y entregar anuncios más personalizados.

⚠️ **Relevante para PEG:** `primavera-marketing-estrategia.md` (sección 5) tiene pendiente confirmar si hay Pixel instalado en `primaveraeventsgroup.com` — sin Pixel, no hay Conversions API posible, y cada campaña sigue optimizando a ciegas. Esta es la pieza técnica de mayor apalancamiento antes de invertir más en pauta.

---

## 2. Políticas de anuncios para pequeños negocios (evitar rechazos/restricciones)

- **Derechos de autor:** solo usar imagen, video y audio sobre los que se tienen derechos (política de Infracción de Terceros).
- **No afirmar ni implicar atributos personales:** raza, etnia, religión, creencias, edad, etc. — en copy, imagen, video, captions, stickers o emojis. No usar "tú/tu" para referirse a un atributo personal del espectador.
- **Describir el servicio con precisión:** expectativas realistas, sin promesas de resultados poco realistas (aplica sobre todo a salud, pérdida de peso u oportunidad económica — menos relevante para banquetes/eventos, pero aplica igual a "garantizamos el evento perfecto" si se usa como promesa literal).
- **Sin groserías ni gramática/puntuación incorrecta** — símbolos, números y letras deben usarse correctamente.
- **No usar la marca de Meta (logos de Facebook/Instagram) como elemento más prominente del creativo**, ni modificar sus assets de marca (color, diseño, animación).
- **Landing page funcional, sin error 404** — las landing pages se evalúan con los mismos estándares que el anuncio.

### Si un anuncio es rechazado
1. **Editar y reenviar** — corregir el contenido en Ads Manager y volver a subir.
2. **Solicitar otra revisión** — en la cuenta de anuncios, ir a Calidad de la Cuenta, seleccionar el anuncio y "Solicitar revisión".

### Si la cuenta/página es restringida
1. Ir a **Calidad de la Cuenta**.
2. En la pestaña de Problemas de la Cuenta, seleccionar la cuenta/usuario/página restringida y "Solicitar revisión" en la sección "Qué puedes hacer".
3. Elegir el motivo de la revisión y enviar la solicitud.

---

## 3. Herramientas adicionales

- **Tailored campaigns** (nuevo en Ads Manager): configuración de campaña precargada con los ajustes óptimos de Meta (objetivo, estrategia de puja, Advantage+ placements, optimización de entrega) — solo se elige el objetivo de ventas y Meta precarga el resto.
- **Meta Marketing Pros:** asesoría de estrategia publicitaria personalizada y gratuita para negocios elegibles — verificar elegibilidad en Meta Business Suite.

---

## Notas de la fuente
¹ ² ³ Meta Internal metadata. Basado en el desempeño promedio de campañas de conversión web de small businesses (muestra ~200,000), 2021-08-01 a 2022-03-25.
⁴ Meta Internal data. Basado en la diferencia mediana de desempeño de A/B tests corridos en 2019 (muestra ~747,000).

## Ver también
- `primavera-marketing-estrategia.md` (repo `alexros-brain/brain/proyectos/`) — sección 5 "Meta Ads", diagnóstico real de la cuenta de PEG y pendientes de Pixel/Ads Manager.
- `redes_sociales_directrices.md` — directrices de copy orgánico (distinto de este playbook, que es específico de campañas pagadas).
- `playbook_comercial_manual_ventas.md` — proceso comercial y ciclo de venta una vez que el lead ya llegó (este playbook cubre solo la etapa de generación/pauta).
