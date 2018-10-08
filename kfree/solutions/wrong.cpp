
//soluzione sbagliata
const int massimo=100000;
bool presente[massimo + 1];
int Trova(int N, int K, int insieme[]) {
    int risposta = 0;
    if(K>1) {
        
        for (int i= 0; i <= N; i++){
            if (presente[i]){
                
                ++risposta;

              
                if(i*K <=massimo && presente[K*i])
                    presente[i*K] = false;
            }
        }
    }
    return risposta;
}