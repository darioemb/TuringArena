
//soluzione ottima
const int massimo = 100000;
//presente[i] vale true se appartiene all'insieme false altrimenti
bool presente[massimo + 1];

int Trova(int N, int K, int insieme[]) {
    //riempiamo l'array presente
    for(int i=0; i<N; i++)
        presente[insieme[i]]=true;

    int risposta = 0;
    if(K>1) {
        //scorriamo gli elementi dell'insieme in ordine crescente

        for (int i= 0; i <= massimo; i++){
            if (presente[i]){
                //inseriamo l'elemento i nel massimo insieme k-free
                //trovato finora
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