import React from "react";
import LatestValues from "./components/LatestValues";

export default function App() {
  return (
    <div className="container mx-auto bg-gray-200 rounded-xl shadow border p-8 m-10">
      <p className="text-3xl font-bold text-blue-600 pb-2">Custom Points</p>
      <LatestValues />
    </div>
  );
}
