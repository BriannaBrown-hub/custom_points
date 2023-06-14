import React from "react";

const CalculateCustomPointsButton = ({ fetchLatestValues }) => {
  const handleClick = () => {
    calculateCustomPointValue();
    fetchLatestValues();
  };

  const calculateCustomPointValue = async () => {
    try {
      await fetch("http://localhost:5000/calculate_custom_point_values");
    } catch (error) {
      console.error("Error calculating values", error);
    }
  };

  return (
    <button
      className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
      onClick={handleClick}
    >
      Calculate Custom Points Value
    </button>
  );
};

export default CalculateCustomPointsButton;
