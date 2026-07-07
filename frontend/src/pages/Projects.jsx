import { useEffect, useState } from "react";

import Layout from "../components/Layout";
import ProjectForm from "../components/ProjectForm";

import {
  getProjects,
  createProject,
  updateProject,
  deleteProject,
} from "../api/project";

import { getTeams } from "../api/team";

export default function Projects() {
  const [teams, setTeams] = useState([]);
  const [selectedTeam, setSelectedTeam] = useState("");
  const [projects, setProjects] = useState([]);
  const [editingProject, setEditingProject] = useState(null);

  async function loadTeams() {
    try {
      const data = await getTeams();
      setTeams(data);

      if (data.length > 0) {
        setSelectedTeam(data[0].id);
      }
    } catch (err) {
      console.error(err);
    }
  }

  async function loadProjects(teamId) {
    if (!teamId) return;

    try {
      const data = await getProjects(teamId);
      setProjects(data);
    } catch (err) {
      console.error(err);
    }
  }

  useEffect(() => {
    loadTeams();
  }, []);

  useEffect(() => {
    if (selectedTeam) {
      loadProjects(selectedTeam);
    }
  }, [selectedTeam]);

  async function handleCreate(project) {
    await createProject(project);

    loadProjects(selectedTeam);
  }

  async function handleUpdate(project) {
    await updateProject(editingProject.id, project);

    setEditingProject(null);

    loadProjects(selectedTeam);
  }

  async function handleDelete(id) {
    if (!window.confirm("Delete this project?")) return;

    await deleteProject(id);

    loadProjects(selectedTeam);
  }

  return (
    <Layout>
      <h1
        style={{
          marginBottom: "25px",
        }}
      >
        Projects
      </h1>

      <div
        style={{
          marginBottom: "25px",
        }}
      >
        <label
          style={{
            marginRight: "10px",
            fontWeight: "bold",
          }}
        >
          Team:
        </label>

        <select
          value={selectedTeam}
          onChange={(e) => setSelectedTeam(Number(e.target.value))}
          style={{
            padding: "10px",
            borderRadius: "8px",
          }}
        >
          {teams.map((team) => (
            <option
              key={team.id}
              value={team.id}
            >
              {team.name}
            </option>
          ))}
        </select>
      </div>

      <ProjectForm
        teams={teams}
        onSubmit={
          editingProject
            ? handleUpdate
            : handleCreate
        }
        initialData={editingProject}
      />

      {projects.length === 0 ? (
        <h3>No Projects Found.</h3>
      ) : (
        projects.map((project) => (
          <div
            key={project.id}
            style={{
              background: "white",
              padding: "20px",
              borderRadius: "12px",
              marginBottom: "20px",
              boxShadow:
                "0 4px 12px rgba(0,0,0,.08)",
            }}
          >
            <h2>{project.name}</h2>

            <p>{project.description}</p>

            <div
              style={{
                marginTop: "15px",
              }}
            >
              <button
                onClick={() =>
                  setEditingProject(project)
                }
                style={{
                  marginRight: "10px",
                  padding: "10px 20px",
                  background: "#2563EB",
                  color: "white",
                  border: "none",
                  borderRadius: "8px",
                  cursor: "pointer",
                }}
              >
                Edit
              </button>

              <button
                onClick={() =>
                  handleDelete(project.id)
                }
                style={{
                  padding: "10px 20px",
                  background: "#EF4444",
                  color: "white",
                  border: "none",
                  borderRadius: "8px",
                  cursor: "pointer",
                }}
              >
                Delete
              </button>
            </div>
          </div>
        ))
      )}
    </Layout>
  );
}