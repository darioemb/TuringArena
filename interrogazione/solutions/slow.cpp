#include <stdio.h>
#include <algorithm>

#define MAXN 10000
int D[MAXN];

using namespace std;

int interroga(int N, int K, int D[])
{

   sort(D,D+N);

   
   int dis = 100;
   int diff = 1000000;
   for (int i = 0; i < N; i++)
        for (int i = 0; i <= N-K; i++)
            diff = min(diff,abs(D[i]-D[i+K-1]));
        dis++;
    return diff;
}
