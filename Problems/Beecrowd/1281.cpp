#include <unordered_map>
#include <iostream>
#include <string>
#include <iomanip>

using namespace std;

int main(){
	unordered_map<string, double> prods;
	int n;
	cin >> n;
	while(n--){
		double bill = 0;
		int m;
		cin >> m;
		while(m--){
			string prod;
			double val;
			cin >> prod >> val;
			prods[prod] = val;
		}
		int p;
		cin >> p;
		while(p--){
			string prod;
			int qnt;
			cin >> prod >> qnt;
			bill += prods[prod] * qnt;	
		}
		cout << "R$ " << fixed << setprecision(2) << bill << endl;
	}

	return 0;
}
