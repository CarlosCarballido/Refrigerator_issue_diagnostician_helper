import pytest
from src.variable_elimination import VariableElimination
from models.bayesian_network_model import RefrigeratorDiagnosticModel

@pytest.fixture
def setup_inference():
    """
    Fixture para inicializar el modelo y el objeto VariableElimination.
    """
    diagnostic_model = RefrigeratorDiagnosticModel()
    ve = VariableElimination(diagnostic_model)
    return ve

def test_query_inference_valid_variable(setup_inference):
    """
    Prueba que un query válido devuelve valores esperados.
    """
    ve = setup_inference
    evidence = {
        "Door Doesn't Lock": 1,
        "Dirt": 1,
        "Incorrect Fan Speed": 1
    }
    result = ve.query("Compressor Failure", evidence)
    assert 1 in result.values, "Inference did not return expected values."

def test_query_inference_invalid_variable(setup_inference):
    """
    Prueba que un query con una variable inexistente lanza KeyError.
    """
    ve = setup_inference
    evidence = {
        "Door Doesn't Lock": 1
    }
    with pytest.raises(KeyError):
        ve.query("Nonexistent Variable", evidence)
