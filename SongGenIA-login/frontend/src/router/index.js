import { createRouter, createWebHistory } from 'vue-router';
import HomeView from "@/views/HomeView.vue";
import LoginForm from "@/components/LoginForm.vue";
import RegisterForm from "@/components/RegisterForm.vue";
import MusicForm from "@/components/MusicForm.vue";  // Vista de Música

const routes = [
  { path: "/", component: HomeView },
  { path: "/login", component: LoginForm },
  { path: "/register", component: RegisterForm },
  { 
    path: "/dashboard", 
    component: MusicForm, // La vista de música debe ir aquí
    beforeEnter: (to, from, next) => {
      const token = localStorage.getItem("authToken");
      if (token) {
        next(); // Permitir el acceso a la vista si está autenticado
      } else {
        next("/login"); // Redirigir al login si no está autenticado
      }
    }
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
