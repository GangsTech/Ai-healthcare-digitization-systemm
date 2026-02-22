def detect_test_type(text):

    text = text.lower()

    if "urine" in text or "urine culture" in text:
        return "Urine Test"

    elif "blood" in text or "cbc" in text or "haemoglobin" in text:
        return "Blood Test"

    elif "glucose" in text or "sugar" in text:
        return "Blood Sugar Test"

    elif "lipid" in text or "cholesterol" in text:
        return "Lipid Profile"

    elif "thyroid" in text or "tsh" in text:
        return "Thyroid Test"

    elif "ecg" in text:
        return "ECG"

    elif "x-ray" in text or "radiology" in text:
        return "X-Ray"

    else:
        return "Unknown Test"
