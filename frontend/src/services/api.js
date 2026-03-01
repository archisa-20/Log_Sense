import axios from "axios";

const API_BASE = "http://127.0.0.1:8000/api";

export const uploadLogs = async (file) => {
  const formData = new FormData();
  formData.append("file", file);

  await axios.post(`${API_BASE}/logs/upload`, formData, {
    headers: { "Content-Type": "multipart/form-data" }
  });
};

export const getEvents = async (filters = {}) => {
  const { severity, type, ip, user } = filters;

  const params = {
    severity: severity || undefined,
    event_type: type || undefined,
    ip: ip || undefined,
    user: user || undefined
  };

  const res = await axios.get(`${API_BASE}/events`, { params });
  return res.data;
};

// Backwards-compatible helper used by Dashboard
export const filterEvents = async (filters) => {
  return getEvents(filters);
};
