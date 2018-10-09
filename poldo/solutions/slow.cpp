#include <stdio.h>

using namespace std;



int poldo(int N, int P[], int soluzione[]) 
{
int v = 0;
int i = 0;
int j = 0;
int massimo = 0;

for (i = 0 ; i<N+1 ; i++)
for (i = 0 ; i<N ; i++) {
    soluzione[i] = 1;
    v = v+1;
    for (j = i - 1 ; j >=0 ;j--)
        if (P[j] > P[i] && soluzione[i] < soluzione[j] + 1)
            soluzione[i] = soluzione[j] + 1;
        if (soluzione[i] > massimo) 
            massimo = soluzione[i];
            v=v+massimo;
}

return massimo;
}
