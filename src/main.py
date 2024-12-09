import os
import sys
from PIL import Image
import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage

# Set up the project root path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(project_root)

from models.bayesian_network_model import RefrigeratorDiagnosticModel
from variable_elimination import VariableElimination

def display_image_gui(image_path):
    """
    Display an image in a new window using Tkinter.
    """
    img_window = tk.Toplevel()
    img_window.title("Component Failure")
    img = PhotoImage(file=image_path)
    img_label = tk.Label(img_window, image=img)
    img_label.image = img  # Keep a reference to prevent garbage collection
    img_label.pack()

def simulate_failure_gui():
    """
    Simulate a refrigerator failure and display the most probable issue in a GUI.
    """
    diagnostic_model = RefrigeratorDiagnosticModel()
    ve = VariableElimination(diagnostic_model)

    evidence = {
        "Incorrect Internal Temperature": var_temp.get(),
        "Refrigerator Doesn't Cool": var_cool.get(),
        "Refrigerator Fills with Frost": var_frost.get(),
        "Light Not Turning On": var_light.get(),
        "Refrigerator Doesn't Stop": var_stop.get(),
    }

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
            messagebox.showerror("Error", f"Error querying {query_variable}: {e}")

    # Sort the list by failure probability in descending order
    failure_probabilities.sort(key=lambda x: x[1], reverse=True)

    if failure_probabilities:
        most_probable_failure = failure_probabilities[0]
        component, probability = most_probable_failure
        messagebox.showinfo(
            "Diagnosis Result",
            f"The most probable failing component is: {component} ({probability:.2f}%)"
        )

        normalized_name = component.lower()
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
                display_image_gui(image_path)
            else:
                messagebox.showerror("Error", f"Image not found for {component}")
        else:
            messagebox.showerror("Error", f"No image mapping found for {component}")

root = tk.Tk()
root.title("Refrigerator Fault Diagnosis Helper")
root.geometry("400x300")

var_temp = tk.IntVar(value=0)
var_cool = tk.IntVar(value=0)
var_frost = tk.IntVar(value=0)
var_light = tk.IntVar(value=0)
var_stop = tk.IntVar(value=0)

tk.Checkbutton(root, text="Incorrect Internal Temperature", variable=var_temp).pack(anchor="w")
tk.Checkbutton(root, text="Refrigerator Doesn't Cool", variable=var_cool).pack(anchor="w")
tk.Checkbutton(root, text="Refrigerator Fills with Frost", variable=var_frost).pack(anchor="w")
tk.Checkbutton(root, text="Light Not Turning On", variable=var_light).pack(anchor="w")
tk.Checkbutton(root, text="Refrigerator Doesn't Stop", variable=var_stop).pack(anchor="w")

simulate_button = tk.Button(root, text="Diagnose", command=simulate_failure_gui)
simulate_button.pack(pady=20)

root.mainloop()
