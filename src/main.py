import os
import sys

# Set up the project root path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(project_root)

from models.bayesian_network_model import RefrigeratorDiagnosticModel
from variable_elimination import VariableElimination

def interview_user():
    print("Welcome to the Refrigerator Fault Diagnosis Helper.")
    print("Please answer the following questions to help us identify the problem.")

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

    responses = {}
    for variable, question in questions.items():
        response = input(question + " (y/n): ").strip().lower()
        responses[variable] = 1 if response == "y" else 0

    return responses

if __name__ == "__main__":
    user_responses = interview_user()
    diagnostic_model = RefrigeratorDiagnosticModel()
    ve = VariableElimination(diagnostic_model)

    print("Inference Result:")
    # Query a variable that is NOT in evidence
    # Here, we use 'Refrigerator Doesn't Cool' as an example query variable
    query_variable = "Refrigerator Doesn't Cool"
    evidence = {key: value for key, value in user_responses.items() if key != query_variable}
    
    result = ve.query(query_variable, evidence)
    print(result)

    print("Thank you for using the Refrigerator Fault Diagnosis Helper.")
