from pgmpy.models import BayesianNetwork

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
