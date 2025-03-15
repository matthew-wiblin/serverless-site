export async function apiHandler(path) {
  const response = await fetch(`${import.meta.env.VITE_API_URL}` + path);
  const data = await response.json();
  console.log(data);
  return data
};
