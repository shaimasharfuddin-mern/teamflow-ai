import { useEffect, useState } from "react";

import Layout from "../components/Layout";
import TeamForm from "../components/TeamForm";

import {
  getTeams,
  createTeam,
  updateTeam,
  deleteTeam,
} from "../api/team";

export default function Teams() {
  const [teams, setTeams] = useState([]);
  const [loading, setLoading] = useState(true);

  const [editingTeam, setEditingTeam] = useState(null);

  async function loadTeams() {
    try {
      const data = await getTeams();
      setTeams(data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    loadTeams();
  }, []);

  async function handleCreate(team) {
    await createTeam(team);
    loadTeams();
  }

  async function handleUpdate(team) {
    await updateTeam(editingTeam.id, team);

    setEditingTeam(null);

    loadTeams();
  }

  async function handleDelete(id) {
    const ok = window.confirm(
      "Are you sure you want to delete this team?"
    );

    if (!ok) return;

    await deleteTeam(id);

    loadTeams();
  }

  return (
    <Layout>
      <h1
        style={{
          fontSize: "30px",
          marginBottom: "25px",
        }}
      >
        Teams
      </h1>

      <TeamForm
        initialData={editingTeam}
        onSubmit={
          editingTeam
            ? handleUpdate
            : handleCreate
        }
        buttonText={
          editingTeam
            ? "Update Team"
            : "Create Team"
        }
      />

      {loading ? (
        <h3>Loading Teams...</h3>
      ) : teams.length === 0 ? (
        <h3>No Teams Found.</h3>
      ) : (
        teams.map((team) => (
          <div
            key={team.id}
            style={{
              background: "white",
              padding: "20px",
              marginBottom: "20px",
              borderRadius: "12px",
              boxShadow:
                "0 4px 12px rgba(0,0,0,.08)",
            }}
          >
            <h2>{team.name}</h2>

            <p>{team.description}</p>

            <small>
              Owner ID: {team.owner_id}
            </small>

            <div
              style={{
                marginTop: "15px",
                display: "flex",
                gap: "10px",
              }}
            >
              <button
                onClick={() =>
                  setEditingTeam(team)
                }
                style={{
                  padding: "10px 18px",
                  border: "none",
                  borderRadius: "8px",
                  cursor: "pointer",
                  background: "#2563eb",
                  color: "white",
                }}
              >
                ✏ Edit
              </button>

              <button
                onClick={() =>
                  handleDelete(team.id)
                }
                style={{
                  padding: "10px 18px",
                  border: "none",
                  borderRadius: "8px",
                  cursor: "pointer",
                  background: "#ef4444",
                  color: "white",
                }}
              >
                🗑 Delete
              </button>
            </div>
          </div>
        ))
      )}
    </Layout>
  );
}