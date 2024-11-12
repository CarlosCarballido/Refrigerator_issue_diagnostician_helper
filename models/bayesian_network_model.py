from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = BayesianNetwork([
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

# CPDs
cpd_refrigerator_doesnt_cool = TabularCPD(
    variable='Refrigerator Doesn\'t Cool', variable_card=2,
    values=[
        [0.9, 0.85, 0.8, 0.75, 0.8, 0.75, 0.7, 0.6, 0.6, 0.5, 0.4, 0.3, 0.5, 0.4, 0.2, 0.1],
        [0.1, 0.15, 0.2, 0.25, 0.2, 0.25, 0.3, 0.4, 0.4, 0.5, 0.6, 0.7, 0.5, 0.6, 0.8, 0.9]
    ],
    evidence=['Incorrect Internal Temperature'],
    evidence_card=[2]
)

cpd_refrigerator_fills_with_frost = TabularCPD(
    variable='Refrigerator Fills with Frost', variable_card=2,
    values=[
        [0.9, 0.85, 0.8, 0.75, 0.8, 0.75, 0.7, 0.6, 0.6, 0.5, 0.4, 0.3, 0.5, 0.4, 0.3, 0.2],
        [0.1, 0.15, 0.2, 0.25, 0.2, 0.25, 0.3, 0.4, 0.4, 0.5, 0.6, 0.7, 0.5, 0.6, 0.7, 0.8]
    ],
    evidence=['Incorrect Internal Temperature'],
    evidence_card=[2]
)

cpd_light_not_turning_on = TabularCPD(
    variable='Light Not Turning On', variable_card=2,
    values=[
        [0.7, 0.6, 0.4, 0.1],
        [0.3, 0.4, 0.6, 0.9]
    ],
    evidence=['Incorrect Voltage'],
    evidence_card=[2]
)

cpd_refrigerator_doesnt_stop = TabularCPD(
    variable='Refrigerator Doesn\'t Stop', variable_card=2,
    values=[
        [0.75, 0.6, 0.55, 0.5, 0.65, 0.6, 0.2, 0.1],
        [0.25, 0.4, 0.45, 0.5, 0.35, 0.4, 0.8, 0.9]
    ],
    evidence=['Incorrect Voltage', 'Compressor Failure'],
    evidence_card=[2, 2, 2]
)

cpd_incorrect_internal_temperature = TabularCPD(
    variable='Incorrect Internal Temperature', variable_card=2,
    values=[
        [0.95, 0.9, 0.85, 0.8, 0.85, 0.8, 0.75, 0.7, 0.8, 0.75, 0.7, 0.5, 0.7, 0.6, 0.5, 0.3, 0.8, 0.7, 0.6, 0.4, 0.6, 0.5, 0.4, 0.2, 0.5, 0.4, 0.3, 0.1, 0.3, 0.2, 0.1, 0.05],
        [0.05, 0.1, 0.15, 0.2, 0.15, 0.2, 0.25, 0.3, 0.2, 0.25, 0.3, 0.5, 0.3, 0.4, 0.5, 0.7, 0.2, 0.3, 0.4, 0.6, 0.4, 0.5, 0.6, 0.8, 0.5, 0.6, 0.7, 0.9, 0.7, 0.8, 0.9, 0.95]
    ],
    evidence=['Door Doesn\'t Lock', 'Dirt', 'Incorrect Fan Speed', 'Incorrect Coolant Pressure', 'Compressor Failure'],
    evidence_card=[2, 2, 2, 2, 2]
)

cpd_incorrect_voltage = TabularCPD(
    variable='Incorrect Voltage', variable_card=2,
    values=[
        [0.7, 0.2],
        [0.3, 0.8]
    ],
    evidence=['Incorrect Coolant Pressure'],
    evidence_card=[2]
)

# Add CPSs to the model
model.add_cpds(
    cpd_refrigerator_doesnt_cool,
    cpd_refrigerator_fills_with_frost,
    cpd_light_not_turning_on,
    cpd_refrigerator_doesnt_stop,
    cpd_incorrect_internal_temperature,
    cpd_incorrect_voltage
)

if __name__ == '__main__':
    print(model.check_model())
    print(model.get_cpds())
    print(model.get_independencies())