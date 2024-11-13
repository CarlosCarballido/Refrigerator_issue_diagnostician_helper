import os
import sys

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
    import time
    diagnostic_model = RefrigeratorDiagnosticModel()
    print("Model initialized and validated.")

    ve = VariableElimination(diagnostic_model)

    print("Inference Result:")
    start = time.time()
    result = ve.query('Incorrect Internal Temperature', {'Door Doesn\'t Lock': 1,'Dirt': 1, 'Incorrect Fan Speed': 1, 'Incorrect Coolant Pressure': 1, 'Compressor Failure': 1})
    finish = time.time()
    print(result)
    print(f"Time taken: {finish - start} seconds")
