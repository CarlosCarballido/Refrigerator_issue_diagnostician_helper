import pytest
import numpy as np
from src.variable_elimination import VariableElimination
from models.bayesian_network_model import RefrigeratorDiagnosticModel

@pytest.fixture
def setup_inference():

    diagnostic_model = RefrigeratorDiagnosticModel()
    ve = VariableElimination(diagnostic_model)
    return ve

def test_query_inference_valid_variable(setup_inference):

    ve = setup_inference
    evidence = {
        "Door Doesn't Lock": 1,
        "Dirt": 1,
        "Incorrect Fan Speed": 1
    }

    variable_to_query = "Compressor Failure"
    
    result = ve.query(variable_to_query, evidence)
    
    assert hasattr(result, "values"), "Result object does not have 'values' attribute."
    assert isinstance(result.values, np.ndarray), "Result 'values' is not a numpy array."
    
    assert len(result.values) > 1, "Result values are incomplete."
    assert np.all(np.isreal(result.values)), "Result values are not numeric."

    assert result.values[1] > 0, "Inference did not return a valid probability."

def test_query_inference_invalid_variable(setup_inference):

    ve = setup_inference
    evidence = {
        "Door Doesn't Lock": 1
    }
    with pytest.raises(KeyError):
        ve.query("Nonexistent Variable", evidence)
