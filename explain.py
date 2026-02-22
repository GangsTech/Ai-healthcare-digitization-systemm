import shap

def explain_prediction(model, X):
    explainer = shap.Explainer(model, X)
    return explainer
