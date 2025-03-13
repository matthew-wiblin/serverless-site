import { apiConfig } from './config';

export const fetchHello = async () => {
  const response = await fetch(`${apiConfig.hello}`);
  const data = await response.json();
  console.log(data);
  return data
};
