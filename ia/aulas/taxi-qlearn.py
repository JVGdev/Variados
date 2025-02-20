import gym
import numpy as np
import random
from IPython.display import clear_output

env = gym.make('Taxi-v3', render_mode='ansi')

env.reset()
print(env.render())

q_table = np.zeros([env.observation_space.n, env.action_space.n])


# moves: 0=south, 1=north, 2=east, 3=west, 4=pick, 5=drop -+- #
alpha = 0.1
gamma = 0.6
epsilon = 0.1

for i in range(100000):
    estado = env.reset()
    print(estado)
    penalidade = 0
    recompensa = 0
    done = False
    while not done:
        if random.uniform(0, 1) < epsilon:
            action = env.action_space.sample()
        else:
            action = np.argmax(q_table[estado[0]])

        proximo_estado, recompensa, done, info = env.step(action)
        q_antigo = q_table[estado, action]
        proximo_maximo = np.max(q_table[proximo_estado])
    
        q_novo = q_antigo + alpha * (recompensa + gamma * proximo_maximo)
        q_table[estado, action] = q_novo

        if recompensa == -10:
            penalidades += 1
        estado = proximo_estado

    if i % 100 == 0:
        clear_output(wait=True)
        print("Episódio: ", i)

    print("\n\nTreinamento Concluído\n")
