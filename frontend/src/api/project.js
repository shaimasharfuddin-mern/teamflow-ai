import api from "./axios";

export const getProjects = async (teamId) => {
  const response = await api.get(`/projects/team/${teamId}`);
  return response.data;
};

export const createProject = async (project) => {
  const response = await api.post("/projects", project);
  return response.data;
};

export const updateProject = async (id, project) => {
  const response = await api.put(`/projects/${id}`, project);
  return response.data;
};

export const deleteProject = async (id) => {
  const response = await api.delete(`/projects/${id}`);
  return response.data;
};