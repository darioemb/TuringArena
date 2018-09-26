
#include <iostream>


using namespace std;

int poldo(int N, int P[], int soluzione[])
{

      
    //int P[N];
    
    //for (int i = 0; i < N; i++)
        //in>>panini[i];
    
    soluzione[N];
    soluzione[0] = 1;
    
    for (int i = 1; i < N; i++)
    {
        
        int maxSol = 0;
        for (int j = i-1; j >= 0; j--)
            if (P[j] > P[i])
                maxSol = max(maxSol,soluzione[j]);
         soluzione[i] = maxSol+1;
    }
    
    int massimo = soluzione[0];
    for (int i = 0; i<N; i++)
        massimo = max(massimo,soluzione[i]);
        
       
    
    return massimo;
}

