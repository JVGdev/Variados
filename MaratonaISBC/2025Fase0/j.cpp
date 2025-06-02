#include <iostream>
#include <thread>

void t1(int a[], int i, int k, int n, std::string *b){
    	int part, index;
    	
	
	part = a[i]; // Com fase inicializada em Ai.
        
	index = i;
        while(true){
            if (part <= a[index]){ // Passou
                part += k;
                index = (index % n) + 1;
                
                if (index >= n){
                    index = index % n;
                }
            } else{ // Não passou
                b += index + 1;
                if (i != n) b += ' ';
                break;
            }
        }
}

int main(){
	int n, k;
    std::cin >> n >> k;

    int a[n];

	std::string b = "", tmp = "";

    for(int i = 0; i < n; i++){
    	std::cin >> a[i];
    }
    
    
    for(int i = 0; i < n; i++){
	    std::thread t1(a, i, k, n, &b);
    	t1.join();
    }

    std::cout << b << std::endl;
    return 0;
}
