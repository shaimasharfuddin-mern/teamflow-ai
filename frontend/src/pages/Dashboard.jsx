import { useEffect, useState } from "react";

import Layout from "../components/Layout";
import DashboardCard from "../components/DashboardCard";
import RecentTasks from "../components/RecentTasks";

import { getDashboardStats } from "../api/dashboard";

export default function Dashboard() {
  const [data, setData] = useState(null);

  useEffect(() => {
    async function load() {
      const res = await getDashboardStats();
      console.log(res);
      setData(res);
    }

    load();
  }, []);

  if (!data) {
    return (
      <Layout>
        <h2>Loading...</h2>
      </Layout>
    );
  }

 return (
  <Layout user={data.user}>
    <h1>Dashboard Works</h1>

    <div
      style={{
        display: "grid",
        gridTemplateColumns: "repeat(3,1fr)",
        gap: "20px",
      }}
    >
        <DashboardCard title="Teams" value={data.teams} color="blue" />
        <DashboardCard title="Projects" value={data.projects} color="green" />
        <DashboardCard title="Tasks" value={data.tasks} color="orange" />
      </div>

      <RecentTasks />
    </Layout>
  );
}