import { useEffect, useState } from "react";

import Sidebar from "../components/Sidebar";
import Topbar from "../components/Topbar";
import DashboardCard from "../components/DashboardCard";
import RecentTasks from "../components/RecentTasks";

import { getDashboardStats } from "../api/dashboard";

export default function Dashboard() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchDashboard() {
      try {
        const response = await getDashboardStats();
        setData(response);
      } catch (error) {
        console.error(error);
      } finally {
        setLoading(false);
      }
    }

    fetchDashboard();
  }, []);

  if (loading) {
    return <h2 style={{ padding: 40 }}>Loading Dashboard...</h2>;
  }

  if (!data) {
    return <h2 style={{ padding: 40 }}>Failed to load dashboard.</h2>;
  }

  return (
    <div
      style={{
        display: "flex",
        background: "#F4F7FB",
        minHeight: "100vh",
      }}
    >
      <Sidebar />

      <div
        style={{
          flex: 1,
        }}
      >
        <Topbar user={data.user} />

        <div style={{ padding: "30px" }}>
          <div
            style={{
              display: "grid",
              gridTemplateColumns: "repeat(auto-fit,minmax(220px,1fr))",
              gap: "20px",
            }}
          >
            <DashboardCard
              title="Teams"
              value={data.teams}
              color="#2563EB"
            />

            <DashboardCard
              title="Projects"
              value={data.projects}
              color="#10B981"
            />

            <DashboardCard
              title="Tasks"
              value={data.tasks}
              color="#F59E0B"
            />

            <DashboardCard
              title="Completed"
              value={data.completed_tasks}
              color="#22C55E"
            />

            <DashboardCard
              title="Pending"
              value={data.pending_tasks}
              color="#EF4444"
            />

            <DashboardCard
              title="Health %"
              value={`${data.health}%`}
              color="#8B5CF6"
            />
          </div>

          <RecentTasks />
        </div>
      </div>
    </div>
  );
}