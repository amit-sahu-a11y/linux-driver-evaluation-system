
import re

def run_static_checks(file_path):
    scores = {
        "security": {"buffer_safety": 0.9, "race_conditions": 0.8, "input_validation": 0.7},
        "code_quality": {"style_compliance": 0.85, "documentation": 0.6, "maintainability": 0.75}
    }
   
    return scores
