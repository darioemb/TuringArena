#include <stdio.h>

using namespace std;



int poldo(int N, int P[], int soluzione[]) 
{
int i = 0;
int j = 0;
int massimo = 0;

for (i = 0 ; i<N ; i++) {
    soluzione[i] = 0;
    for (j = i - 1 ; j >=0 ;j--)
        if (P[j] > P[i] && soluzione[i] < soluzione[j] + 1)
            soluzione[i] = soluzione[j] + 1;
        if (soluzione[i] > massimo) 
            massimo = soluzione[i];
}

return massimo;
}
