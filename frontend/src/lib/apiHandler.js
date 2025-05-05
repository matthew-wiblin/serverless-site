const API = import.meta.env.VITE_API_URL;

export async function apiHandler({ path, method, queryParams, body, accessToken }) {
  var url = `${API}${path}`;
  const headers = { "Content-Type": "application/json" };
  let options = { method, headers };

  if (!(path && method)) { return `invalid path and method - ${path}, ${method}` }

  if (accessToken) { headers["Authorization"] = `Bearer ${accessToken}`; }
  if (queryParams && typeof queryParams === 'object') {
    const query = new URLSearchParams(queryParams).toString();
    url += `?${query}`;
  }
  if (['POST', 'PUT', 'PATCH'].includes(method)) {
    if (body !== null) { options.body = JSON.stringify(body); }
  }

  console.log(`URL = ${url.split('.com')[1]}`)

  try {
    const response = await fetch(`${url}`, options);
    const data = await response.json();
    console.log('apiHandler data = ', data);
    return data;
  } catch (error) {
    console.log('API HTTP error ', error)
  }
}
