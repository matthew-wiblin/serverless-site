import { useEffect, useState } from "react";
import { apiHandler } from "../lib/apiHandler";

export default function Home() {
  const [message, setMessage] = useState("");

  useEffect(() => {
    const fetchData = async () => {
      const data = await apiHandler("users");
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
