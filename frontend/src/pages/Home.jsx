import { useEffect, useState } from "react";
import { fetchHello } from "../lib/apiHandler";

export default function Home() {
  const [message, setMessage] = useState("");

  useEffect(() => {
    const fetchData = async () => {
      const data = await fetchHello();
      setMessage(data.message);
    };

    fetchData();
  }, []);

  return (
    <div>
      home
      <p>{message}</p>
    </div>
  );
}
