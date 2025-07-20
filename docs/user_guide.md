# 🧑‍💻 User Guide: Linux Device Driver Evaluation System

This guide explains how to install dependencies, run the evaluation pipeline, and interpret the results for AI-generated Linux device driver code.

---

## 📁 Project Structure Overview

```bash
driver-eval-system/
├── code_samples/            # Put your input C driver files here
├── evaluation/              # Evaluation logic: compilation, analysis, scoring
├── reports/                 # Final output report (JSON)
├── docs/                    # Documentation files
├── run_evaluation.py        # Main entry script
└── requirements.txt         # Dependency list
