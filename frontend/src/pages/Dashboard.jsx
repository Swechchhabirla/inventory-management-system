import { useEffect, useState } from "react";
import API from "../services/api";

function Dashboard() {

  const [stats, setStats] = useState({});

  useEffect(() => {
    fetchDashboard();
  }, []);

  const fetchDashboard = async () => {
    const response = await API.get("/dashboard");
    setStats(response.data);
  };

  return (
    <div className="p-6">

      <h1 className="text-3xl font-bold mb-6">
        Dashboard
      </h1>

      <div className="grid grid-cols-2 gap-4">

        <div className="bg-blue-100 p-4 rounded">
          <h2>Total Products</h2>
          <p className="text-2xl">
            {stats.total_products}
          </p>
        </div>

        <div className="bg-green-100 p-4 rounded">
          <h2>Total Customers</h2>
          <p className="text-2xl">
            {stats.total_customers}
          </p>
        </div>

        <div className="bg-yellow-100 p-4 rounded">
          <h2>Total Orders</h2>
          <p className="text-2xl">
            {stats.total_orders}
          </p>
        </div>

        <div className="bg-red-100 p-4 rounded">
          <h2>Low Stock Products</h2>
          <p className="text-2xl">
            {stats.low_stock_products}
          </p>
        </div>

      </div>

    </div>
  );
}

export default Dashboard;