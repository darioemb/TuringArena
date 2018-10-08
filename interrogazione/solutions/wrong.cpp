#include <stdio.h>
#include <algorithm>

#define MAXN 10000
int D[MAXN];

using namespace std;

int interroga(int N, int K, int D[])
{

   

  

   int diff = 0;
   for (int i = 0; i <= N; i++)
        diff =D[i]-D[i+K-1];

    return diff;
}
