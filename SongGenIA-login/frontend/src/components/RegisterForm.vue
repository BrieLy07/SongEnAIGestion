<template>
  <div class="app-body">
    <div class="register-container">
      <h2 class="app-title">
        🆕Registro de Usuario
      </h2>
      <form @submit.prevent="register">
        <div class="form-group">
          <label for="nombre">Nombre</label>
          <input
            id="nombre"
            v-model="user.nombre"
            type="text"
            required
          >
        </div>
        <div class="form-group">
          <label for="cedula">Cédula</label>
          <input
            id="cedula"
            v-model="user.cedula"
            type="text"
            required
          >
        </div>
        <div class="form-group">
          <label for="telefono">Teléfono</label>
          <input
            id="telefono"
            v-model="user.telefono"
            type="text"
            required
          >
        </div>
        <div class="form-group">
          <label for="email">Email</label>
          <input
            id="email"
            v-model="user.email"
            type="email"
            required
          >
        </div>
        <div class="form-group">
          <label for="username">Usuario</label>
          <input
            id="username"
            v-model="user.username"
            type="text"
            required
          >
        </div>
        <div class="form-group">
          <label for="password">Contraseña</label>
          <input
            id="password"
            v-model="user.password"
            type="password"
            required
          >
        </div>
        <button type="submit">
          Registrar
        </button>
        <p
          v-if="error"
          class="error"
        >
          {{ error }}
        </p>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      user: {
        nombre: "",
        cedula: "",
        telefono: "",
        email: "",
        username: "",
        password: ""
      },
      error: null
    };
  },
  methods: {
    async register() {
      try {
        const response = await axios.post("http://localhost:3000/register", this.user);
        alert(response.data.msg);
        this.$router.push("/login");
      } catch (error) {
        this.error = error.response?.data?.msg || "Error al registrar el usuario";
      }
    }
  }
};
</script>

<style scoped>
/* Fondo de la página personalizable */
.app-body {
  background-color: #11686448; 
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  min-height: 90vh; 
  display: flex;
  justify-content: center; 
  align-items: flex-start; 
  padding-top: 50px; 
}


.register-container {
  max-width: 450px; 
  padding: 30px;
  border-radius: 10px;
  background-color: #caf0ef; 
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1); 
  width: 100%; 
}

/* Título */
.app-title {
  font-size: 2rem;
  font-weight: bold;
  color: #1f8724b0; 
  margin-bottom: 20px;
}


/* Estilo de los grupos de formulario */
.form-group {
  margin-bottom: 20px;
}

/* Estilo de las etiquetas alineadas a la izquierda */
label {
  display: block;
  font-weight: bold;
  margin-bottom: 5px;
  color: #333;
  text-align: left; 
}

/* Estilo de los campos de texto */
input {
  width: 80%;
  border: 1px solid #9be7bf59;
  padding: 8px 40px;
  border-radius: 25px;
  font-size: 1rem;
  margin-top: 5px;
  background-color: #4dbea0c9;
}

/* Estilo del botón */
button {
  width: 100%;
  color: #212a76;
  text-decoration: none;
  border: 2px solid transparent;
  padding: 5px 40px;
  border-radius: 25px;
  background-color: hsla(196, 72%, 28%, 0.536); /* Botón transparente con borde sin color */
  font-size: 1.1rem;
  transition: background-color 0.3s;
}

/* Efecto hover en el botón */
button:hover {
  background-color: #45a049;
}

/* Estilo del mensaje de error */
.error {
  color: #e74c3c;
  font-size: 0.9rem;
  margin-top: 10px;
  text-align: center;
}
</style>
