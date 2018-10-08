#include <stdio.h>
#define MAXN 100000

int D[MAXN];
int rifornisci(int N, int M, int K, int D[]) {

   int A = 0;
   int distributori = 0; // per i distributori che vengono utilizzati
   for (int i = 0; i < N; i++)

       if (D[i] >= A+M)
       {
           if (D[i] <= K) return distributori;
           distributori = distributori + 1;
           A = D[i];
       }

    if (K - A > M ) ;

   return distributori;
}