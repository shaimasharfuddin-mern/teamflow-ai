import { FaBell, FaSearch, FaUserCircle } from "react-icons/fa";

export default function Topbar({ user }) {
  return (
    <div className="topbar">
      <h2>Dashboard</h2>

      <div className="topbar-right">
        <div className="search-box">
          <FaSearch />

          <input
            type="text"
            placeholder="Search..."
          />
        </div>

        <button className="notification-btn">
          <FaBell />
        </button>

        <div className="user-info">
          <FaUserCircle className="avatar" />

          <span>{user}</span>
        </div>
      </div>
    </div>
  );
}