import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";

import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import Teams from "./pages/Teams";
import Projects from "./pages/Projects";
import Tasks from "./pages/Tasks";
import Analytics from "./pages/Analytics";
import Health from "./pages/Health";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Navigate to="/login" />} />

        <Route path="/login" element={<Login />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/teams" element={<Teams />} />
        <Route path="/projects" element={<Projects />} />
        <Route path="/tasks" element={<Tasks />} />
        <Route path="/analytics" element={<Analytics />} />
        <Route path="/health" element={<Health />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;