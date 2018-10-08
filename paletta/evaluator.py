import random


from turingarena import *

Task = [False]*6

def evaluate():
    # Task 2
    for _ in range(0, 5): 

        N = random.randint(1, 100)
        V = [
            random.randint(1, N)
            for _ in range(0, N)
        ]
        V.sort()
        ret = compute(N, V)
        correct = solve(N, V)
        if ret == correct:
            print(f"Task 2 -- > (correct)  constraints for subtask(2): N ≤ 100")
            
        else:
            print(f"Task 2 -- > {ret}!={correct}(wrong)  constraints for subtask(2): N ≤ 100")
            Task[2] = False
    
    #task 3
   
    for _ in range(0, 3): 
        N = random.randint(1, 5000)
        
        V = [
            random.randint(1, N)
            for _ in range(0, N)
            ]
        V.sort()
        ret = compute(N, V)
        correct = solve(N, V)
        if ret == correct:
            print(f"Task 3 -- > (correct)  constraints for subtask(3): N ≤ 5000")
            
        else:
            print(f"Task 3 -- > {ret}!={correct}(wrong)  subtask(3): N ≤ 5000")
            Task[3] = False
    #task 5
    
    for _ in range(0, 1): 
        N = random.randint(1, 10000)
        V = [
            random.randint(1, N)
            for _ in range(0, N)
        ]
        V.sort()
        ret = compute(N, V)
        correct = solve(N, V)
        if ret == correct:
            print(f"Task 5 -- > (correct)  subtask(4):N ≤ 10000")
            
        else:
            print(f"Task 5 -- > {ret}!={correct}(wrong)  subtask(4):N ≤ 10000")
            Task[5] = False
    #task 6
    
    for _ in range(0, 1): 
        N = random.randint(1, 15000)
        V = [
            random.randint(1, N)
            for _ in range(0, N)
        ]
        V.sort()
        ret = compute(N, V)
        correct = solve(N, V)
        if ret == correct:
            print(f"Task 6 -- > (correct)  subtask(4):N ≤ 15000")
            
        else:
            print(f"Task 6 -- > {ret}!={correct}(wrong)  subtask(4):N ≤ 1500000")
            Task[6] = False
def compute(N, V):
    try:
        with run_algorithm(submission.source) as process:
            return process.functions.paletta_sort(N, V)
    except AlgorithmError as e:
        print(e)
        return -1
    finally:
	    print(process.time_usage)

def ask(i):
    res = 0
    for i  in range((0,N,[i&(i+1)-1])):
        res = res+fen[i]
    return res
    	
def add(i, N):
    for i in range((0,N,[i|(i+1)])):
        fen[i]

def Solve(N):
    for i in range((N)):
        fen[i] = 0
    for i in range((N)):
        od[A[i]] = i
    res = 0
    for i in range(N-1, 0):
        res = res + ask(od[i])
        add(od[i], N)
    return res

def solve(N, V):
    res=0
    for i in range((N)):
        if V[i]%2 != i%2:
            return -1

    for i in range(1,N,[2]):
        A[(i-1)/2] = (V[i]-1)/2
        res = res + Solve(N/2)
    return res
    

evaluate()

        







