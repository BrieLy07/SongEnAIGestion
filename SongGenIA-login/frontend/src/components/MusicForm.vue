<template>
  <div class="music-form">
    <h2>🎶 Genera tu Canción con IA</h2>
    <form @submit.prevent="submitForm">
      <label>📝 Escribe una frase:</label>
      <input
        v-model="lyrics"
        type="text"
        placeholder="Escribe aquí..."
        required
      >

      <label>🎼 Género:</label>
      <select v-model="genre">
        <option>Pasillo</option>
        <option>Sanjuanito</option>
        <option>Albazo</option>
      </select>

      <label>😊 Estado de ánimo:</label>
      <select v-model="mood">
        <option>Alegre</option>
        <option>Triste</option>
        <option>Romántico</option>
      </select>

      <button type="submit">
        🎤 Generar Canción
      </button>
    </form>

    <p v-if="loading">
      ⌛ Generando canción...
    </p>
    <p v-if="taskId">
      ✅ ID de tarea: {{ taskId }}
    </p>
  </div>
</template>

<script>
import { generateMusic } from "@/services/music";

export default {
  data() {
    return {
      lyrics: "",
      genre: "Pasillo",
      mood: "Alegre",
      taskId: null,
      loading: false
    };
  },
  methods: {
    async submitForm() {
      this.loading = true;
      const response = await generateMusic(this.lyrics, this.genre, this.mood);
      if (response.data) {
        this.taskId = response.data.taskId;
      } else {
        alert("Error al generar la canción");
      }
      this.loading = false;
    }
  }
};
</script>

<style scoped>
.music-form {
  max-width: 400px;
  margin: auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 8px;
}
</style>
