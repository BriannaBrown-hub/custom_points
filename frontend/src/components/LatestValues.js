import React, { useState, useEffect } from "react";
import CalculateCustomPointsButton from "./CalculateCustomPointsButton";
import LatestValuesTable from "./LatestValuesTable";
import CustomPointModal from "./CreateCustomPointModal";

const App = () => {
  const [latestValues, setLatestValues] = useState([]);

  useEffect(() => {
    fetchLatestValues();
  }, []);

  const fetchLatestValues = async () => {
    try {
      const response = await fetch("http://localhost:5000/get_latest_points");
      const jsonData = await response.json();
      setLatestValues(jsonData);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  return (
    <div>
      <div className="flex justify-between py-5">
        <CalculateCustomPointsButton fetchLatestValues={fetchLatestValues} />
        <CustomPointModal />
      </div>
      {latestValues.length > 0 && <LatestValuesTable data={latestValues} />}
    </div>
  );
};

export default App;
