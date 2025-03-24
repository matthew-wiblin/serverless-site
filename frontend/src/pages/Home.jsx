import { useEffect, useState } from "react";
import { apiHandler } from "../lib/apiHandler";

export default function Home() {
  const [message, setMessage] = useState("");
  const [message2, setMessage2] = useState("");

  useEffect(() => {
    const fetchData = async () => {
      const data = await apiHandler("users");
      setMessage(data.message);
    };
    fetchData();

    const fetchData2 = async () => {
      const data = await apiHandler("");
      setMessage2(data.message);
    };
    fetchData2();
  }, []);

  return (
    <div>
      home
      <p>{message}</p>
      <p>{message2}</p>
    </div>
  );
}
