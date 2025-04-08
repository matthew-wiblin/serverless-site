const API = import.meta.env.VITE_API_URL;

export async function apiHandler(path, method = "GET", body = null, accessToken = null) {
  const url = `${API}${path}`;
  const headers = { "Content-Type": "application/json" };

  if (accessToken) {
    headers["Authorization"] = `Bearer ${accessToken}`;
  }

  let options = { method, headers };

  if (method === 'GET') {
    console.log(`GET request to ${url}`)
  } else if (['POST', 'PUT', 'PATCH'].includes(method)) {
    if (body !== null) {
      options.body = JSON.stringify(body);
    }
  } else {
    console.log('method supplied not accounted for')
  }
  console.log(options)
  try {
    const response = await fetch(`${url}`, options);
    const data = await response.json();
    console.log('apiHandler data = ', data);
    return data;
  } catch (error) {
    console.log('API HTTP error ', error)
  }
}
