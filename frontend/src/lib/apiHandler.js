const API = import.meta.env.VITE_API_URL;

export async function apiHandler(path, method = "GET", body = null) {
  const options = {
    method,
    headers: {
      "Content-Type": "application/json",
    },
  };

  if (body !== null) {
    options.body = JSON.stringify(body);
  }

  const response = await fetch(`${API}${path}`, options);
  const data = await response.json();
  console.log(data);
  return data;
}
