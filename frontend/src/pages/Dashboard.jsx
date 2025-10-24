import React from "react";
import SpendingTrend from "../components/Charts/SpendingTrend";
import ForecastChart from "../components/Charts/ForecastChart";

export default function Dashboard() {
  return (
    <div className="p-8 space-y-8">
      <h1 className="text-2xl font-bold">AI Satın Alma Dashboard</h1>
      <SpendingTrend />
      <ForecastChart />
    </div>
  );
}
