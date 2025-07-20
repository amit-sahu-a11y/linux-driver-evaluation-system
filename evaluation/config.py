# Config with weights and thresholds
# evaluation/config.py

# Weightage for each category in overall score
CATEGORY_WEIGHTS = {
    "compilation": 0.40,      # 40%
    "security": 0.25,         # 25%
    "code_quality": 0.20,     # 20%
    "performance": 0.10,      # 10%
    "advanced_features": 0.05 # 5% (optional/bonus)
}

# Thresholds (you can adjust these based on needs)
WARNING_THRESHOLD = 5         # Number of warnings allowed before penalty
ERROR_THRESHOLD = 0           # Compilation errors not allowed

# Style compliance scoring parameters
STYLE_MAX_SCORE = 1.0
STYLE_PENALTY_PER_ISSUE = 0.05  # Deduct per style issue found

# Documentation score
MIN_DOC_LINES = 3
DOC_SCORE_FULL = 1.0
DOC_SCORE_LOW = 0.5
DOC_SCORE_NONE = 0.0

# Maintainability
MAX_FUNCTION_LENGTH = 50     # Lines per function (for maintainability)
MAINTAINABILITY_PENALTY = 0.1  # Deduction if too long

# Performance checks (mocked or expandable later)
PERFORMANCE_DEFAULT_SCORE = 0.5  # Used if no runtime data

# Enable/disable optional checks
ENABLE_CLANG_TIDY = False
ENABLE_RUNTIME_TESTS = False

# Overall scoring scale (0 to 100)
SCORE_SCALE = 100
