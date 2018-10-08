import random
import math


from turingarena import *

Task = [False]*4

def evaluate():
    # Task 2 volendo si può ingrandire le difficoltà in D ora è =100
    N = random.randint(1, 10)
    K = random.randint(1, 10)
    D = [
        random.randint(1, 100000)
        for _ in range(0, N)
    ]
    D.sort()
    for _ in range(0, 10): 
        ret = compute(N, K, D)
        correct = solve(N, K, D)
        if ret == correct:
            print(f"Task 2 -- > (correct)")
            Task[2] = True
        else:
            print(f"Task 2 -- > {ret}!={correct}(wrong)")
            Task[2] = False
    
    #task 3
   
    for _ in range(0, 5): 
        N = random.randint(1, 1000)
        K = random.randint(1, 2)
        D = [
            random.randint(1, 100000)
            for _ in range(0, N)
            ]
        D.sort()
        ret = compute(N, K, D)
        correct = solve(N, K, D)
        if ret == correct:
            print(f"Task 3 -- > (correct)")
            Task[2] = True
        else:
            print(f"Task 3 -- > {ret}!={correct}(wrong)")
    
    #task 4
    
    for _ in range(0, 2): 
        N = random.randint(1, 100000)
        K = random.randint(0, 100000)
        D = [
            random.randint(1, 100000)
            for _ in range(0, N)
        ]
        D.sort()
        ret = compute(N, K, D)
        correct = solve(N, K, D)
        if ret == correct:
            print(f"Task 4 -- > (correct)")
            Task[2] = True
        else:
            print(f"Task 4 -- > {ret}!={correct}(wrong)")
    
def compute(N, K, D):
    try:
        with run_algorithm(submission.source) as process:
            return process.functions.interroga(N, K, D)
    except AlgorithmError as e:
        print(e)
        return -1
    finally:
        print(process.time_usage)

def solve(N, K, D):
    
    
    diff = 1000000
    for i in range(0, N-K):
        diff = min(diff,abs(D[i]-D[i+K-1]))
    return diff

evaluate()

        







