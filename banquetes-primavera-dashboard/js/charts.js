// Charts.js - Chart functionality for Banquetes Primavera Dashboard

// Note: This implementation uses basic Canvas API for charts
// For production, consider using Chart.js library

let charts = {};

// Initialize all charts
function initializeCharts() {
    createRadarChart();
    createBarChart();
    createHeatMap();
    createCompetitorChart();
    createBenefitsChart();
}

// Create sociological chart
function createSociologicalChart() {
    const canvas = document.getElementById('sociologicalChart');
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    const data = [45, 35, 20]; // Local clients, Foraneos, Premium perception
    const labels = ['Locales', 'Foráneos', 'Premium'];

    drawPieChart(ctx, [
        {category: 'Clientes Locales', percentage: 45},
        {category: 'Clientes Foráneos', percentage: 35},
        {category: 'Percepción Premium', percentage: 20}
    ]);
}

// Create comparison chart
function createComparisonChart() {
    const canvas = document.getElementById('comparisonChart');
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    const angloPros = 5;
    const angloCons = 4;
    const spanishPros = 5;
    const spanishCons = 4;

    drawBarChart(ctx, ['Anglo Pros', 'Anglo Cons', 'Español Pros', 'Español Cons'], [
        [angloPros, angloCons, spanishPros, spanishCons]
    ]);
}

// Create financial chart
function createFinancialChart() {
    const canvas = document.getElementById('financialChart');
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    const angloCost = 120; // +20-40%
    const spanishCost = 100; // baseline

    drawBarChart(ctx, ['Anglo', 'Español'], [[angloCost, spanishCost]]);
}

// Create radar chart for current situation analysis
function createRadarChart() {
    const canvas = document.getElementById('radarChart');
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    const data = dashboardData.radarData;
    const labels = ['Presencia Digital', 'Operaciones', 'Tecnología', 'Ventas', 'Marketing'];

    // Simple radar chart implementation
    drawRadarChart(ctx, labels, data.current, data.competitors, data.target);
}

// Draw radar chart
function drawRadarChart(ctx, labels, current, competitors, target) {
    const centerX = 200;
    const centerY = 200;
    const radius = 150;
    const angleStep = (Math.PI * 2) / labels.length;

    ctx.clearRect(0, 0, 400, 400);

    // Draw grid
    ctx.strokeStyle = '#e0e0e0';
    ctx.lineWidth = 1;
    for (let i = 1; i <= 5; i++) {
        const r = (radius / 5) * i;
        ctx.beginPath();
        for (let j = 0; j < labels.length; j++) {
            const angle = j * angleStep - Math.PI / 2;
            const x = centerX + Math.cos(angle) * r;
            const y = centerY + Math.sin(angle) * r;
            if (j === 0) ctx.moveTo(x, y);
            else ctx.lineTo(x, y);
        }
        ctx.closePath();
        ctx.stroke();
    }

    // Draw axes
    ctx.strokeStyle = '#ccc';
    for (let i = 0; i < labels.length; i++) {
        const angle = i * angleStep - Math.PI / 2;
        const x = centerX + Math.cos(angle) * radius;
        const y = centerY + Math.sin(angle) * radius;
        ctx.beginPath();
        ctx.moveTo(centerX, centerY);
        ctx.lineTo(x, y);
        ctx.stroke();
    }

    // Draw data polygons
    drawDataPolygon(ctx, centerX, centerY, radius, current, angleStep, '#F8BBD9', 0.3);
    drawDataPolygon(ctx, centerX, centerY, radius, competitors, angleStep, '#E91E63', 0.3);
    drawDataPolygon(ctx, centerX, centerY, radius, target, angleStep, '#4CAF50', 0.3);

    // Draw labels
    ctx.fillStyle = '#333';
    ctx.font = '12px Roboto';
    ctx.textAlign = 'center';
    for (let i = 0; i < labels.length; i++) {
        const angle = i * angleStep - Math.PI / 2;
        const x = centerX + Math.cos(angle) * (radius + 20);
        const y = centerY + Math.sin(angle) * (radius + 20);
        ctx.fillText(labels[i], x, y);
    }
}

// Draw data polygon
function drawDataPolygon(ctx, centerX, centerY, radius, data, angleStep, color, alpha) {
    ctx.fillStyle = color;
    ctx.globalAlpha = alpha;
    ctx.beginPath();
    for (let i = 0; i < data.length; i++) {
        const angle = i * angleStep - Math.PI / 2;
        const value = data[i] / 10; // Assuming max value is 10
        const x = centerX + Math.cos(angle) * radius * value;
        const y = centerY + Math.sin(angle) * radius * value;
        if (i === 0) ctx.moveTo(x, y);
        else ctx.lineTo(x, y);
    }
    ctx.closePath();
    ctx.fill();
    ctx.globalAlpha = 1;
}

// Create bar chart
function createBarChart() {
    const canvas = document.getElementById('barChart');
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    const data = dashboardData.barData;

    drawBarChart(ctx, ['Actual', 'Potencial'], [data.current, data.potential]);
}

// Draw bar chart
function drawBarChart(ctx, labels, data) {
    const width = 400;
    const height = 300;
    const barWidth = 60;
    const maxValue = Math.max(...data.flat());

    ctx.clearRect(0, 0, width, height);

    data.forEach((categoryData, categoryIndex) => {
        categoryData.forEach((value, index) => {
            const x = 50 + categoryIndex * 150 + index * barWidth;
            const barHeight = (value / maxValue) * 200;
            const y = height - 50 - barHeight;

            // Bar
            ctx.fillStyle = index === 0 ? '#F8BBD9' : '#E91E63';
            ctx.fillRect(x, y, barWidth - 10, barHeight);

            // Value label
            ctx.fillStyle = '#333';
            ctx.font = '12px Roboto';
            ctx.textAlign = 'center';
            ctx.fillText(value.toString(), x + (barWidth - 10) / 2, y - 5);
        });
    });

    // Labels
    ctx.fillStyle = '#333';
    ctx.font = '14px Roboto';
    labels.forEach((label, index) => {
        ctx.fillText(label, 50 + index * 150 + barWidth, height - 20);
    });
}

// Create heat map
function createHeatMap() {
    const container = document.getElementById('heatMap');
    if (!container) return;

    container.innerHTML = '';

    dashboardData.heatMap.forEach(cell => {
        const div = document.createElement('div');
        div.className = `heat-cell heat-${getHeatLevel(cell.value)}`;
        div.textContent = `${cell.x} vs ${cell.y}: ${cell.value}`;
        container.appendChild(div);
    });
}

// Get heat level
function getHeatLevel(value) {
    if (value < 0.4) return 'low';
    if (value < 0.7) return 'medium';
    return 'high';
}

// Create competitor chart
function createCompetitorChart() {
    const canvas = document.getElementById('competitorChart');
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    // Simple bar chart for competitors
    const competitors = ['Banquetes Primavera', 'Competidor A', 'Competidor B', 'Competidor C', 'Competidor D'];
    const data = [6, 3, 4, 2, 5]; // Number of venues

    drawBarChart(ctx, competitors, [data]);
}

// Create benefits chart (pie chart)
function createBenefitsChart() {
    const canvas = document.getElementById('benefitsChart');
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    const data = dashboardData.benefits;

    drawPieChart(ctx, data);
}

// Draw pie chart
function drawPieChart(ctx, data) {
    const centerX = 200;
    const centerY = 200;
    const radius = 150;
    let startAngle = 0;

    ctx.clearRect(0, 0, 400, 400);

    data.forEach((item, index) => {
        const sliceAngle = (item.percentage / 100) * Math.PI * 2;
        const endAngle = startAngle + sliceAngle;

        // Slice
        ctx.beginPath();
        ctx.moveTo(centerX, centerY);
        ctx.arc(centerX, centerY, radius, startAngle, endAngle);
        ctx.closePath();
        ctx.fillStyle = getColor(index);
        ctx.fill();
        ctx.strokeStyle = '#fff';
        ctx.lineWidth = 2;
        ctx.stroke();

        // Label
        const labelAngle = startAngle + sliceAngle / 2;
        const labelX = centerX + Math.cos(labelAngle) * (radius * 0.7);
        const labelY = centerY + Math.sin(labelAngle) * (radius * 0.7);

        ctx.fillStyle = '#fff';
        ctx.font = '12px Roboto';
        ctx.textAlign = 'center';
        ctx.fillText(`${item.category}: ${item.percentage}%`, labelX, labelY);

        startAngle = endAngle;
    });
}

// Get color for pie chart
function getColor(index) {
    const colors = ['#F8BBD9', '#E91E63', '#FF9800', '#4CAF50', '#2196F3'];
    return colors[index % colors.length];
}

// Animate charts on scroll
function animateCharts() {
    const chartCanvases = document.querySelectorAll('canvas');
    chartCanvases.forEach(canvas => {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    canvas.classList.add('chart-fade-in');
                }
            });
        });
        observer.observe(canvas);
    });
}

// Initialize chart animations
document.addEventListener('DOMContentLoaded', animateCharts);