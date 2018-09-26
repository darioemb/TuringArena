import random
import math


from turingarena import *

Task = [False]*4

def evaluate():
    # Task 2 
    N = random.randint(1, 100)
          
    P = [
        random.randint(0, 100)
        for _ in range(0, N)
    ]
    P.sort()
    
    soluzione = [
        
        random.randint(0, 100)
        for _ in range(0, N)
        
    ]
    
    soluzione.sort()
   
    
    
    for _ in range(0, 10): 
        soluzione[0]=1
        ret = compute(N, P, soluzione)
        correct = solve(N, P, soluzione)
        if ret == correct:
            print(f"Task 2 -- > (correct)")
            Task[2] = True
        else:
            print(f"Task 2 -- > {ret}!={correct}(wrong)")
            Task[2] = False
    
    #task 3
   
    for _ in range(0, 5): 
        N = random.randint(1, 1000)
          
    P = [
        random.randint(0, 1000)
        for _ in range(0, N)
    ]
    P.sort()
    
    soluzione = [
        
        random.randint(0, 1000)
        for _ in range(0, N)
        
    ]
    soluzione.sort()
    
    for _ in range(0, 5):
        soluzione[0]=1
        ret = compute(N, P, soluzione)
        correct = solve(N, P, soluzione)
        if ret == correct:
            print(f"Task 3 -- > (correct)")
            Task[2] = True
        else:
            print(f"Task 3 -- > {ret}!={correct}(wrong)")
            Task[2] = False
    
    #task 4
    for _ in range(0, 2): 
        N = random.randint(1, 3000)
          
    P = [
        random.randint(0, 3000)
        for _ in range(0, N)
    ]
    P.sort()
    
    soluzione = [
        
        random.randint(0, 3000)
        for _ in range(0, N)
        
    ]
    soluzione.sort()
    for _ in range(0, 2):
        soluzione[0]=1
        ret = compute(N, P, soluzione)
        correct = solve(N, P, soluzione)
        if ret == correct:
            print(f"Task 4 -- > (correct)")
            Task[2] = True
        else:
            print(f"Task 4 -- > {ret}!={correct}(wrong)")
            Task[2] = False
    
 #task 5 si può aumentare il valore di N e P ma impiega tanto tempo
    for _ in range(0, 1): 
        N = random.randint(1, 10000)
          
    P = [
        random.randint(0, 10000)
        for _ in range(0, N)
    ]
    P.sort()
    
    soluzione = [
        
        random.randint(0, 10000)
        for _ in range(0, N)
        
    ]
    soluzione.sort()
    for _ in range(0, 1):
        soluzione[0]=1
        ret = compute(N, P, soluzione)
        correct = solve(N, P, soluzione)
        if ret == correct:
            print(f"Task 5 -- > (correct)")
            Task[2] = True
        else:
            print(f"Task 5 -- > {ret}!={correct}(wrong)")
            Task[2] = False

    
    
def compute(N, P, soluzione):
    try:
        with run_algorithm(submission.source) as process:
            return process.functions.poldo(N, P, soluzione)
    except AlgorithmError as e:
        print(e)
        return -1

def solve(N, P, soluzione):
   
    
    for i in range(0, N):
        
        soluzione[0]=1
        maxSol = 0
        for j in range(i-1, 0):
            #soluzione[0]=1
            if P[j] > P[i]:
                #soluzione[0]=1
                maxSol = max(maxSol,soluzione[j])
        soluzione[i] = maxSol+1
    #soluzione[0]=1
    massimo = soluzione[0]
    for i in range(0, N):
        #soluzione[0]=1
        massimo = max(massimo,soluzione[i])
    
    #soluzione[0]=1
    return massimo

      
    
evaluate()

        







