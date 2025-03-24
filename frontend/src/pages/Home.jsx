import { useEffect, useState } from "react";
import { apiHandler } from "../lib/apiHandler";

export default function Home() {
  const [message, setMessage] = useState("");
  const [message2, setMessage2] = useState("");
  const [input, setInput] = useState("");

  useEffect(() => {
    const fetchData = async () => {
      const data = await apiHandler("");
      setMessage(data.message);
    };
    fetchData();
  }, []);

  const writeToDB = async (method) => {
    const data = await apiHandler("create", method, { data: input })
    setMessage2(data.message)
  }

  return (
    <div>
      home
      <p>{message}</p>
      <p>{message2}</p>
      <div>
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type something"
        />
        <button onClick={() => writeToDB("POST")}>Send to API</button>
      </div>    
    </div>
  );
}
