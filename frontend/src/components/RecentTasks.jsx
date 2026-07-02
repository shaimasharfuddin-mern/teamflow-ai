export default function RecentTasks() {
  const tasks = [
    "Design Login Page",
    "Implement JWT",
    "Fix Dashboard API",
    "Create Analytics",
    "Deploy Backend",
  ];

  return (
    <div
      style={{
        background: "white",
        marginTop: "30px",
        padding: "25px",
        borderRadius: "15px",
        boxShadow: "0 5px 15px rgba(0,0,0,.08)",
      }}
    >
      <h2>Recent Tasks</h2>

      <ul>
        {tasks.map((task, index) => (
          <li key={index} style={{ margin: "15px 0" }}>
            ✅ {task}
          </li>
        ))}
      </ul>
    </div>
  );
}