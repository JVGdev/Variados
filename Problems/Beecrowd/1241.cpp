#include <iostream>
#include <string>

using namespace std;

int main(){

	int n;
	cin >> n;
	while(n--){
		bool enc = 1;
		string a, b;
		cin >> a >> b;

		int max = a.length()-1;
		int i = b.length()-1;
		if (max < i){
			cout << "nao encaixa" << endl;
			continue ;
		}


		for(auto c: b){
			if(c != a[max-i]){
				enc = 0;
				break;
			}
			i--;	
		}
		if(enc){cout << "encaixa" << endl;} else {cout << "nao encaixa" << endl;}
	}
	return 0;
}
