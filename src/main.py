import os
import sys
import random

# Set up the project root path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(project_root)

from models.bayesian_network_model import RefrigeratorDiagnosticModel
from variable_elimination import VariableElimination

def interview_user():
    """
    Realiza una entrevista al usuario para determinar el fallo en la nevera.
    """
    print("\nWelcome to the Refrigerator Fault Diagnosis Helper.")
    print("Please answer the following questions to help identify the issue.")

    questions = {
        "Incorrect Internal Temperature": "Is the internal temperature of the refrigerator incorrect?",
        "Refrigerator Doesn't Cool": "Is the refrigerator not cooling?",
        "Refrigerator Fills with Frost": "Is there frost buildup in the refrigerator?",
        "Incorrect Voltage": "Is there an incorrect voltage supply?",
        "Light Not Turning On": "Is the light inside the refrigerator not turning on?",
        "Refrigerator Doesn't Stop": "Does the refrigerator keep running and not stop?",
        "Door Doesn't Lock": "Does the refrigerator door fail to lock properly?",
        "Dirt": "Is there dirt or dust buildup affecting the refrigerator's performance?",
        "Incorrect Fan Speed": "Is the fan speed incorrect?",
        "Incorrect Coolant Pressure": "Is there incorrect coolant pressure?",
        "Compressor Failure": "Is the compressor experiencing any failure?"
    }

    evidence = {}
    for variable, question in questions.items():
        response = input(question + " (y/n): ").strip().lower()
        evidence[variable] = 1 if response == "y" else 0

    return evidence

def simulate_refrigerator_failure():
    """
    Simula una nevera con un componente que falla y utiliza la red bayesiana
    para calcular las probabilidades de error.
    """
    print("Simulating Refrigerator Fault...")

    # Crear modelo de diagnóstico
    diagnostic_model = RefrigeratorDiagnosticModel()
    ve = VariableElimination(diagnostic_model)

    # Realizar entrevista al usuario para determinar evidencia
    evidence = interview_user()

    print("\nEvidence provided to the model:")
    for key, value in evidence.items():
        print(f"{key}: {'Yes' if value == 1 else 'No'}")

    # Realizar inferencias sobre todos los nodos del modelo
    print("\nInference Results:")
    for query_variable in diagnostic_model.model.nodes():  # Acceder al modelo interno
        if query_variable not in evidence or evidence[query_variable] == 0:
            result = ve.query([query_variable], evidence=evidence)
            print(f"{query_variable}: {result}")

if __name__ == "__main__":
    simulate_refrigerator_failure()
