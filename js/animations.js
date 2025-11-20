// Animations.js - Animation and interaction functionality

// Scroll-triggered animations
function initializeScrollAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-in');
            }
        });
    }, observerOptions);

    // Observe elements for animation
    const animateElements = document.querySelectorAll('.section, .chart-wrapper, .kpi-card, .timeline-item, .node, .flow-item');
    animateElements.forEach(element => {
        observer.observe(element);
    });
}

// Initialize stagger animations
function initializeStaggerAnimations() {
    const staggerContainers = document.querySelectorAll('.connections, .sub-flow, .timeline-container');

    staggerContainers.forEach(container => {
        const items = container.children;
        Array.from(items).forEach((item, index) => {
            item.style.animationDelay = `${index * 0.1}s`;
            item.classList.add('stagger-item');
        });
    });
}

// Parallax effect for header
function initializeParallax() {
    const header = document.querySelector('.header');
    if (!header) return;

    window.addEventListener('scroll', () => {
        const scrolled = window.pageYOffset;
        const rate = scrolled * -0.5;
        header.style.transform = `translateY(${rate}px)`;
    });
}

// Micro-interactions
function initializeMicroInteractions() {
    // Button hover effects
    const buttons = document.querySelectorAll('button, .accordion-header');
    buttons.forEach(button => {
        button.addEventListener('mouseenter', () => {
            button.classList.add('button-hover');
        });
        button.addEventListener('mouseleave', () => {
            button.classList.remove('button-hover');
        });
    });

    // Glow effects
    const cards = document.querySelectorAll('.chart-wrapper, .kpi-card');
    cards.forEach(card => {
        card.addEventListener('mouseenter', () => {
            card.classList.add('glow-on-hover');
        });
        card.addEventListener('mouseleave', () => {
            card.classList.remove('glow-on-hover');
        });
    });

    // Light shadow effects
    const sections = document.querySelectorAll('.section');
    sections.forEach(section => {
        section.addEventListener('mouseenter', () => {
            section.classList.add('light-shadow');
        });
        section.addEventListener('mouseleave', () => {
            section.classList.remove('light-shadow');
        });
    });
}

// Loading animations
function showLoadingAnimation(element) {
    element.classList.add('loading');
    setTimeout(() => {
        element.classList.remove('loading');
    }, 2000);
}

// Pulse animation for important elements
function initializePulseAnimations() {
    const importantElements = document.querySelectorAll('.central-node, .status-red');
    importantElements.forEach(element => {
        element.classList.add('pulse');
    });
}

// Chart animations
function animateChartBars() {
    const bars = document.querySelectorAll('.chart-bar');
    bars.forEach((bar, index) => {
        setTimeout(() => {
            bar.classList.add('animate');
        }, index * 200);
    });
}

// Timeline reveal animation
function animateTimeline() {
    const timelineItems = document.querySelectorAll('.timeline-item');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry, index) => {
            if (entry.isIntersecting) {
                setTimeout(() => {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateX(0)';
                }, index * 200);
            }
        });
    });

    timelineItems.forEach(item => {
        item.style.opacity = '0';
        item.style.transform = 'translateX(-100px)';
        item.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(item);
    });
}

// KPI counter animation
function animateKPICounters() {
    const kpiValues = document.querySelectorAll('.kpi-value');

    kpiValues.forEach(value => {
        const target = parseInt(value.textContent);
        let current = 0;
        const increment = target / 100;
        const timer = setInterval(() => {
            current += increment;
            if (current >= target) {
                current = target;
                clearInterval(timer);
            }
            value.textContent = Math.floor(current);
        }, 20);
    });
}

// Accordion smooth animation
function enhanceAccordion() {
    const accordions = document.querySelectorAll('.accordion-content');

    accordions.forEach(accordion => {
        accordion.style.maxHeight = '0';
        accordion.style.overflow = 'hidden';
        accordion.style.transition = 'max-height 0.4s ease';
    });
}

// Smooth scrolling for anchor links
function initializeSmoothScrolling() {
    const links = document.querySelectorAll('a[href^="#"]');

    links.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const target = document.querySelector(link.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// Initialize all animations on page load
document.addEventListener('DOMContentLoaded', function() {
    initializeScrollAnimations();
    initializeStaggerAnimations();
    initializeParallax();
    initializeMicroInteractions();
    initializePulseAnimations();
    animateTimeline();
    enhanceAccordion();
    initializeSmoothScrolling();
});

// Animate charts when they come into view
function animateChartsOnScroll() {
    const chartObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                if (entry.target.tagName === 'CANVAS') {
                    animateChartBars();
                }
                animateKPICounters();
            }
        });
    });

    const charts = document.querySelectorAll('canvas, .kpi-grid');
    charts.forEach(chart => {
        chartObserver.observe(chart);
    });
}

// Call chart animations after data is loaded
function onDataLoaded() {
    setTimeout(() => {
        animateChartsOnScroll();
    }, 500);
}

// Export for use in main.js
window.AnimationManager = {
    showLoadingAnimation,
    animateChartBars,
    animateKPICounters,
    onDataLoaded
};