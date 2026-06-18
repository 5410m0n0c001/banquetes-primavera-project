# 🗺️ Planificadores y Croquis Centralizados - Primavera Events Group

Este directorio centraliza los proyectos de diseño de croquis y planos interactivos 2D/3D para las locaciones principales de **Primavera Events Group**. Se han unificado aquí para facilitar futuros diseños, modificaciones de planos y servir de referencia técnica para nuevos desarrollos.

---

## 📂 Directorio de Planificadores

### 1. 🌿 Planificador del Salón Jardín La Flor
Una aplicación web interactiva premium en 2D (SVG interactivo con drag-and-drop y snapping magnético a rejilla) y proyecciones 3D realistas en tiempo real utilizando **Three.js** y **OrbitControls**.
- **Dimensiones:** Terreno real de 16m × 20m.
- **Mobiliario:** Mesas redondas y cuadradas, arreglos florales, sillas, cabina de DJ, pista de baile y elementos exteriores (capilla, estacionamiento, accesos).
- **Código Fuente:** [jardin-la-flor-plano/](file:///c:/Users/Lenovo/Documents/primavera%20brain/venues_planners/jardin-la-flor-plano/)
- **Manual de Desarrollo:** [MANUAL_3D.md](file:///c:/Users/Lenovo/Documents/primavera%20brain/venues_planners/jardin-la-flor-plano/MANUAL_3D.md) — *Contiene la lógica de transformación de coordenadas 2D a 3D, cálculos trigonométricos de distribución de sillas y optimizaciones de Three.js.*

### 2. 🏛️ Planificador del Salón Jardín Yolomecatl
Una aplicación web interactiva para el diseño del acomodo del Salón Señorial Yolomecatl. Permite posicionar mesas imperiales, mesas estándar, pista de baile y visualizar toda la estructura en 3D.
- **Dimensiones:** Terreno real de 100m × 98m (escala real).
- **Estructura:** Salón de doble altura, escenario de DJ elevado, cocina, baños, alberca, capilla al aire libre y cascada de agua sobre muro de piedra volcánica.
- **Código Fuente:** [yolomecatl-croquis/](file:///c:/Users/Lenovo/Documents/primavera%20brain/venues_planners/yolomecatl-croquis/)
- **Manual de Desarrollo:** [3d_modeling_manual.md](file:///c:/Users/Lenovo/Documents/primavera%20brain/venues_planners/yolomecatl-croquis/3d_modeling_manual.md) — *Detalla las coordenadas CAD del proyecto, las alturas del eje Z, la tabla de materiales y texturas PBR sugeridos, y esquemas de iluminación nocturna de gala.*

---

## 🚀 Cómo Iniciar las Aplicaciones Localmente

Por razones de seguridad del navegador, al utilizar módulos de JavaScript (`import`/`export`), las aplicaciones no se pueden ejecutar abriendo directamente el archivo `.html` en tu navegador (`file://`). Deben ser ejecutadas a través de un servidor local.

### Opción 1: Servidor en Python (Recomendado, no requiere instalaciones)
Abre la consola (PowerShell o CMD), navega a la carpeta de la locación y ejecuta:
```bash
python -m http.server 8000
```
Luego abre tu navegador en: 👉 [http://localhost:8000](http://localhost:8000)

### Opción 2: Servidor en Node.js (npx)
Si tienes Node instalado, ejecuta en la carpeta del proyecto:
```bash
npx http-server -p 8000
```
Luego abre tu navegador en: 👉 [http://localhost:8000](http://localhost:8000)

---

## 📐 Resumen de Fórmulas Clave para Nuevos Croquis
Para replicar esta tecnología en nuevas locaciones (ej. *Villa Di Fiori*, *Rancho Los Potrillos* o *Salón Solaire*), guíate en las siguientes implementaciones que ya funcionan:

### Conversión de Coordenadas 2D a 3D
Dado que el plano 2D tiene el eje Y creciendo hacia abajo y las rotaciones en sentido horario, y Three.js tiene el eje Y hacia arriba (altura) y el eje Z hacia el fondo, aplicamos:
$$\begin{aligned}
X_{3D} &= X_{2D\text{ (en metros)}} \\
Y_{3D} &= \text{Altura (Z del plano)} \\
Z_{3D} &= Y_{2D\text{ (en metros)}} \\
\theta_{3D} &= -\theta_{2D\text{ (en radianes)}}
\end{aligned}$$

### Distribución de Sillas alrededor de una Mesa Redonda (Trigonometría Polar)
Para posicionar $N$ sillas a una distancia $R$ (radio) del centro de la mesa:
```javascript
const angle = (i * 2 * Math.PI) / numChairs;
const chairX = Math.sin(angle) * (radius + offset);
const chairZ = Math.cos(angle) * (radius + offset);
const chairRotY = angle + Math.PI; // Mirando hacia el centro
```
