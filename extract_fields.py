import re

def extract_fields(text):

    text = text.lower()
    data = {"age": None, "bp": None, "sugar": None}

    lines = text.split("\n")

    for line in lines:

        # ---------- AGE ----------
        age_match = re.search(
            r'\bage\s*[:=\-]?\s*(\d{1,3})\b',
            line
        )
        if age_match and data["age"] is None:
            data["age"] = int(age_match.group(1))

        # ---------- BLOOD PRESSURE ----------
        bp_match = re.search(
            r'\b(bp|blood pressure)\s*[:=\-]?\s*(\d{2,3})\b',
            line
        )
        if bp_match and data["bp"] is None:
            data["bp"] = int(bp_match.group(2))

        # ---------- BLOOD SUGAR ----------
        sugar_match = re.search(
            r'\b(sugar|glucose|blood sugar)\s*[:=\-]?\s*(\d{2,3})\b',
            line
        )
        if sugar_match and data["sugar"] is None:
            data["sugar"] = int(sugar_match.group(2))

    return data
