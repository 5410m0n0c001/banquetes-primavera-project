// Scroll Effects.js - Advanced scroll-based animations and effects

// Throttle function for performance
function throttle(func, limit) {
    let inThrottle;
    return function() {
        const args = arguments;
        const context = this;
        if (!inThrottle) {
            func.apply(context, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    }
}

// Parallax scrolling effects
function initializeParallaxEffects() {
    const parallaxElements = document.querySelectorAll('[data-parallax]');

    function updateParallax() {
        const scrolled = window.pageYOffset;

        parallaxElements.forEach(element => {
            const rate = element.dataset.parallax || 0.5;
            const yPos = -(scrolled * rate);
            element.style.transform = `translateY(${yPos}px)`;
        });
    }

    window.addEventListener('scroll', throttle(updateParallax, 16));
}

// Background parallax for hero section
function initializeBackgroundParallax() {
    const hero = document.querySelector('.header');
    if (!hero) return;

    window.addEventListener('scroll', throttle(() => {
        const scrolled = window.pageYOffset;
        const rate = scrolled * 0.5;
        hero.style.backgroundPositionY = `${rate}px`;
    }, 16));
}

// Scroll progress indicator
function initializeScrollProgress() {
    const progressBar = document.createElement('div');
    progressBar.className = 'scroll-progress';
    progressBar.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        width: 0%;
        height: 4px;
        background: linear-gradient(90deg, #F8BBD9, #E91E63);
        z-index: 1000;
        transition: width 0.3s ease;
    `;
    document.body.appendChild(progressBar);

    function updateProgress() {
        const windowHeight = document.documentElement.scrollHeight - window.innerHeight;
        const scrolled = (window.pageYOffset / windowHeight) * 100;
        progressBar.style.width = `${scrolled}%`;
    }

    window.addEventListener('scroll', throttle(updateProgress, 16));
}

// Fade in elements on scroll
function initializeFadeInOnScroll() {
    const fadeElements = document.querySelectorAll('[data-fade]');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const delay = entry.target.dataset.fadeDelay || 0;
                setTimeout(() => {
                    entry.target.classList.add('fade-in');
                }, delay);
            }
        });
    }, { threshold: 0.1 });

    fadeElements.forEach(element => {
        observer.observe(element);
    });
}

// Slide in elements from different directions
function initializeSlideInEffects() {
    const slideElements = document.querySelectorAll('[data-slide]');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const direction = entry.target.dataset.slide || 'left';
                const delay = entry.target.dataset.slideDelay || 0;

                setTimeout(() => {
                    entry.target.classList.add(`slide-in-${direction}`);
                }, delay);
            }
        });
    }, { threshold: 0.1 });

    slideElements.forEach(element => {
        observer.observe(element);
    });
}

// Scale in animations
function initializeScaleInEffects() {
    const scaleElements = document.querySelectorAll('[data-scale]');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const delay = entry.target.dataset.scaleDelay || 0;
                setTimeout(() => {
                    entry.target.classList.add('scale-in');
                }, delay);
            }
        });
    }, { threshold: 0.1 });

    scaleElements.forEach(element => {
        observer.observe(element);
    });
}

// Bounce in animations
function initializeBounceInEffects() {
    const bounceElements = document.querySelectorAll('[data-bounce]');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const delay = entry.target.dataset.bounceDelay || 0;
                setTimeout(() => {
                    entry.target.classList.add('bounce-in');
                }, delay);
            }
        });
    }, { threshold: 0.1 });

    bounceElements.forEach(element => {
        observer.observe(element);
    });
}

// Reveal animations with clip-path
function initializeRevealEffects() {
    const revealElements = document.querySelectorAll('[data-reveal]');

    revealElements.forEach(element => {
        element.style.clipPath = 'inset(0 100% 0 0)';
        element.style.transition = 'clip-path 1s ease';
    });

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const delay = entry.target.dataset.revealDelay || 0;
                setTimeout(() => {
                    entry.target.style.clipPath = 'inset(0 0 0 0)';
                }, delay);
            }
        });
    }, { threshold: 0.1 });

    revealElements.forEach(element => {
        observer.observe(element);
    });
}

// Stagger animations for lists
function initializeStaggerEffects() {
    const staggerContainers = document.querySelectorAll('[data-stagger]');

    staggerContainers.forEach(container => {
        const children = container.children;
        const delay = parseInt(container.dataset.staggerDelay) || 100;

        const observer = new IntersectionObserver((entries) => {
            if (entries[0].isIntersecting) {
                Array.from(children).forEach((child, index) => {
                    setTimeout(() => {
                        child.classList.add('stagger-item');
                    }, index * delay);
                });
            }
        }, { threshold: 0.1 });

        observer.observe(container);
    });
}

// Dynamic background color changes on scroll
function initializeDynamicBackground() {
    const sections = document.querySelectorAll('.section');

    function updateBackground() {
        const scrollPosition = window.pageYOffset;

        sections.forEach((section, index) => {
            const sectionTop = section.offsetTop - 100;
            const sectionBottom = sectionTop + section.offsetHeight;

            if (scrollPosition >= sectionTop && scrollPosition < sectionBottom) {
                const progress = (scrollPosition - sectionTop) / section.offsetHeight;
                const opacity = Math.min(progress * 0.1, 0.1);

                // Subtle background color change
                section.style.backgroundColor = `rgba(248, 187, 217, ${opacity})`;
            } else {
                section.style.backgroundColor = '';
            }
        });
    }

    window.addEventListener('scroll', throttle(updateBackground, 16));
}

// Scroll-based counter animations
function initializeScrollCounters() {
    const counters = document.querySelectorAll('[data-counter]');

    counters.forEach(counter => {
        const target = parseInt(counter.dataset.counter);
        const observer = new IntersectionObserver((entries) => {
            if (entries[0].isIntersecting) {
                animateCounter(counter, target);
            }
        }, { threshold: 0.5 });

        observer.observe(counter);
    });
}

function animateCounter(element, target) {
    let current = 0;
    const increment = target / 100;
    const duration = 2000; // 2 seconds
    const step = duration / 100;

    const timer = setInterval(() => {
        current += increment;
        if (current >= target) {
            current = target;
            clearInterval(timer);
        }
        element.textContent = Math.floor(current);
    }, step);
}

// Initialize all scroll effects
document.addEventListener('DOMContentLoaded', function() {
    initializeParallaxEffects();
    initializeBackgroundParallax();
    initializeScrollProgress();
    initializeFadeInOnScroll();
    initializeSlideInEffects();
    initializeScaleInEffects();
    initializeBounceInEffects();
    initializeRevealEffects();
    initializeStaggerEffects();
    initializeDynamicBackground();
    initializeScrollCounters();
});

// Add data attributes to elements for scroll effects
function addScrollAttributes() {
    // Add fade effects to sections
    const sections = document.querySelectorAll('.section');
    sections.forEach((section, index) => {
        section.setAttribute('data-fade', '');
        section.setAttribute('data-fade-delay', (index * 200).toString());
    });

    // Add slide effects to chart wrappers
    const charts = document.querySelectorAll('.chart-wrapper');
    charts.forEach((chart, index) => {
        if (index % 2 === 0) {
            chart.setAttribute('data-slide', 'left');
        } else {
            chart.setAttribute('data-slide', 'right');
        }
        chart.setAttribute('data-slide-delay', '200');
    });

    // Add scale effects to KPI cards
    const kpiCards = document.querySelectorAll('.kpi-card');
    kpiCards.forEach(card => {
        card.setAttribute('data-scale', '');
        card.setAttribute('data-scale-delay', '300');
    });

    // Add stagger effects to connections
    const connections = document.querySelectorAll('.connections');
    connections.forEach(connection => {
        connection.setAttribute('data-stagger', '');
        connection.setAttribute('data-stagger-delay', '150');
    });
}

// Call after DOM is ready
document.addEventListener('DOMContentLoaded', addScrollAttributes);