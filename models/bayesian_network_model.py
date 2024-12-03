from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

class RefrigeratorDiagnosticModel:
    def __init__(self):
        self.model = BayesianNetwork([
            ('Incorrect Internal Temperature', 'Refrigerator Doesn\'t Cool'),
            ('Incorrect Internal Temperature', 'Refrigerator Fills with Frost'),
            ('Incorrect Voltage', 'Incorrect Internal Temperature'),
            ('Incorrect Voltage', 'Light Not Turning On'),
            ('Incorrect Voltage', 'Refrigerator Doesn\'t Stop'),
            ('Door Doesn\'t Lock', 'Incorrect Internal Temperature'),
            ('Dirt', 'Incorrect Internal Temperature'),
            ('Incorrect Fan Speed', 'Incorrect Internal Temperature'),
            ('Incorrect Coolant Pressure', 'Incorrect Internal Temperature'),
            ('Incorrect Coolant Pressure', 'Incorrect Voltage'),
            ('Compressor Failure', 'Incorrect Internal Temperature'),
            ('Compressor Failure', 'Refrigerator Doesn\'t Stop'),
        ])
        self._add_cpds()
        if not self.model.check_model():
            raise ValueError("The model has errors and is not valid.")
        self.inference = VariableElimination(self.model)

    def _add_cpds(self):
        cpd_refrigerator_doesnt_cool = TabularCPD(
            variable='Refrigerator Doesn\'t Cool', variable_card=2,
            values=[[0.53, 0.47], [0.47, 0.53]],
            evidence=['Incorrect Internal Temperature'],
            evidence_card=[2]
        )

        cpd_refrigerator_fills_with_frost = TabularCPD(
            variable='Refrigerator Fills with Frost', variable_card=2,
            values=[[0.91, 0.09], [0.09, 0.91]],
            evidence=['Incorrect Internal Temperature'],
            evidence_card=[2]
        )

        cpd_light_not_turning_on = TabularCPD(
            variable='Light Not Turning On', variable_card=2,
            values=[[0.7, 0.4], [0.3, 0.6]],
            evidence=['Incorrect Voltage'],
            evidence_card=[2]
        )

        cpd_refrigerator_doesnt_stop = TabularCPD(
            variable='Refrigerator Doesn\'t Stop', variable_card=2,
            values=[[0.75, 0.6, 0.2, 0.1], [0.25, 0.4, 0.8, 0.9]],
            evidence=['Incorrect Voltage', 'Compressor Failure'],
            evidence_card=[2, 2]
        )

        cpd_incorrect_internal_temperature = TabularCPD(
            variable='Incorrect Internal Temperature', variable_card=2,
            values=[
                [0.03, 0.39, 0.55, 0.95, 0.71, 0.48, 0.37, 0.13, 0.09, 0.25, 0.07, 0.92, 0.43, 0.84, 0.51, 0.36, 0.32, 0.22, 0.47, 0.19, 0.76, 0.98, 0.03, 0.12, 0.34, 0.84, 0.62, 0.32, 0.31, 0.62, 0.98, 0.53, 0.39, 0.86, 0.82, 0.38, 0.78, 0.34, 0.95, 0.98, 0.81, 0.22, 0.17, 0.7, 0.64, 0.2, 0.24, 0.45, 0.99, 0.24, 0.03, 0.13, 0.06, 0.56, 0.69, 0.53, 0.98, 0.99, 0.95, 0.36, 0.78, 0.45, 0.5, 0.1],
                [0.97, 0.61, 0.45, 0.05, 0.29, 0.52, 0.63, 0.87, 0.91, 0.75, 0.93, 0.08, 0.57, 0.16, 0.49, 0.64, 
                 0.68, 0.78, 0.53, 0.81, 0.24, 0.02, 0.97, 0.88, 0.66, 0.16, 0.38, 0.68, 0.69, 0.38, 0.02, 0.47, 
                 0.61, 0.14, 0.18, 0.62, 0.22, 0.66, 0.05, 0.02, 0.19, 0.78, 0.83, 0.3, 0.36, 0.8, 0.76, 0.55, 
                 0.01, 0.76, 0.97, 0.87, 0.94, 0.44, 0.31, 0.47, 0.02, 0.01, 0.05, 0.64, 0.22, 0.55, 0.5, 0.9]
            ],
            evidence=['Door Doesn\'t Lock', 'Dirt', 'Incorrect Fan Speed', 'Incorrect Coolant Pressure', 'Compressor Failure', 'Incorrect Voltage'],
            evidence_card=[2, 2, 2, 2, 2, 2]
        )

        cpd_incorrect_voltage = TabularCPD(
            variable='Incorrect Voltage', variable_card=2,
            values=[[0.7, 0.2], [0.3, 0.8]],
            evidence=['Incorrect Coolant Pressure'],
            evidence_card=[2]
        )

        cpd_door_doesnt_lock = TabularCPD(variable='Door Doesn\'t Lock', variable_card=2, values=[[0.3], [0.7]])
        cpd_dirt = TabularCPD(variable='Dirt', variable_card=2, values=[[0.4], [0.6]])
        cpd_incorrect_fan_speed = TabularCPD(variable='Incorrect Fan Speed', variable_card=2, values=[[0.25], [0.75]])
        cpd_incorrect_coolant_pressure = TabularCPD(variable='Incorrect Coolant Pressure', variable_card=2, values=[[0.2], [0.8]])
        cpd_compressor_failure = TabularCPD(variable='Compressor Failure', variable_card=2, values=[[0.25], [0.75]])

        self.model.add_cpds(
            cpd_refrigerator_doesnt_cool,
            cpd_refrigerator_fills_with_frost,
            cpd_light_not_turning_on,
            cpd_refrigerator_doesnt_stop,
            cpd_incorrect_internal_temperature,
            cpd_incorrect_voltage,
            cpd_door_doesnt_lock,
            cpd_dirt,
            cpd_incorrect_fan_speed,
            cpd_incorrect_coolant_pressure,
            cpd_compressor_failure
        )
        
    def infer_failure_probability(self, variable, evidence):
        return self.inference.query(variables=[variable], evidence=evidence)