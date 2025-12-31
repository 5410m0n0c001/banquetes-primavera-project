// Main JavaScript for Banquetes Primavera Dashboard

// Hardcoded dashboard data
const dashboardData = {
    ecosystem: {
        marketing: ["Leads", "Cotizaciones"],
        sales: ["Cotizaciones", "Contratos"],
        operations: ["Inventarios", "Logística"],
        finance: ["Facturación", "Pagos"]
    },
    radarData: {
        current: [3, 4, 2, 5, 3],
        competitors: [7, 6, 8, 4, 7],
        target: [8, 9, 9, 8, 9]
    },
    barData: {
        current: [40, 30, 20, 10],
        potential: [60, 40, 30, 20]
    },
    heatMap: [
        { "x": "Precio", "y": "Servicios", "value": 0.8 },
        { "x": "Precio", "y": "Calidad", "value": 0.6 },
        { "x": "Ubicación", "y": "Servicios", "value": 0.9 }
    ],
    timeline: [
        { "phase": "Fase 1", "month": "Mes 1-3", "milestones": ["Registro Marca", "Sitio Web", "Identidad"] },
        { "phase": "Fase 2", "month": "Mes 4-6", "milestones": ["Automatización", "IA", "Marketing"] },
        { "phase": "Fase 3", "month": "Mes 7-9", "milestones": ["Optimización", "Escalabilidad"] },
        { "phase": "Fase 4", "month": "Mes 10-12", "milestones": ["Expansión", "Internacional"] }
    ],
    kpis: [
        { "name": "Conversión de Leads", "current": 25, "target": 40, "description": "Porcentaje de leads que se convierten en cotizaciones" },
        { "name": "Tiempo de Respuesta", "current": 4, "target": 2, "description": "Horas promedio para responder consultas" },
        { "name": "Ticket Promedio", "current": 80000, "target": 96000, "description": "Ingreso promedio por evento" },
        { "name": "Tráfico Web", "current": 2000, "target": 5000, "description": "Visitas mensuales al sitio web" }
    ],
    benefits: [
        { "category": "Eficiencia Operativa", "percentage": 35 },
        { "category": "Crecimiento Ventas", "percentage": 25 },
        { "category": "Reducción Tiempos", "percentage": 20 },
        { "category": "Mejora Experiencia", "percentage": 15 },
        { "category": "Sostenibilidad", "percentage": 5 }
    ],
    requirements: [
        { "area": "Datos Legales", "status": "red", "priority": "Alta", "complexity": "Media", "dependencies": "Registro Marca" },
        { "area": "Información Salones", "status": "yellow", "priority": "Alta", "complexity": "Baja", "dependencies": "Fotografía" },
        { "area": "Estructura Team", "status": "red", "priority": "Media", "complexity": "Alta", "dependencies": "Organigrama" },
        { "area": "Proveedores", "status": "yellow", "priority": "Media", "complexity": "Media", "dependencies": "Alianzas" }
    ]
};

// Load data on page load
document.addEventListener('DOMContentLoaded', function () {
    populateDashboard();
    initializeInteractiveComponents();
    initializeCharts();
    // Ensure analysis dropdowns are initialized after everything else
    setTimeout(() => {
        initializeAnalysisDropdowns();
    }, 100);
});

// Populate dashboard with data
function populateDashboard() {
    populateRequirementsTable();
    populateTimeline();
    populateKPIs();
}

// Populate requirements table
function populateRequirementsTable() {
    const tbody = document.getElementById('requirementsTableBody');
    if (!tbody || !dashboardData.requirements) return;

    tbody.innerHTML = '';

    dashboardData.requirements.forEach(req => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${req.area}</td>
            <td class="status-${req.status}">${getStatusIcon(req.status)}</td>
            <td>${req.priority}</td>
            <td>${req.complexity}</td>
            <td>${req.dependencies}</td>
        `;
        tbody.appendChild(row);
    });
}

// Get status icon
function getStatusIcon(status) {
    const icons = {
        red: '🔴',
        yellow: '🟡',
        green: '🟢'
    };
    return icons[status] || status;
}

// Populate timeline
function populateTimeline() {
    const container = document.getElementById('timelineContainer');
    if (!container || !dashboardData.timeline) return;

    container.innerHTML = '';

    dashboardData.timeline.forEach((phase, index) => {
        const item = document.createElement('div');
        item.className = 'timeline-item';
        item.innerHTML = `
            <h4 class="timeline-phase">${phase.phase}</h4>
            <div class="timeline-month">${phase.month}</div>
            <ul class="timeline-milestones">
                ${phase.milestones.map(milestone => `<li>${milestone}</li>`).join('')}
            </ul>
        `;
        container.appendChild(item);
    });
}

// Populate KPIs
function populateKPIs() {
    const grid = document.getElementById('kpiGrid');
    if (!grid || !dashboardData.kpis) return;

    grid.innerHTML = '';

    dashboardData.kpis.forEach(kpi => {
        const card = document.createElement('div');
        card.className = 'kpi-card';
        const progressPercent = (kpi.current / kpi.target) * 100;

        card.innerHTML = `
            <h4 class="kpi-title">${kpi.name}</h4>
            <div class="kpi-value">${kpi.current}</div>
            <div class="kpi-target">Objetivo: ${kpi.target}</div>
            <div class="kpi-progress">
                <div class="kpi-progress-bar" style="width: ${progressPercent}%"></div>
            </div>
            <div class="kpi-description">${kpi.description}</div>
        `;
        grid.appendChild(card);
    });
}

// Initialize interactive components
function initializeInteractiveComponents() {
    // Accordion functionality with dynamic height
    const accordionHeaders = document.querySelectorAll('.accordion-header');
    accordionHeaders.forEach(header => {
        header.addEventListener('click', function () {
            const content = this.nextElementSibling;
            const icon = this.querySelector('.accordion-icon');

            if (content.classList.contains('open')) {
                content.style.maxHeight = '0px';
                setTimeout(() => {
                    content.classList.remove('open');
                }, 400); // Match transition duration
            } else {
                content.classList.add('open');
                content.style.maxHeight = content.scrollHeight + 'px';
            }

            // Rotate icon
            if (icon) {
                icon.classList.toggle('rotate');
            }
        });
    });

    // Impact calculator
    initializeImpactCalculator();
}

// Initialize analysis dropdowns
function initializeAnalysisDropdowns() {
    const analysisHeaders = document.querySelectorAll('.analysis-header');

    analysisHeaders.forEach(header => {
        // Click event
        header.addEventListener('click', function () {
            toggleAnalysisContent(this);
        });

        // Keyboard events
        header.addEventListener('keydown', function (e) {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                toggleAnalysisContent(this);
            }
        });
    });
}

// Toggle analysis content
function toggleAnalysisContent(header) {
    const content = header.nextElementSibling;
    const icon = header.querySelector('.analysis-icon');
    const isExpanded = header.getAttribute('aria-expanded') === 'true';

    // Toggle content
    content.classList.toggle('open');

    // Update ARIA attributes
    header.setAttribute('aria-expanded', !isExpanded);

    // Rotate icon
    if (icon) {
        icon.classList.toggle('rotate');
    }

    // Initialize charts when section opens
    if (!isExpanded) {
        const sectionId = header.textContent.trim().split(' ')[0];
        setTimeout(() => {
            initializeAnalysisCharts(sectionId);
        }, 100);
    }
}

// Initialize analysis charts
function initializeAnalysisCharts(sectionId) {
    switch (sectionId) {
        case '🌎':
            createSociologicalChart();
            break;
        case '🆚':
            createComparisonChart();
            break;
        case '💸':
            createFinancialChart();
            break;
    }
}

// Initialize impact calculator
function initializeImpactCalculator() {
    const eventsSlider = document.getElementById('eventsSlider');
    const timeSlider = document.getElementById('timeSlider');
    const capacitySlider = document.getElementById('capacitySlider');
    const resultsDiv = document.getElementById('impactResults');

    if (!eventsSlider || !timeSlider || !capacitySlider || !resultsDiv) return;

    function updateCalculator() {
        const events = parseInt(eventsSlider.value);
        const time = parseInt(timeSlider.value);
        const capacity = parseInt(capacitySlider.value);

        // Calculate impact (simplified)
        const efficiencyGain = Math.round((events * 0.1) + (24 - time) * 2 + (capacity / 10));
        const revenueIncrease = Math.round(events * capacity * 0.05);

        resultsDiv.innerHTML = `
            <h4>Impacto Estimado</h4>
            <p><strong>Ganancia de Eficiencia:</strong> ${efficiencyGain}%</p>
            <p><strong>Incremento de Ingresos:</strong> $${revenueIncrease.toLocaleString()} MXN/mes</p>
            <p><em>Estos son cálculos aproximados basados en proyecciones.</em></p>
        `;
    }

    eventsSlider.addEventListener('input', updateCalculator);
    timeSlider.addEventListener('input', updateCalculator);
    capacitySlider.addEventListener('input', updateCalculator);

    // Initial calculation
    updateCalculator();
}

// Utility functions
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Format numbers
function formatNumber(num) {
    return num.toLocaleString();
}

// Format currency
function formatCurrency(amount, currency = 'MXN') {
    return `$${formatNumber(amount)} ${currency}`;
}

// Show loading state
function showLoading(element) {
    element.classList.add('loading');
}

// Hide loading state
function hideLoading(element) {
    element.classList.remove('loading');
}

// Error handling
function showError(message) {
    console.error(message);
    // Could implement user-friendly error display
}

// Success feedback
function showSuccess(message) {
    console.log('Success:', message);
    // Could implement success notifications
}
/* New Toggle Functions for Refactored Phases */
function togglePhase(header) {
    const content = header.nextElementSibling;
    content.classList.toggle('active');
    const icon = header.querySelector('.phase-icon');
    if (content.classList.contains('active')) {
        icon.textContent = '-';
    } else {
        icon.textContent = '+';
    }
}

function toggleCollapsible(header) {
    const body = header.nextElementSibling;
    body.classList.toggle('active');
    const span = header.querySelector('span');
    if (body.classList.contains('active')) {
        span.textContent = '-';
    } else {
        span.textContent = '+';
    }
}


function toggleNested(header) {
    const content = header.nextElementSibling;
    const icon = header.querySelector('.accordion-icon') || header.querySelector('span');
    if (content.style.display === 'none' || content.style.display === '') {
        content.style.display = 'block';
        if (icon) icon.textContent = '▲';
    } else {
        content.style.display = 'none';
        if (icon) icon.textContent = '▼';
    }
}
