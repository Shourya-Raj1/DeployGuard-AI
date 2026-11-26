
def calculate_risk_score(changed_files, critical_service, database_changed):

    risk_score = len(changed_files) * 10
    reasons = []
    recommendations = []

    if changed_files:
        reasons.append(f"{len(changed_files)} files modified")
        recommendations.append("Review all modified files.")

    if critical_service:
        risk_score += 30
        reasons.append("Critical service affected (+30 points)")
        recommendations.append("Perform critical service testing.")

    if database_changed:
        risk_score += 20
        reasons.append("Database changes detected (+20 points)")
        recommendations.append("Run database migration tests.")

    risk_score = min(risk_score, 100)

    if risk_score <= 30:
        risk_level = "LOW"
    elif risk_score <= 60:
        risk_level = "MEDIUM"
    else:
        risk_level = "HIGH"

    return {
        "risk_score": risk_score,
        "risk_level": risk_level,
        "reasons": reasons,
        "recommendations": recommendations
    }
