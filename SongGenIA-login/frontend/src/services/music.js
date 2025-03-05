import axios from "axios";
import { MUSIC_API_URL } from "./api"; // Importamos la URL base

// Función para generar una canción
export const generateMusic = async (lyrics, genre, mood) => {
  try {
    const response = await axios.post(`${MUSIC_API_URL}/generate-music`, {
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
    const response = await axios.get(`${MUSIC_API_URL}/get-audio/${taskId}`);
    return response.data;
  } catch (error) {
    console.error("Error al obtener el audio:", error);
    return { error: "No se pudo obtener el audio" };
  }
};
