import random


from turingarena import *

Task = [False]*4

def evaluate():
    # Task 2
    N = random.randint(1, 10)
    M = random.randint(1, 100)
    K = random.randint(1, 1000)
    D = [
        random.randint(1, M)
        for _ in range(0, N)
    ]
    D.sort()
    for _ in range(0, 10): 
        ret = compute(N, M, K, D)
        correct = solve(N, M, K, D)
        if ret == correct:
            print(f"Task 2 -- > (correct)")
            Task[2] = True
        else:
            print(f"Task 2 -- > {ret}!={correct}(wrong)")
            Task[2] = False

    #task 3
   
    for _ in range(0, 5): 
        N = random.randint(1, 1000)
        M = random.randint(1, 100)
        K = random.randint(1, 1000)
        D = [
            random.randint(1, M)
            for _ in range(0, N)
            ]
        D.sort()
        ret = compute(N, M, K, D)
        correct = solve(N, M, K, D)
        if ret == correct:
            print(f"Task 3 -- > (correct)")
            Task[2] = True
        else:
            print(f"Task 3 -- > {ret}!={correct}(wrong)")

    #task 4
    
    for _ in range(0, 2): 
        N = random.randint(1, 100000)
        M = random.randint(1, 10000)
        K = random.randint(0, 100000)
        D = [
            random.randint(1, M)
            for _ in range(0, N)
        ]
        D.sort()
        ret = compute(N, M, K, D)
        correct = solve(N, M, K, D)
        if ret == correct:
            print(f"Task 4 -- > (correct)")
            Task[2] = True
        else:
            print(f"Task 4 -- > {ret}!={correct}(wrong)")

def compute(N, M, K, D):
    try:
        with run_algorithm(submission.source) as process:
            return process.functions.rifornisci(N, M, K,D)
    except AlgorithmError as e:
        print(e)
        return -1

def solve(N, M, K, D):
    d = 0
    A = 0
    for i in range(0, N):
        if D[i] > A+M:
        
            if D[i-1] > K:
                d = d + 1
                A = D[i-1]
                return d
    if K - A > M:
        d = d + 1
    return d

evaluate()

        







