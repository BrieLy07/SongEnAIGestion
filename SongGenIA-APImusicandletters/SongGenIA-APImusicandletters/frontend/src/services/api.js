import axios from "axios";

const API_URL = "http://127.0.0.1:5000"; // URL del backend en Flask

// Función para generar una canción
export const generateMusic = async (lyrics, genre, mood) => {
  try {
    const response = await axios.post(`${API_URL}/generate-music`, {
      lyrics,
      genre,
      mood,
    });
    return response.data;
  } catch (error) {
    console.error("Error al generar la música:", error);
    return { error: "No se pudo generar la canción" };
  }
};

// Función para obtener el audio generado
export const getAudio = async (taskId) => {
  try {
    const response = await axios.get(`${API_URL}/get-audio/${taskId}`);
    return response.data;
  } catch (error) {
    console.error("Error al obtener el audio:", error);
    return { error: "No se pudo obtener el audio" };
  }
};
