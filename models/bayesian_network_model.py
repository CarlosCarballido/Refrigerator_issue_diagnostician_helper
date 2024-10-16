from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD

def create_bayesian_model():
    """
    Crea y devuelve el modelo bayesiano para diagnosticar fallos en neveras.
    """
    model = BayesianNetwork([('Internal_temperature', 'Compressor_status'),
                             ('Voltage', 'Compressor_status'),
                             ('Pressure', 'Compressor_status'),
                             ('Fan_speed', 'Compressor_status'),
                             ('Sensor_status', 'Compressor_status'),
                             ('Door_well_closed', 'Compressor_status'),
                             ('Has_dirt', 'Compressor_status')])
    
    cpd_internal_temp = TabularCPD(variable='Internal_temperature', variable_card=3, 
                                   values=[[0.2],  # Baja temperatura
                                           [0.5],  # Temperatura normal
                                           [0.3]]) # Alta temperatura

    cpd_voltage = TabularCPD(variable='Voltage', variable_card=3, 
                             values=[[0.15],  # Bajo voltaje
                                     [0.7],   # Voltaje normal
                                     [0.15]]) # Alto voltaje

    cpd_pressure = TabularCPD(variable='Pressure', variable_card=3, 
                              values=[[0.25],  # Baja presión
                                      [0.5],   # Presión normal
                                      [0.25]]) # Alta presión

    cpd_fan_speed = TabularCPD(variable='Fan_speed', variable_card=3, 
                               values=[[0.3],   # Velocidad baja
                                       [0.5],   # Velocidad normal
                                       [0.2]])  # Velocidad alta

    cpd_sensor_status = TabularCPD(variable='Sensor_status', variable_card=2, 
                                   values=[[0.95], [0.05]])
    cpd_door_closed = TabularCPD(variable='Door_well_closed', variable_card=2, 
                                 values=[[0.95], [0.05]])
    cpd_has_dirt = TabularCPD(variable='Has_dirt', variable_card=2, 
                              values=[[0.7], [0.3]])
    
    model.add_cpds(cpd_internal_temp, cpd_voltage, cpd_pressure, cpd_fan_speed, cpd_sensor_status, cpd_door_closed, cpd_has_dirt)
    