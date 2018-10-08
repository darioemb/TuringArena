import random
import math



from turingarena import *

Task = [False]*4

def evaluate():
    #task 2
    for _ in range(0, 10): 
        N = random.randint(1, 1000)
          
        insieme = [
            random.randint(1, 1000)
            for _ in range(0, N)
            
        ]
        
        K=2
        
        
        ret = compute(N, K, insieme)
        correct = solve(N, K, insieme)
        if ret == correct:
            print(f"Task 2 -- > (correct)  constraints subtask(4): K=2  N<=1000")
            
        else:
            print(f"Task 2 -- > {ret}!={correct}(wrong)  constraints subtask(4): K=2 N<=1000")
            Task[2] = False
    for _ in range(0, 5):
    # Task 3 
        
        N = random.randint(1, 10)
        K = random.randint(1, 1000)
        

        insieme = [
            random.randint(1, 100000)
            for _ in range(0, N)
            
        ]
    
               
        ret = compute(N, K, insieme)
        
        correct = solve(N, K, insieme)
        if ret == correct:
            print(f"Task 3 -- > (correct)  constraints subtask(3):N<=10")
            
            
        else:
            print(f"Task 3 -- > {ret}!={correct}(wrong)  constraints subtask(3):N<=10")
            Task[3] = False
    
    #task 4
   
    for _ in range(0, 2): 
        
        N = random.randint(1, 100000)
        
        K = random.randint(1, 1000)
        

        insieme = [
            random.randint(1, 100000)
            for _ in range(0, N)
            
        ]
    
               
        ret = compute(N, K, insieme)
        
        correct = solve(N, K, insieme)
        if ret == correct:
            print(f"Task 4 -- > (correct)  constraints subtask(4):N<=100000")
            
            
        else:
            print(f"Task 4 -- > {ret}!={correct}(wrong)  constraints subtask(4):N<=100000")
            Task[3] = False
    
    
   
   
def compute(N, K, insieme):
    try:

        with run_algorithm(submission.source) as process:
            return process.functions.Trova(N, K, insieme)
        
        
    except AlgorithmError as e:
        print(e)
        return -1
    finally:
        print(process.time_usage)

def solve(N, K, insieme):
    massimo = 100000
    presente = [False]*100001
    
    for i in range(N):
         
        presente[insieme[i]]=True
    risposta = 0
    if K>1:
        for i in range(100001):
            if presente[i]:
                risposta = risposta + 1

                if (i*K) <= massimo and presente[K*i]:
                    presente[i*K]=False

    return risposta
        
    
      
    
evaluate()

   