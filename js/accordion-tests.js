// Accordion Tests for Browser Console
// Run these tests in the browser console to verify accordion functionality

// Test 1: Check if all analysis headers exist
function testAnalysisHeadersExist() {
    const headers = document.querySelectorAll('.analysis-header');
    console.log(`✅ Test 1 - Analysis headers found: ${headers.length}`);
    console.log('Headers:', Array.from(headers).map(h => h.textContent.trim().substring(0, 10) + '...'));
    return headers.length === 6;
}

// Test 2: Check ARIA attributes
function testAriaAttributes() {
    const headers = document.querySelectorAll('.analysis-header');
    let allValid = true;

    headers.forEach((header, index) => {
        const hasRole = header.getAttribute('role') === 'button';
        const hasTabindex = header.getAttribute('tabindex') === '0';
        const hasAriaExpanded = header.hasAttribute('aria-expanded');
        const hasAriaControls = header.hasAttribute('aria-controls');

        const valid = hasRole && hasTabindex && hasAriaExpanded && hasAriaControls;
        console.log(`✅ Test 2.${index + 1} - ${header.textContent.trim().substring(0, 15)}...: ARIA valid: ${valid}`);

        if (!valid) {
            console.log('  Missing attributes:', {
                role: hasRole,
                tabindex: hasTabindex,
                'aria-expanded': hasAriaExpanded,
                'aria-controls': hasAriaControls
            });
            allValid = false;
        }
    });

    return allValid;
}

// Test 3: Test click functionality
function testClickFunctionality() {
    const headers = document.querySelectorAll('.analysis-header');
    let allWorking = true;

    headers.forEach((header, index) => {
        const initialExpanded = header.getAttribute('aria-expanded');
        const content = header.nextElementSibling;
        const initialOpen = content.classList.contains('open');

        // Simulate click
        header.click();

        const newExpanded = header.getAttribute('aria-expanded');
        const newOpen = content.classList.contains('open');

        const toggled = initialExpanded !== newExpanded && initialOpen !== newOpen;
        console.log(`✅ Test 3.${index + 1} - Click toggle works: ${toggled}`);

        if (!toggled) {
            console.log('  Initial state:', { expanded: initialExpanded, open: initialOpen });
            console.log('  New state:', { expanded: newExpanded, open: newOpen });
            allWorking = false;
        }

        // Reset for next test
        if (newOpen) {
            header.click();
        }
    });

    return allWorking;
}

// Test 4: Test keyboard functionality
function testKeyboardFunctionality() {
    const headers = document.querySelectorAll('.analysis-header');
    let allWorking = true;

    headers.forEach((header, index) => {
        const initialExpanded = header.getAttribute('aria-expanded');

        // Simulate Enter key
        const enterEvent = new KeyboardEvent('keydown', { key: 'Enter' });
        header.dispatchEvent(enterEvent);

        const newExpanded = header.getAttribute('aria-expanded');
        const toggled = initialExpanded !== newExpanded;

        console.log(`✅ Test 4.${index + 1} - Enter key works: ${toggled}`);

        if (!toggled) {
            allWorking = false;
        }

        // Reset for next test
        if (header.getAttribute('aria-expanded') === 'true') {
            header.click();
        }
    });

    return allWorking;
}

// Test 5: Test mobile touch targets
function testMobileTouchTargets() {
    const headers = document.querySelectorAll('.analysis-header');
    let allValid = true;

    headers.forEach((header, index) => {
        const rect = header.getBoundingClientRect();
        const minTouchTarget = 44; // WCAG minimum

        const valid = rect.height >= minTouchTarget && rect.width >= minTouchTarget;
        console.log(`✅ Test 5.${index + 1} - Touch target size: ${rect.width.toFixed(0)}x${rect.height.toFixed(0)}px - Valid: ${valid}`);

        if (!valid) {
            allValid = false;
        }
    });

    return allValid;
}

// Test 6: Test content visibility
function testContentVisibility() {
    const headers = document.querySelectorAll('.analysis-header');
    let allWorking = true;

    headers.forEach((header, index) => {
        const content = header.nextElementSibling;

        // Open accordion
        header.click();

        // Check if content is visible
        const isVisible = content.classList.contains('open') &&
                         window.getComputedStyle(content).maxHeight !== '0px';

        console.log(`✅ Test 6.${index + 1} - Content visible when open: ${isVisible}`);

        if (!isVisible) {
            console.log('  Content classes:', content.className);
            console.log('  Max height:', window.getComputedStyle(content).maxHeight);
            allWorking = false;
        }

        // Close accordion
        header.click();
    });

    return allWorking;
}

// Test 7: Test images load correctly
function testImagesLoad() {
    const images = document.querySelectorAll('img[loading="lazy"]');
    let loadedCount = 0;

    images.forEach((img, index) => {
        if (img.complete && img.naturalHeight !== 0) {
            loadedCount++;
        }
    });

    const allLoaded = loadedCount === images.length;
    console.log(`✅ Test 7 - Images loaded: ${loadedCount}/${images.length} - All loaded: ${allLoaded}`);

    return allLoaded;
}

// Test 8: Test figcaption presence
function testFigcaptions() {
    const figures = document.querySelectorAll('figure');
    let allHaveCaptions = true;

    figures.forEach((figure, index) => {
        const hasFigcaption = figure.querySelector('figcaption') !== null;
        console.log(`✅ Test 8.${index + 1} - Figure has figcaption: ${hasFigcaption}`);

        if (!hasFigcaption) {
            allHaveCaptions = false;
        }
    });

    return allHaveCaptions;
}

// Run all tests
function runAllAccordionTests() {
    console.log('🚀 Running Accordion Tests...\n');

    const results = [
        testAnalysisHeadersExist(),
        testAriaAttributes(),
        testClickFunctionality(),
        testKeyboardFunctionality(),
        testMobileTouchTargets(),
        testContentVisibility(),
        testImagesLoad(),
        testFigcaptions()
    ];

    const passed = results.filter(r => r).length;
    const total = results.length;

    console.log(`\n📊 Test Results: ${passed}/${total} tests passed`);

    if (passed === total) {
        console.log('🎉 All tests passed! Accordions are working correctly.');
    } else {
        console.log('⚠️ Some tests failed. Check the output above for details.');
    }

    return { passed, total, results };
}

// Make tests available globally
window.AccordionTests = {
    runAll: runAllAccordionTests,
    testHeaders: testAnalysisHeadersExist,
    testAria: testAriaAttributes,
    testClick: testClickFunctionality,
    testKeyboard: testKeyboardFunctionality,
    testTouch: testMobileTouchTargets,
    testVisibility: testContentVisibility,
    testImages: testImagesLoad,
    testCaptions: testFigcaptions
};

// Auto-run tests when script loads (optional)
console.log('💡 Accordion tests loaded. Run AccordionTests.runAll() to execute all tests.');