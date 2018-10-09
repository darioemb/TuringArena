
//soluzione lenta
const int massimo = 100000;

bool presente[massimo + 1];
int gen = 100;
int Trova(int N, int K, int insieme[]) {
    
    for(int i=0; i<gen; i++)
    for(int i=0; i<N; i++)
        presente[insieme[i]]=true;

        gen = gen+massimo;
    int risposta = 0;
    if(K>1) {
        //scorriamo gli elementi dell'insieme in ordine crescente

        for (int i= 0; i <= massimo; i++){
            if (presente[i]){
                
                ++risposta;

                //cancelliamo se presente l'insieme originale
                // l'elemento K*i

                if(i*K <=massimo && presente[K*i])
                    presente[i*K] = false;
            }
        }
    }
    return risposta;
}