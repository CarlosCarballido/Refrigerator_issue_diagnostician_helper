import os
import sys
import importlib.util

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(project_root)

from models.bayesian_network_model import RefrigeratorDiagnosticModel

class VariableElimination:
    def __init__(self, model: RefrigeratorDiagnosticModel):
        self.model = model

    def query(self, variable: str, evidence: dict):
        result = self.model.infer_failure_probability(variable, evidence)
        return result
    
if __name__ == "__main__":
    diagnostic_model = RefrigeratorDiagnosticModel()
    print("Model initialized and validated.")

    ve = VariableElimination(diagnostic_model)

    print("Inference Result:")
    result = ve.query('Refrigerator Doesn\'t Cool', {'Incorrect Internal Temperature': 1})
    print(result)
