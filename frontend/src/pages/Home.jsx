import { useEffect, useState } from "react";
import { apiHandler } from "../lib/apiHandler";
import View from "../components/View.jsx"

export default function Home() {
  const [homeView, setHomeView] = useState("");
  const [webData, setWebData] = useState("");

  useEffect(() => {
    const fetchData = async () => {
      const data = await apiHandler({path: '/view/home', method: 'GET'});
      setHomeView(data)
    };

    const callWeb = async () => {
      const data = await apiHandler({path: '/web', method: 'GET'});
      console.log(data)
      setWebData(data)
    }

    fetchData();
    callWeb();

  }, []);

  return (
    <div>
      <br/>
      <View viewData={homeView}/> 
      <p>{webData.message}</p>
    </div>
  );
}
