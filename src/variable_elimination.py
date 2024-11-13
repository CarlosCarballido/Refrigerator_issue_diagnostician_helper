from models.bayesian_network_model import BayesianNetworkModel

class VariableElimination:
    def __init__(self, model: BayesianNetworkModel):
        self.model = model

    def query(self, variable: str, evidence: dict):
        factors = self.model.factors()
        for var, value in evidence.items():
            factors = self.inference(var, value, factors)
        return self.inference(variable, None, factors)
    
    def inference(self, variable: str, value: str, factors: list):
        factors = self.reduce_factors(variable, value, factors)
        return self.multiply_factors(factors)
    
if __name__ == "__main__":
    from models.bayesian_network_model import BayesianNetworkModel

    model = BayesianNetworkModel()
    model.add_variable("A", ["T", "F"])
    model.add_variable("B", ["T", "F"])
    model.add_variable("C", ["T", "F"])
    model.add_variable("D", ["T", "F"])
    model.add_cpt("A", [], [0.5, 0.5])
    model.add_cpt("B", ["A"], [0.5, 0.5, 0.5, 0.5])
    model.add_cpt("C", ["A"], [0.5, 0.5, 0.5, 0.5])