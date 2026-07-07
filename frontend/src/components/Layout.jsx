import Sidebar from "./Sidebar";
import Topbar from "./Topbar";

export default function Layout({ children, user }) {
  return (
    <div className="layout">
      <Sidebar />

      <div className="content">
        <Topbar user={user} />

        <div className="main-content">
          {children}
        </div>
      </div>
    </div>
  );
}