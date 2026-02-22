def detect_disease(text):

    text = text.lower()

    if "heart attack" in text or "myocardial" in text or "st elevation" in text:
        return "Heart Disease"

    if "diabetes" in text or "high glucose" in text:
        return "Diabetes"

    if "creatinine" in text or "renal" in text or "kidney" in text:
        return "Kidney Disease"

    if "infection" in text or "pus cells" in text or "bacteria" in text:
        return "Infection"

    if "hypertension" in text or "high blood pressure" in text:
        return "Hypertension"

    return None
