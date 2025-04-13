import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000/api/';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// LAB ENDPOINTS

export const getLabs = () => api.get('labs/');
export const getLab = (id) => api.get(`labs/${id}/`);
export const createLab = (labData) => api.post('labs/', labData);
export const updateLab = (id, labData) => api.put(`labs/${id}/`, labData);
export const deleteLab = (id) => api.delete(`labs/${id}/`);

export default {
  getLabs,
  getLab,
  createLab,
  updateLab,
  deleteLab,
};
