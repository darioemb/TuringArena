import random


from turingarena import *

Task = [False]*6

def evaluate():
    # Task 2
    for _ in range(0, 10):
        N = random.randint(1, 100)
        M = random.randint(1, 1000000000)
        K = random.randint(1, 100)

        ret = compute(N, M, K)
        correct = solve(N, M, K)
        if ret == correct:
            print(f"Task 2 -- > (correct) subtask constraints: N<=100,K<=100")
            
        else:
            print(f"Task 2 -- > {ret}!={correct}(wrong)")
            Task[2] = False
    
    #task 3
   
    for _ in range(0, 5): 
        N = random.randint(1, 10000)
        M = random.randint(1, 1000000000)
        K = random.randint(1, 1000000000)
       
        ret = compute(N, M, K)
        correct = solve(N, M, K)
        if ret == correct:
            print(f"Task 3 -- > (correct) subtask constaints: N<=10000")
            
        else:
            print(f"Task 3 -- > {ret}!={correct}(wrong)")
            Task[3] = False
    #task 4
    
    for _ in range(0, 1): 
        N = random.randint(1, 1000000)
        M = random.randint(1, 1000000000)
        K = random.randint(0, 1000000000)
        
        ret = compute(N, M, K)
        correct = solve(N, M, K)
        if ret == correct:
            print(f"Task 4 -- > (correct) subtask constraints: N<=1000000")
            
        else:
            print(f"Task 4 -- > {ret}!={correct}(wrong)")
            Task[4] = False
    #task 5
    for _ in range(0, 1): 
        N = random.randint(1, 1000000000)
        M = random.randint(1, 1000000000)
        K = random.randint(0, 1000000000)
        
        ret = compute(N, M, K)
        correct = solve(N, M, K)
        if ret == correct:
            print(f"Task 5 -- > (correct) subtask constraints: No limits")
            
        else:
            print(f"Task 5 -- > {ret}!={correct}(wrong)")
            Task[5] = False

def compute(N, M, K):
    try:
        with run_algorithm(submission.source) as process:
            return process.functions.spegni(N, M, K)
    except AlgorithmError as e:
        print(e)
        return -1
    finally:
	    print(process.time_usage)

def solve(N, M, K):
    MAX=10000000
    accese = 0
    cnt = 1
    for i in range(2, MAX,2):
        accese=accese+i
        cnt=cnt+i
        if cnt>= N:
            return accese
            break
        cnt=cnt+1

evaluate()

        







