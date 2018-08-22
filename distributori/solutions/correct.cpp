#include <stdio.h>
#define MAXN 100000
using namespace std;
int D[MAXN];
int rifornisci(int N, int M, int K, int D[]) {

   int A = 0;
   int d = 0; // per i distributori che vengono utilizzati
   for (int i = 0; i < N; i++)

       if (D[i] > A+M)
       {
           if (D[i-1] > K) return d;
           d++;
           A = D[i-1];
       }

    if (K - A > M ) d++;

   return d;
}





