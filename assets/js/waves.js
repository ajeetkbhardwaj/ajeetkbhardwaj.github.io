// assets/js/waves.js

// assets/js/waves.js

function initWaves() {
    const canvas = document.getElementById('bg-canvas');
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    let width, height;
    let time = 0;

    function resize() {
        width = canvas.width = window.innerWidth;
        height = canvas.height = window.innerHeight;
    }

    window.addEventListener('resize', resize);
    resize();

    // Wave configuration
    const waves = [
        { amplitude: 60, frequency: 0.01, speed: 0.02, offset: 0 },
        { amplitude: 40, frequency: 0.015, speed: 0.03, offset: Math.PI / 2 },
        { amplitude: 80, frequency: 0.008, speed: 0.015, offset: Math.PI }
    ];

    function render() {
        ctx.clearRect(0, 0, width, height);
        
        // Check if dark theme is active
        const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
        
        ctx.lineWidth = 1.5;

        for (let i = 0; i < waves.length; i++) {
            const wave = waves[i];
            ctx.beginPath();
            
            // Set dynamic colors based on theme
            if (isDark) {
                // Glowy cyan/indigo for dark mode
                ctx.strokeStyle = `rgba(79, 70, 229, ${0.1 + (i * 0.05)})`; 
            } else {
                // Subtle orange/gray for light mode
                ctx.strokeStyle = `rgba(255, 126, 95, ${0.2 + (i * 0.1)})`;
            }

            for (let x = 0; x < width; x += 10) {
                // Calculate y using sine wave math
                const y = Math.sin(x * wave.frequency + time * wave.speed + wave.offset) * wave.amplitude + (height / 2) + (i * 50 - 50);
                
                if (x === 0) {
                    ctx.moveTo(x, y);
                } else {
                    ctx.lineTo(x, y);
                }
            }
            ctx.stroke();
        }

        time += 1;
        requestAnimationFrame(render);
    }

    render();
}

if (document.readyState === 'loading') {
    document.addEventListener("DOMContentLoaded", initWaves);
} else {
    initWaves();
}
