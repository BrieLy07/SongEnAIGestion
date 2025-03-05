<template>
  <div class="home-view">
    <!-- Título con estilo atractivo -->
    <h1 class="app-title">
      🎵 SongGenIA
    </h1>
    
    <!-- Imagen o GIF debajo del título -->
    <div class="image-container">
      <img
        src="ruta/a/tu/imagen-o-gif.gif"
        alt="Imagen o gif"
        class="app-image"
      >
    </div>
    
    <!-- Sección de Login y Registro -->
    <div class="auth-links">
      <p>
        ¿Ya tienes cuenta? <router-link
          to="/login"
          class="auth-link"
        >
          Inicia sesión
        </router-link>
      </p>
      <p>
        ¿No tienes cuenta? <router-link
          to="/register"
          class="auth-link"
        >
          Regístrate
        </router-link>
      </p>
    </div>
  </div>
</template>

<script>
export default {
  name: "HomeView",
};
</script>

<style scoped>

.home-view {
  text-align: center;
  padding: 0; 
  background-color: rgba(75, 140, 158, 0.456); 
  height: 90vh; 
  display: flex;
  flex-direction: column;
  justify-content: center; 
  align-items: center; 
}

.app-title {
  font-size: 3rem;
  font-weight: bold;
  color: #4CAF50; /* Verde, puedes cambiarlo */
  margin-bottom: 20px;
}

.image-container {
  margin: 20px 0;
}

.app-image {
  width: 80%;
  max-width: 500px; /* Ajusta el tamaño del gif/imagen */
  height: auto;
}

.auth-links {
  margin-top: 30px;
  text-align: center;
}

.auth-link {
  color: #212a76;
  text-decoration: none;
  border: 2px solid transparent;
  padding: 5px 40px;
  border-radius: 25px;
  background-color: hsla(196, 72%, 28%, 0.536); /* Botón transparente con borde sin color */
  font-size: 1.1rem;
  transition: all 0.3s ease;
}

.auth-link:hover {
  background-color: rgba(0, 123, 255, 0.2);
  color: #fff;
}
</style>