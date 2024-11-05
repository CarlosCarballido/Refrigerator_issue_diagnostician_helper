# Script para entrenar el modelo bayesiano

import pandas as pd
from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.estimators import MaximumLikelihoodEstimator, BayesianEstimator

# Definición del modelo
model = BayesianNetwork([
    ("Incorrect Internal Temperature", "Refrigerator Doesn't Cool"),
    ("Incorrect Internal Temperature", "Refrigerator Fills with Frost"),
    ("Incorrect Voltage", "Light Not Turning On"),
    ("Incorrect Voltage", "Refrigerator Doesn't Stop"),
    ("Incorrect Coolant Pressure", "Incorrect Voltage"),
    ("Compressor Failure", "Refrigerator Doesn't Stop"),
    ("Door Doesn't Lock", "Incorrect Internal Temperature"),
    ("Dirt", "Incorrect Internal Temperature"),
    ("Incorrect Fan Speed", "Incorrect Internal Temperature"),
    ("Incorrect Coolant Pressure", "Incorrect Internal Temperature")
])

# Ejemplo de datos observados
data = pd.DataFrame({
    "Incorrect Internal Temperature": [0, 1, 0, 1, 1],
    "Refrigerator Doesn't Cool": [1, 1, 0, 1, 0],
    "Refrigerator Fills with Frost": [0, 1, 1, 0, 1],
    "Light Not Turning On": [0, 1, 0, 0, 1],
    "Refrigerator Doesn't Stop": [1, 1, 0, 1, 0],
    "Incorrect Voltage": [0, 1, 0, 1, 1],
    "Incorrect Coolant Pressure": [1, 0, 1, 1, 0],
    "Compressor Failure": [0, 1, 0, 1, 0],
    "Door Doesn't Lock": [1, 0, 1, 1, 0],
    "Dirt": [0, 1, 0, 1, 1],
    "Incorrect Fan Speed": [1, 0, 1, 0, 1]
})

# Entrenamiento del modelo con MaximumLikelihoodEstimator
model.fit(data, estimator=MaximumLikelihoodEstimator)

# Visualización de los CPDs entrenados
print("CPDs ajustados con MaximumLikelihoodEstimator:")
for cpd in model.get_cpds():
    print(cpd)

# (Opcional) Entrenamiento del modelo con BayesianEstimator y pseudocontadores (equivalent_sample_size=5)
model.fit(data, estimator=BayesianEstimator, prior_type="BDeu", equivalent_sample_size=5)

# Visualización de los CPDs entrenados con BayesianEstimator
print("\nCPDs ajustados con BayesianEstimator:")

for cpd in model.get_cpds():
    print(cpd)