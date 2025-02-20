import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

qualidade = ctrl.Antecedent(np.arange(0, 11, 1), 'qualidade')
servico = ctrl.Antecedent(np.arange(0, 11, 1), 'servico')
gorjeta = ctrl.Consequent(np.arange(0, 21, 1), 'gorjeta')

qualidade.automf(number=3, names=['ruim', 'boa', 'saborosa'])
servico.automf(number=3, names=['ruim', 'aceitavel', 'otimo'])

gorjeta['baixa'] = fuzz.trimf(gorjeta.universe, [0, 0, 8])
gorjeta['media'] = fuzz.trimf(gorjeta.universe, [8, 12, 16])
gorjeta['alta'] = fuzz.trimf(gorjeta.universe, [12, 20, 20])

regra1 = ctrl.Rule(qualidade['ruim'] | servico['ruim'], gorjeta['baixa'])
regra2 = ctrl.Rule(servico['aceitavel'], gorjeta['media'])
regra3 = ctrl.Rule(servico['otimo'] | qualidade['saborosa'], gorjeta['alta'])

sistema_controle = ctrl.ControlSystem([regra1, regra2, regra3])
sistema = ctrl.ControlSystemSimulation(sistema_controle)

sistema.input['qualidade'] = 10.0
sistema.input['servico'] = 10.0
sistema.compute()

print(sistema.output['gorjeta'])

