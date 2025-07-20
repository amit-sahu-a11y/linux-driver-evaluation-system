
from evaluation.compile_and_score import compile_code
from evaluation.static_analysis import run_static_checks
from evaluation.metrics import evaluation_metrics

def evaluate(file_path):
    result = compile_code(file_path)
    evaluation_metrics["compilation"]["success_rate"] = 1.0 if result["success"] else 0.0
    evaluation_metrics["compilation"]["warnings_count"] = result["warnings"]
    evaluation_metrics["compilation"]["errors_count"] = result["errors"]

    static_scores = run_static_checks(file_path)
    for cat, values in static_scores.items():
        for key, val in values.items():
            evaluation_metrics[cat][key] = val

    # Compute overall_score (example weighting)
    overall = (
        evaluation_metrics["compilation"]["success_rate"] * 40 +
        evaluation_metrics["security"]["buffer_safety"] * 25 +
        evaluation_metrics["code_quality"]["style_compliance"] * 20 +
        5  # basic performance placeholder
    )
    evaluation_metrics["overall_score"] = round(overall, 2)
    return evaluation_metrics

if __name__ == "__main__":
    import sys, json
    file_path = sys.argv[1] if len(sys.argv) > 1 else "code_samples/sample_driver.c"
    results = evaluate(file_path)
    print(json.dumps(results, indent=4))
