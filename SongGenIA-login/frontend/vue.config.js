module.exports = {
  transpileDependencies: true,
  devServer: {
    proxy: {
      "/api/auth": {
        target: "http://127.0.0.1:3000",  // Asegúrate de que el backend esté en este puerto
        changeOrigin: true
      },
      "/api/music": {
        target: "http://127.0.0.1:5000",  // Si estás usando otro backend para música
        changeOrigin: true
      }
    }
  }
};
