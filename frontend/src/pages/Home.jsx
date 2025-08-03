import { useEffect, useState } from "react";
import { apiHandler } from "../lib/apiHandler";
import View from "../components/View.jsx"

export default function Home() {
  const [homeView, setHomeView] = useState("");

  useEffect(() => {
    const fetchData = async () => {
      const data = await apiHandler({path: '/view/home', method: 'GET'});
      setHomeView(data)
    };
    fetchData();
  }, []);

  return (
    <div>
      <br/>
      <View viewData={homeView}/> 
    </div>
  );
}
