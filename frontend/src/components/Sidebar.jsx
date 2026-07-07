import { NavLink } from "react-router-dom";

import {
  FaHome,
  FaUsers,
  FaFolderOpen,
  FaTasks,
  FaChartBar,
  FaHeartbeat,
  FaCog,
  FaSignOutAlt,
} from "react-icons/fa";

export default function Sidebar() {
  const menu = [
    {
      name: "Dashboard",
      icon: <FaHome />,
      path: "/dashboard",
    },
    {
      name: "Teams",
      icon: <FaUsers />,
      path: "/teams",
    },
    {
      name: "Projects",
      icon: <FaFolderOpen />,
      path: "/projects",
    },
    {
      name: "Tasks",
      icon: <FaTasks />,
      path: "/tasks",
    },
    {
      name: "Analytics",
      icon: <FaChartBar />,
      path: "/analytics",
    },
    {
      name: "Health",
      icon: <FaHeartbeat />,
      path: "/health",
    },
  ];

  return (
    <div className="sidebar">
      <h2 className="logo">TeamFlow AI</h2>

      <nav>
        {menu.map((item) => (
          <NavLink
            key={item.name}
            to={item.path}
            className={({ isActive }) =>
              isActive ? "menu active" : "menu"
            }
          >
            <span>{item.icon}</span>
            <span>{item.name}</span>
          </NavLink>
        ))}
      </nav>

      <button className="logout-btn">
        <FaSignOutAlt />
        Logout
      </button>
    </div>
  );
}