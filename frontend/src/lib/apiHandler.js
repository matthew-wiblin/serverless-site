import { apiConfig } from './config';

export async function apiHandler (path) {
  const response = await fetch(`${apiConfig[path]}`);
  const data = await response.json();
  console.log(data);
  return data
};
