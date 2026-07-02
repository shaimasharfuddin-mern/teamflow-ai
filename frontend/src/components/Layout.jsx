import Sidebar from "./Sidebar";
import Topbar from "./Topbar";

export default function Layout({ children }) {
  return (
    <div className="layout">
      <Sidebar />

      <div className="content">
        <Topbar />

        <div className="main-content">
          {children}
        </div>
      </div>
    </div>
  );
}