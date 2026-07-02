export default function DashboardCard({ title, value, color }) {
  return (
    <div
      style={{
        background: "#fff",
        borderRadius: "15px",
        padding: "25px",
        boxShadow: "0 5px 15px rgba(0,0,0,.08)",
        borderLeft: `6px solid ${color}`,
        flex: 1,
        minWidth: "180px",
      }}
    >
      <h4
        style={{
          color: "#666",
          marginBottom: "15px",
        }}
      >
        {title}
      </h4>

      <h1
        style={{
          color: "#111",
          margin: 0,
          fontSize: "38px",
        }}
      >
        {value}
      </h1>
    </div>
  );
}