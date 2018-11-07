from pgmpy.models import BayesianModel 
from pgmpy.factors.discrete import TabularCPD
test_model = BayesianModel([('rain', 'sprinkler'),('rain','wetGrass'),('sprinkler','wetGrass')])


cpd_rain = TabularCPD(variable='rain', variable_card=2, values=[[0.2],[0.8]])
cpd_wetGrass = TabularCPD(variable='wetGrass', variable_card=2, values=[[0,1],[0.8,0.2],[0.9,0.1],[0.99,0.01]], evidence=['rain','sprinkler'], evidence_card=[2, 2])
cpd_sprinkler = TabularCPD(variable='sprinkler', variable_card=2, values=[[0.4,0.01],[0.6,0.99]],evidence=['rain'], evidence_card=[2])


test_model.add_cpds(cpd_rain,cpd_sprinkler,cpd_wetGrass)
test_model.check_model()