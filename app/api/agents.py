from fastapi import APIRouter
from app.database.database import SessionLocal
from app.models.agent import Agent


router = APIRouter(
    prefix="/agents",
    tags=["Agents"]
)


@router.post("/")
def create_agent(
    name: str,
    description: str,
    role: str
):
    db = SessionLocal()

    # التحقق هل الـ Agent موجود مسبقًا
    existing_agent = db.query(Agent).filter(
        Agent.name == name,
        Agent.role == role
    ).first()

    if existing_agent:
        db.close()

        return {
            "message": "Agent already exists",
            "agent": existing_agent
        }

    # إنشاء Agent جديد
    agent = Agent(
        name=name,
        description=description,
        role=role
    )

    db.add(agent)
    db.commit()
    db.refresh(agent)
    db.close()

    return agent


@router.get("/")
def get_agents():
    db = SessionLocal()

    agents = db.query(Agent).all()

    db.close()

    return agents


@router.post("/seed")
def seed_capabilities():
    db = SessionLocal()

    agents = db.query(Agent).all()

    capabilities_map = {
        "researcher": [
            "Literature Review",
            "PubMed Search",
            "Evidence Analysis",
            "Risk Assessment"
        ],
        "laboratory_specialist": [
            "Sample Validation",
            "Test Recommendation",
            "Biomarker Interpretation",
            "Quality Control"
        ],
        "healthcare_institution": [
            "Clinical Decision Support",
            "Hospital Guidelines",
            "Case Prioritization",
            "Patient Safety"
        ]
    }

    updated = 0

    for agent in agents:
        if not agent.capabilities:
            agent.capabilities = ", ".join(
                capabilities_map.get(agent.role, [])
            )
            updated += 1

    db.commit()
    db.close()

    return {
        "message": f"{updated} agents updated successfully"
    }


@router.delete("/{agent_id}")
def delete_agent(agent_id: int):
    db = SessionLocal()

    agent = db.query(Agent).filter(
        Agent.id == agent_id
    ).first()

    if agent is None:
        db.close()

        return {
            "message": "Agent not found"
        }

    db.delete(agent)
    db.commit()
    db.close()

    return {
        "message": "Agent deleted successfully"
    }