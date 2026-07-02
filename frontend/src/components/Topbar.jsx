export default function Topbar({ user }) {
  return (
    <div
      style={{
        background: "white",
        padding: "20px 30px",
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center",
        boxShadow: "0 2px 8px rgba(0,0,0,.08)",
      }}
    >
      <h2>Dashboard</h2>

      <h4>{user}</h4>
    </div>
  );
}