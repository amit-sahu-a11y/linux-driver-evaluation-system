# utils/clang_tools.py

import subprocess
import os

def run_clang_tidy(file_path, checks="*", export_fixes=False):
    """
    Runs clang-tidy on the provided C file.

    Args:
        file_path (str): Path to the .c file to analyze.
        checks (str): Which checks to run (default: all "*").
        export_fixes (bool): If True, exports suggested fixes to a YAML file.

    Returns:
        dict: {
            "success": True/False,
            "issues": number of warnings,
            "output": raw output from clang-tidy
        }
    """
    if not os.path.isfile(file_path):
        return {"success": False, "issues": 0, "output": "File not found."}

    command = [
        "clang-tidy",
        file_path,
        "--", "-std=c11"
    ]

    if checks:
        command.insert(1, f"-checks={checks}")

    if export_fixes:
        command.insert(1, f"-export-fixes=fixes.yaml")

    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=20)
        warnings = result.stdout.count("warning:")
        return {
            "success": True,
            "issues": warnings,
            "output": result.stdout
        }
    except Exception as e:
        return {"success": False, "issues": 0, "output": str(e)}
