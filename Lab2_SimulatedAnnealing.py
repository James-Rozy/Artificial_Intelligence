"""
CECS 451: Lab #2: Simulated Annealing
@author: James Rozsypal
"""
from __future__ import print_function, division  # python 2 compatability if needed

import numpy as np
import numpy.random as rn
import matplotlib.pyplot as plt
import matplotlib as mpl

from scipy import optimize

import seaborn as sns 
sns.set(context="talk", style="darkgrid", palette="hls", font="sans-serif", font_scale = 1.05)

FIGSIZE = (19, 8)
mpl.rcParams['figure.figsize'] = FIGSIZE

def annealing(random_start,
              cost_function,
              random_neighbor,
              acceptance,
              temperature, 
               max_steps=1000,
              debug=True):
    state = random_start()
    cost = cost_function(state)
    states, costs = [state], [cost]
    
    for step in range(max_steps):
        fraction = step / float(max_steps)
        T = temperature(fraction)
        new_state = random_neighbor(state, fraction)
        new_cost = cost_function(new_state)
        
        if debug: print("Step #{:>2}/{:>2} : T = {:>4.3g}, state = {:>4.3g}, cost = {:>4.3g}, new_state = {:>4.3g}, new_cost = {:>4.3g} ...".format(step, max_steps, T, state, cost, new_state, new_cost))
        
        if acceptance(cost, new_cost, T) > rn.random():
            state, cost = new_state, new_cost
            states.append(state)
            costs.append(cost)
        
    return state, cost_function(state), states, costs


def see_annealing(states, costs):
    plt.figure()
    plt.suptitle("Evolution of states and costs of the simulated annealing")
    plt.subplot(121)
    plt.plot(states, 'r')
    plt.title("States")
    plt.subplot(122)
    plt.plot(costs,'b')
    plt.title("Costs")
    plt.show()


def visualize_annealing(cost_function):
    state, c, states, costs = annealing(random_start, cost_function, random_neighbor, acceptance_probability, temperature, max_steps=1000, debug=False)
    see_annealing(states, costs)
    return state, c


interval = (-10, 10)


def f(x):
    # Function to minimize
    return x**2


def clip(x):
    # Force x to be in the interval
    a, b = interval
    return max(min(x,b), a)


def random_start():
    # Random point in the interval
    a, b = interval
    return a + (b - a) * rn.random_sample()


def cost_function(x):
    # Cost of x = f(x)
    return f(x)


def random_neighbor(x, fraction=1):
    amplitude = (max(interval) - min(interval)) * fraction / 10
    delta = (-amplitude/2.0) + amplitude * rn.random_sample()
    return clip(x + delta)


def acceptance_probability(cost, new_cost, temperature):
    if new_cost < cost:
        return 1
    else:
        p = np.exp(-(new_cost - cost) / temperature)
        return p
    
    
def temperature(fraction):
    # Example of temperature decreasing as the process goes on
    return max(0.01, min(1, 1 - fraction))


# Calling upon our work!

annealing(random_start, cost_function, random_neighbor, acceptance_probability, temperature, max_steps=30, debug=True)

state, c, states, costs = annealing(random_start, cost_function, random_neighbor, acceptance_probability, temperature, max_steps=1000, debug=False)

visualize_annealing(lambda x: x**2)
    

