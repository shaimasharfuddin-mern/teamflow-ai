import { useState } from "react";

export default function ProjectForm({
  teams,
  onSubmit,
  initialData = null,
}) {
  const [name, setName] = useState(initialData?.name || "");
  const [description, setDescription] = useState(
    initialData?.description || ""
  );

  const [teamId, setTeamId] = useState(
    initialData?.team_id || ""
  );

  function handleSubmit(e) {
    e.preventDefault();

    onSubmit({
      name,
      description,
      team_id: Number(teamId),
    });

    if (!initialData) {
      setName("");
      setDescription("");
      setTeamId("");
    }
  }

  return (
    <form
      onSubmit={handleSubmit}
      style={{
        background: "white",
        padding: "25px",
        borderRadius: "12px",
        marginBottom: "30px",
        boxShadow: "0 5px 15px rgba(0,0,0,.08)",
      }}
    >
      <h2 style={{ marginBottom: "20px" }}>
        {initialData ? "Edit Project" : "Create Project"}
      </h2>

      <input
        type="text"
        placeholder="Project Name"
        value={name}
        onChange={(e) => setName(e.target.value)}
        required
        style={inputStyle}
      />

      <textarea
        placeholder="Description"
        value={description}
        onChange={(e) => setDescription(e.target.value)}
        style={{
          ...inputStyle,
          height: "90px",
        }}
      />

      <select
        value={teamId}
        onChange={(e) => setTeamId(e.target.value)}
        required
        style={inputStyle}
      >
        <option value="">Select Team</option>

        {teams.map((team) => (
          <option
            key={team.id}
            value={team.id}
          >
            {team.name}
          </option>
        ))}
      </select>

      <button
        type="submit"
        style={buttonStyle}
      >
        {initialData ? "Update Project" : "Create Project"}
      </button>
    </form>
  );
}

const inputStyle = {
  width: "100%",
  padding: "12px",
  marginBottom: "15px",
  borderRadius: "8px",
  border: "1px solid #ddd",
  fontSize: "15px",
};

const buttonStyle = {
  background: "#2563EB",
  color: "white",
  border: "none",
  padding: "12px 25px",
  borderRadius: "8px",
  cursor: "pointer",
};