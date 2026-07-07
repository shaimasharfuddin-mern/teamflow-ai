import axios from "axios";

const api = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

api.interceptors.request.use((config) => {
  const token = localStorage.getItem("token");

  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }

  return config;
});


api.interceptors.request.use((config) => {
  console.log("REQUEST URL:", config.url);
  console.log("AUTH HEADER:", config.headers.Authorization);

  const token = localStorage.getItem("token");

  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }

  console.log("FINAL HEADER:", config.headers.Authorization);

  return config;
});

export default api;
