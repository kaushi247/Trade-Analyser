def calculate_health_score(win_rate, avg_holding, profit_factor):

    # Discipline
    discipline = min(int(win_rate), 100)

    # Risk Management
    if profit_factor == "Infinity":
        risk_management = 90
    elif profit_factor >= 2:
        risk_management = 85
    elif profit_factor >= 1:
        risk_management = 70
    else:
        risk_management = 40

    # Patience
    if avg_holding >= 5:
        patience = 85
    elif avg_holding >= 2:
        patience = 70
    else:
        patience = 40

    # Consistency
    if win_rate >= 70:
        consistency = 90
    elif win_rate >= 50:
        consistency = 75
    else:
        consistency = 50

    overall = int(
        (
            discipline +
            risk_management +
            patience +
            consistency
        ) / 4
    )

    return {
        "discipline": discipline,
        "risk_management": risk_management,
        "patience": patience,
        "consistency": consistency,
        "overall": overall
    }