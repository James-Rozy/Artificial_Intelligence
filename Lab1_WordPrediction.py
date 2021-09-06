"""
CECS 451: Lab #1: Word Prediction
@author: James Rozsypal
"""
import random
import string


target = list("James")


def generate_random_solutions(length=len(target)):
    return [random.choice(string.printable) for i in range(length)]


def evaluate(solution):
    diff = 0
    
    for i in range(len(target)):
        s = solution[i]
        t = target[i]
        diff += abs(ord(s) - ord(t))
        
    return diff


def mutate_solution(solution):
    index = random.randint(0, len(solution)-1)
    solution[index] = random.choice(string.printable)
    


best = generate_random_solutions()
best_score = evaluate(best)

# for counting how many attempts it takes to find the answer
iterations = 0

# infinite loop for finding the solution
while True:
    iterations += 1
    
    print("# of iterations:", iterations, "The best score yet is:" , best_score, "Solution: "+"".join(best))
    
    if best_score == 0:
        break
    
    new_solution = list(best)
    mutate_solution(new_solution)
    score = evaluate(new_solution)
    
    if score < best_score:
        best = new_solution
        best_score = score