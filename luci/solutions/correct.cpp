

#include <iostream>
#include <list>
#include <stack>
#include <vector>
#include <bitset>
#include <cstdio>
#include <sstream>
#include <climits>
#include <algorithm>
#include <queue>
#include <set>
#include <string.h>


using namespace std;


int spegni(int N, int M, int K)
{


    
        int accese = 0;
        int cnt = 1;
        for (int i = 2; ; i+=2)
        {
            accese+= i;
            cnt+=i;
            if (cnt >= N)
            {
                return accese;
                break;
            }
            
            cnt++;
        }

}


