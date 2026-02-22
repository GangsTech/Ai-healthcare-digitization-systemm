from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
)
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
import os


def generate_pdf(report, patient_username):

    
    if not os.path.exists("reports"):
        os.makedirs("reports")

    filename = f"reports/{patient_username}_report.pdf"

    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()
    elements = []

    
    title = Paragraph(
        "<h1>AI Healthcare Digitization System</h1>"
        "<h3>Automated Medical Report</h3>",
        styles["Title"]
    )
    elements.append(title)
    elements.append(Spacer(1, 20))

    
    patient_photo = report.get("patient_photo")

    if patient_photo and os.path.exists(patient_photo):
        elements.append(Paragraph("<b>Patient Photograph</b>", styles["Heading2"]))
        elements.append(Image(patient_photo, width=120, height=120))
        elements.append(Spacer(1, 15))

    
    elements.append(Paragraph("<b>Patient Information</b>", styles["Heading2"]))

    patient_table = Table([
        ["Patient Name", report.get("patient_name", "")],
        ["Age", report.get("age", "")],
        ["Weight (kg)", report.get("weight", "")],
        ["Height (cm)", report.get("height", "")],
    ])

    patient_table.setStyle(TableStyle([
        ("GRID", (0,0), (-1,-1), 1, colors.grey),
        ("BACKGROUND", (0,0), (0,-1), colors.whitesmoke)
    ]))

    elements.append(patient_table)
    elements.append(Spacer(1, 15))

    
    elements.append(Paragraph("<b>Clinical Measurements</b>", styles["Heading2"]))

    clinical_table = Table([
        ["Blood Pressure", report.get("bp", "")],
        ["Blood Sugar", report.get("sugar", "")],
        ["Disease / Condition", report.get("disease", "Not Detected")],
    ])

    clinical_table.setStyle(TableStyle([
        ("GRID", (0,0), (-1,-1), 1, colors.grey),
        ("BACKGROUND", (0,0), (0,-1), colors.whitesmoke)
    ]))

    elements.append(clinical_table)
    elements.append(Spacer(1, 20))

    
    elements.append(Paragraph("<b>Doctor Information</b>", styles["Heading2"]))

    doctor_table = Table([
        ["Doctor Name", report.get("doctor", "")],
        ["Date", report.get("date", "")],
    ])

    doctor_table.setStyle(TableStyle([
        ("GRID", (0,0), (-1,-1), 1, colors.grey),
        ("BACKGROUND", (0,0), (0,-1), colors.whitesmoke)
    ]))

    elements.append(doctor_table)
    elements.append(Spacer(1, 20))

    
    elements.append(Paragraph("<b>Doctor Signature</b>", styles["Heading2"]))

    signature_path = report.get("signature")

    if signature_path and os.path.exists(signature_path):
        elements.append(Image(signature_path, width=120, height=50))
    else:
        elements.append(Paragraph("Not Provided", styles["BodyText"]))

    elements.append(Spacer(1, 30))

    
    disclaimer = """
This report is generated using AI-assisted clinical decision support.
Final diagnosis and treatment decisions must be made by a licensed
medical professional.
"""
    elements.append(Paragraph(disclaimer, styles["Italic"]))

    
    doc.build(elements)

    return filename
