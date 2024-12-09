import os
import sys
import random

# Set up the project root path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(project_root)

from fridge.refrigerator import Refrigerator
from models.bayesian_network_model import RefrigeratorDiagnosticModel
from variable_elimination import VariableElimination

def introduce_random_failure(refrigerator):
    """
    Introduce un fallo aleatorio en uno de los componentes del refrigerador.
    """
    components = [
        "door", "compressor", "cooling_system", "electrical_system", "dirt", "refrigerant", "fan"
    ]
    failed_component = random.choice(components)

    if failed_component == "door":
        refrigerator.door.deteriorate_seals(30)
    elif failed_component == "compressor":
        refrigerator.compressor.set_noise_level(100)
    elif failed_component == "cooling_system":
        refrigerator.cooling_system.set_temperature(15)
    elif failed_component == "electrical_system":
        refrigerator.electrical_system.set_voltage(150)
    elif failed_component == "dirt":
        refrigerator.dirt.accumulate_dirt(80)
    elif failed_component == "refrigerant":
        refrigerator.refrigerant.simulate_leak()
    elif failed_component == "fan":
        refrigerator.fan.set_speed(500)

    print(f"[ SIMULATION ] A failure has been introduced in the {failed_component}.")


def interview_user():
    """
    Realiza una entrevista al usuario para determinar el fallo en el refrigerador.
    """
    print("\nWelcome to the Refrigerator Fault Diagnosis Helper.")
    print("Please answer the following questions to help identify the issue.")

    questions = {
        "Incorrect Internal Temperature": "Is the internal temperature of the refrigerator incorrect?",
        "Refrigerator Doesn't Cool": "Is the refrigerator not cooling?",
        "Refrigerator Fills with Frost": "Is there frost buildup in the refrigerator?",
        "Light Not Turning On": "Is the light inside the refrigerator not turning on?",
        "Refrigerator Doesn't Stop": "Does the refrigerator keep running and not stop?",
    }

    evidence = {}
    for variable, question in questions.items():
        response = input(question + " (y/n): ").strip().lower()
        evidence[variable] = 1 if response == "y" else 0

    return evidence

def calculate_failure_probabilities(model, evidence):
    """
    Utiliza un modelo probabilístico para calcular las probabilidades de fallo de cada componente.
    """
    ve = VariableElimination(model)
    nodes = list(model.model.nodes())

    failure_probabilities = []

    for query_variable in nodes:
        if query_variable in evidence:
            continue

        try:
            result = ve.query(query_variable, evidence=evidence)
            failure_probability = result.values[1] * 100
            failure_probabilities.append((query_variable, failure_probability))
        except Exception as e:
            print(f"Error querying {query_variable}: {e}")

    return sorted(failure_probabilities, key=lambda x: x[1], reverse=True)

def simulate_refrigerator_failure():
    """
    Simula una nevera con un componente que falla y permite al usuario diagnosticar el fallo.
    """
    fridge = Refrigerator()

    introduce_random_failure(fridge)

    diagnostic_model = RefrigeratorDiagnosticModel()


    print("\n--- Starting Diagnostic ---")
    evidence = interview_user()

    print("\nEvidence provided to the model:")
    for key, value in evidence.items():
        print(f"{key}: {'Yes' if value == 1 else 'No'}")

    if fridge.dirt.get_dirt_level() > 50:
        evidence["High Dirt Level"] = 1

    failure_probabilities = calculate_failure_probabilities(diagnostic_model, evidence)

    print("\nComponents sorted by probability of failure:")
    for component, probability in failure_probabilities:
        print(f"{component}: {probability:.2f}%")

if __name__ == "__main__":
    simulate_refrigerator_failure()
