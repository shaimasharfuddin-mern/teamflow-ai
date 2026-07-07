import { useState, useEffect } from "react";

export default function TeamForm({
  onSubmit,
  initialData = null,
  buttonText = "Create Team",
}) {
  const [name, setName] = useState("");
  const [description, setDescription] = useState("");

  useEffect(() => {
    if (initialData) {
      setName(initialData.name);
      setDescription(initialData.description || "");
    }
  }, [initialData]);

  async function handleSubmit(e) {
    e.preventDefault();

    if (!name.trim()) return;

    await onSubmit({
      name,
      description,
    });

    if (!initialData) {
      setName("");
      setDescription("");
    }
  }

  return (
    <div
      style={{
        background: "white",
        padding: "25px",
        borderRadius: "12px",
        marginBottom: "30px",
        boxShadow: "0 5px 15px rgba(0,0,0,.08)",
      }}
    >
      <h2>{buttonText}</h2>

      <form onSubmit={handleSubmit}>
        <input
          placeholder="Team Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          style={{
            width: "100%",
            padding: "12px",
            marginTop: "15px",
            marginBottom: "15px",
          }}
        />

        <textarea
          placeholder="Description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          style={{
            width: "100%",
            height: "90px",
            padding: "12px",
            marginBottom: "15px",
          }}
        />

        <button
          style={{
            background: "#2563eb",
            color: "white",
            border: "none",
            padding: "12px 25px",
            borderRadius: "8px",
            cursor: "pointer",
          }}
        >
          {buttonText}
        </button>
      </form>
    </div>
  );
}