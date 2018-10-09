//soluzione migliore

#include <iostream>
using namespace std;
#define MAXN 1500000

int N;
int F[MAXN];
int A[MAXN];
int od[MAXN];
int fen[MAXN];

int ask(int i) {
	int res = 0;
	for (; i >= 0; i = (i&(i+1))-1) res += fen[i];
	return res;
}

void add(int i, const int N) {
	for (; i < N; i = i|(i+1)) fen[i]++;
}

long long Solve(int N) {
    for (int i = 0; i < N; i++) F[i] = 0;
	for (int i = 0; i < N; i++) fen[i] = 0;
	for (int i = 0; i < N; i++) od[A[i]] = i;
	
	long long res = 0;
	for (int i = N-1; i >= 0; i--) {
		res += (long long)ask(od[i]);
		add(od[i], N);
	}
	return res;
}

long long paletta_sort(int N, int V[]) {	
		
	long long res = 0;
	for (int i = 0; i < N; i++) {
		if (V[i]%2 != i%2) return -1;
	}
	for (int i = 0; i < N; i+=2) A[i/2] = V[i]/2;
	res += Solve((N+1)/2);
	
	for (int i = 1; i < N; i+=2) A[(i-1)/2] = (V[i]-1)/2;
	res += Solve(N/2);
	F[MAXN]=F[MAXN-1];
	return res;
}

