def predict_progression(age, bp, sugar, disease):

    score = 0

    if age > 50:
        score += 2
    if bp > 140:
        score += 2
    if sugar > 180:
        score += 2

    if disease in ["Heart Disease", "Kidney Disease"]:
        score += 3

    if score <= 2:
        return "Stable"
    elif score <= 5:
        return "Moderate Progression"
    elif score <= 7:
        return "High Progression"
    else:
        return "Critical Progression"
python