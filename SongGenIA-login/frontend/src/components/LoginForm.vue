<template>
  <div class="app-body">
    <div class="login-form">
      <h2>🔑 Iniciar sesión</h2>
      <form @submit.prevent="submitLogin">
        <div class="form-group">
          <label for="email">📧 Correo electrónico:</label>
          <input
            id="email"
            v-model="email"
            type="email"
            placeholder="Ingresa tu correo"
            required
          >
        </div>

        <div class="form-group">
          <label for="password">🔒 Contraseña:</label>
          <input
            id="password"
            v-model="password"
            type="password"
            placeholder="Ingresa tu contraseña"
            required
          >
        </div>

        <button type="submit">
          Iniciar sesión
        </button>
      </form>

      <button @click="googleLogin">
        🟢 Iniciar sesión con Google
      </button>

      <p
        v-if="errorMessage"
        class="error"
      >
        {{ errorMessage }}
      </p>
    </div>
  </div>
</template>

<script>
import { login, loginWithGoogle } from "@/services/auth";

export default {
  data() {
    return {
      email: "",
      password: "",
      errorMessage: null,
    };
  },
  mounted() {
    
    const urlParams = new URLSearchParams(window.location.search);
    const token = urlParams.get('token');
    if (token) {
      localStorage.setItem("authToken", token);  
      this.$router.push("/dashboard");  
    }
  },
  methods: {
    async submitLogin() {
      try {
        const response = await login(this.email, this.password);

        if (response.token) {
          localStorage.setItem("authToken", response.token); 
          this.$router.push("/dashboard"); 
        } else {
          this.errorMessage = response.error || "Credenciales incorrectas.";
        }
      } catch (error) {
        this.errorMessage = "Error al iniciar sesión. Inténtalo de nuevo.";
      }
    },

    // Inicia sesión con Google
    googleLogin() {
      loginWithGoogle();  // Llamada al backend para la autenticación con Google
    },
  }
};
</script>

<style scoped>

.app-body {
  background-color: #11686448; 
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  min-height: 89vh; 
  display: flex;
  justify-content: center; 
  align-items: flex-start; 
  padding-top: 50px; 
}


.login-form {
  max-width: 450px; 
  padding: 30px;
  border-radius: 10px;
  background-color: #caf0ef; 
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1); 
  width: 100%; 
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  margin-bottom: 8px;
  font-weight: bold;
}

input {
  width: 100%;
  padding: 10px;
  font-size: 16px;
  border-radius: 25px;
  border: 1px solid #ccc;
}

button {
  width: 100%;
  padding: 10px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  font-size: 16px;
  cursor: pointer;
  margin-top: 20px;
}

button:hover {
  background-color: #0056b3;
}

button:focus {
  outline: none;
}

.error {
  color: red;
  font-size: 14px;
  margin-top: 15px;
  text-align: center;
}
</style>