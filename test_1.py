import random
n_agents = 125
n_tasks = 3000
n_iterations = 1000

population = [random.sample(range(n_agents),n_agents)for _ in range(n_tasks)]

print(population)