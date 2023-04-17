import { fileURLToPath, URL } from 'url'
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
    server: {
        open: '/',
        proxy: {
            '^/api*': {
                target: 'http://localhost:8080/',
            }

        }
    },
    plugins: [vue()],
    resolve: {
        alias: {
            '@': fileURLToPath(new URL('./src',
                import.meta.url)),
            '~bootstrap': fileURLToPath(new URL('node_modules/bootstrap',
                import.meta.url)),
        }
    },
})