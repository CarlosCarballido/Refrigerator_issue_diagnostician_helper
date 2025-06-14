import os
import sys
from PIL import Image
from time import sleep

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
        "Light Not Turning On": "Is the light inside the refrigerator not turning on?",
        "Refrigerator Doesn't Stop": "Does the refrigerator keep running and not stop?",
    }

    evidence = {}
    for variable, question in questions.items():
        response = input(question + " (y/n): ").strip().lower()
        evidence[variable] = 1 if response == "y" else 0

    return evidence

def display_image(component_name):
    """
    Muestra la imagen del componente fallado.
    """
    # Normalizar el nombre del componente
    normalized_name = component_name.lower()
    normalized_name = (
        normalized_name.replace("failure", "")
        .replace("incorrect", "")
        .replace("speed", "")
        .replace("pressure", "")
        .replace("doesn't lock", "")
        .strip()
    )

    image_dir = os.path.join(project_root, 'data', 'Fridge-Images')
    image_mapping = {
        "compressor": "compressor.png",
        "cooling system": "coolant-system.png",
        "door": "door_open.png",
        "electrical system": "electrical-system.png",
        "fan": "fridge-fan.png",
        "refrigerant": "refrigerant.png",
        "refrigerator": "refrigerator.png",
        "coolant": "coolant-system.png",
        "voltage": "voltage.png",
        "internal temperature": "temperature.png",
        "dirt": "dirt.png",
        "fan speed": "fan-speed.png",
    }

    image_file = image_mapping.get(normalized_name)
    if image_file:
        image_path = os.path.join(image_dir, image_file)
        if os.path.exists(image_path):
            print(f"Displaying image for {normalized_name.capitalize()}")
            try:
                img = Image.open(image_path)
                img.show()
            except Exception as e:
                print(f"Error displaying image: {e}")
        else:
            print(f"Image file not found at path: {image_path}")
    else:
        print(f"No image mapping found for '{normalized_name}'.")

def simulate_refrigerator_failure():
    print("Simulating Refrigerator Fault...")

    diagnostic_model = RefrigeratorDiagnosticModel()
    ve = VariableElimination(diagnostic_model)

    evidence = interview_user()

    print("\nEvidence provided to the model:")
    for key, value in evidence.items():
        print(f"{key}: {'Yes' if value == 1 else 'No'}")

    nodes = list(diagnostic_model.model.nodes())

    failure_probabilities = []

    excluded_states = [
        "Refrigerator Doesn't Stop",
        "Light Not Turning On",
        "Refrigerator Doesn't Cool",
        "Refrigerator Fills with Frost",
        "Incorrect Internal Temperature"
    ]

    for query_variable in nodes:
        if query_variable in excluded_states:  
            continue

        test_evidence = {k: v for k, v in evidence.items() if k != query_variable}  
        try:
            result = ve.query(query_variable, evidence=test_evidence)

            failure_probability = result.values[1] * 100
            failure_probabilities.append((query_variable, failure_probability))
        except Exception as e:
            print(f"Error querying {query_variable} with minimal evidence: {e}")

    failure_probabilities.sort(key=lambda x: x[1], reverse=True)

    print("\nComponents sorted by probability of failure:")
    for component, probability in failure_probabilities:
        print(f"{component}: {probability:.2f}%")

    if failure_probabilities:
        most_probable_failure = failure_probabilities[0]
        print(f"\nThe most probable failure is: {most_probable_failure[0]} ({most_probable_failure[1]:.2f}%)")
        sleep(1)
        print("Displaying image of the most probable failure...")
        sleep(3)
        display_image(most_probable_failure[0])

if __name__ == "__main__":
    simulate_refrigerator_failure()
