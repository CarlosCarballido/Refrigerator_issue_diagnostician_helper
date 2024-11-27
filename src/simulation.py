import os
import sys
import random

# Set up the project root path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(project_root)

from fridge.refrigerator import Refrigerator

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
        refrigerator.compressor.set_noise_level(100)  # Nivel de ruido inaceptable
    elif failed_component == "cooling_system":
        refrigerator.cooling_system.set_temperature(15)  # Temperatura fuera del rango óptimo
    elif failed_component == "electrical_system":
        refrigerator.electrical_system.set_voltage(150)  # Voltaje fuera del rango aceptable
    elif failed_component == "dirt":
        refrigerator.dirt.accumulate_dirt(80)  # Nivel de suciedad inaceptable
    elif failed_component == "refrigerant":
        refrigerator.refrigerant.simulate_leak()  # Simula una fuga
    elif failed_component == "fan":
        refrigerator.fan.set_speed(500)  # Velocidad del ventilador fuera del rango óptimo

    print(f"A failure has been introduced in the {failed_component}.")


def interview_user():
    """
    Realiza una entrevista al usuario para determinar el fallo en el refrigerador.
    """
    print("\nWelcome to the Refrigerator Fault Diagnosis Helper.")
    print("Please answer the following questions to help identify the issue.")

    questions = {
        "Is the door closed properly?": lambda fridge: fridge.is_door_closed(),
        "Is the compressor making unusual noise?": lambda fridge: not fridge.is_compressor_working(),
        "Is the internal temperature correct?": lambda fridge: fridge.is_temperature_adequate(),
        "Is the voltage supply normal?": lambda fridge: fridge.is_voltage_adequate(),
        "Is the refrigerator clean (no dirt buildup)?": lambda fridge: fridge.is_clean(),
        "Is the refrigerant pressure adequate?": lambda fridge: fridge.is_refrigerant_pressure_adequate(),
        "Is the fan running at an appropriate speed?": lambda fridge: fridge.is_fan_speed_adequate(),
    }

    for question, check_function in questions.items():
        response = input(f"{question} (y/n): ").strip().lower()
        if response == "n":
            print("This might be where the issue lies. Investigating further...")
            return check_function

    print("No issues reported based on user input. Consider performing a deeper diagnostic.")
    return None


def simulate_refrigerator_failure():
    """
    Simula una nevera con un componente que falla y permite al usuario diagnosticar el fallo.
    """
    fridge = Refrigerator()

    # Introduce un fallo aleatorio
    introduce_random_failure(fridge)

    # Realiza la entrevista
    print("\n--- Starting Diagnostic ---")
    check_function = interview_user()

    if check_function and not check_function(fridge):
        print("Confirmed: The component identified by the user has a failure.")
    else:
        print("Unable to confirm the failure based on user input. Further diagnostics needed.")


if __name__ == "__main__":
    simulate_refrigerator_failure()
