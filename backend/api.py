
from fastapi import FastAPI
from pydantic import BaseModel
from backend.risk_engine import calculate_risk_score

app = FastAPI(
    title="DeployGuard AI",
    description="Software Deployment Risk Assessment API",
    version="1.0.0"
)


class DeploymentRequest(BaseModel):
    changed_files: list[str]
    critical_service: bool
    database_changed: bool


@app.get("/")
def home():
    return {
        "message": "Welcome to DeployGuard AI",
        "status": "API is running"
    }


@app.post("/assess")
def assess_deployment(request: DeploymentRequest):

    report = calculate_risk_score(
        request.changed_files,
        request.critical_service,
        request.database_changed
    )

    return report
