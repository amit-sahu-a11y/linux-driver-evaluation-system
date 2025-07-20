
import subprocess

def compile_code(path_to_c_file):
    try:
        result = subprocess.run(['gcc', '-Wall', path_to_c_file],
                                capture_output=True, text=True, timeout=10)
        errors = result.stderr.count("error:")
        warnings = result.stderr.count("warning:")
        success = result.returncode == 0
        return {"success": success, "warnings": warnings, "errors": errors}
    except Exception as e:
        return {"success": False, "warnings": 0, "errors": 1, "exception": str(e)}
