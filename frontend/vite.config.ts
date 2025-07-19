import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import tailwindcss from '@tailwindcss/vite';
import { resolve } from 'path';

// https://vite.dev/config/
export default defineConfig({
    plugins: [vue(), tailwindcss()],
    resolve: {
        alias: {
            '@': resolve(__dirname, 'src'),
        },
    },
    server: {
        port: 5173,
        host: true,
    },
    build: {
        outDir: 'dist',
        sourcemap: false,
    },
    define: {
        'import.meta.env.VITE_API_BASE_URL': JSON.stringify(
            process.env.VITE_API_BASE_URL || 'http://localhost:8000/api',
        ),
    },
});
