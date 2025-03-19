const API = import.meta.env.VITE_API_URL

export async function apiHandler(path) {
  const response = await fetch(`${API}` + path);
  const data = await response.json();
  console.log(data);
  return data
};
