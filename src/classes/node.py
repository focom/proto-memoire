from pgmpy.models import BayesianModel 
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination


test_model = BayesianModel([('rain', 'sprinkler'),('rain','wetGrass'),('sprinkler','wetGrass')])


cpd_rain = TabularCPD(variable='rain', variable_card=2, values=[[0.2],[0.8]])
cpd_wetGrass = TabularCPD(variable='wetGrass', variable_card=2, values=[[0,0.8,0.9,0.99],[1,0.2,0.1,0.01]], evidence=['rain','sprinkler'], evidence_card=[2, 2])
cpd_sprinkler = TabularCPD(variable='sprinkler', variable_card=2, values=[[0.4,0.01],[0.6,0.99]],evidence=['rain'], evidence_card=[2])


test_model.add_cpds(cpd_rain,cpd_sprinkler,cpd_wetGrass)
test_model.edges()
test_model.nodes()
test_model.check_model()

# print('hello')


test_infer = VariableElimination(test_model)

q = test_infer.query(variables=['wetGrass'], evidence={'rain':1})
result = q['wetGrass']
string = str(q['wetGrass'])
print(string)
print(type(string))



"""

    P(grade|diff, intel)
        +-------+--------------------+------------------+
        |diff   |      easy          |    hard          |
        +-------+-----+------+-------+------+----+------+
        |intel  |dumb |  avg | smart | dumb |avg |smart |
        +-------+-----+------+-------+------+----+------+
        |gradeA |0.1  |  0.1 |  0.1  | 0.1  |0.1 | 0.1  |
        +-------+-----+------+-------+------+----+------+
        |gradeB |0.1  |  0.1 |  0.1  | 0.1  |0.1 | 0.1  |
        +-------+-----+------+-------+------+----+------+
        |gradeC |0.8  |  0.8 |  0.8  | 0.8  |0.8 | 0.8  |
        +-------+-----+------+-------+------+----+------+

        values should be
        [[0.1,0.1,0.1,0.1,0.1,0.1],
        [0.1,0.1,0.1,0.1,0.1,0.1],
        [0.8,0.8,0.8,0.8,0.8,0.8]]


    """


#   def _str(self, phi_or_p="phi", tablefmt="grid", print_state_names=True):
#         """
#         Generate the string from `__str__` method.
#         Parameters
#         ----------
#         phi_or_p: 'phi' | 'p'
#                 'phi': When used for Factors.
#                   'p': When used for CPDs.
#         print_state_names: boolean
#                 If True, the user defined state names are displayed.
#         """
#         string_header = list(map(lambda x: six.text_type(x), self.scope()))
#         string_header.append('{phi_or_p}({variables})'.format(phi_or_p=phi_or_p,
#                                                               variables=','.join(string_header)))

#         value_index = 0
#         factor_table = []
#         for prob in product(*[range(card) for card in self.cardinality]):
#             if self.state_names and print_state_names:
#                 prob_list = ["{var}({state})".format(
#                     var=list(self.variables)[i], state=self.state_names[list(
#                         self.variables)[i]][prob[i]])
#                              for i in range(len(self.variables))]
#             else:
#                 prob_list = ["{s}_{d}".format(s=list(self.variables)[i], d=prob[i])
#                              for i in range(len(self.variables))]

#             prob_list.append(self.values.ravel()[value_index])
#             factor_table.append(prob_list)
#             value_index += 1

# return tabulate(factor_table, headers=string_header, tablefmt=tablefmt, floatfmt=".4f")


