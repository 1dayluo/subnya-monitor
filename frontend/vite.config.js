import { defineConfig } from 'vite'

export default defineConfig({
  build: {
    outDir: '../static', // 将构建输出设置为 Flask 的静态文件目录
  },
  plugins: [vue()]

})