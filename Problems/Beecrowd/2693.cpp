#include <iostream>
#include <algorithm>

using namespace std;

struct Passenger{

	string name;
	char dir;
	int dis;
};


int main(){

	int n;
	while(cin >> n){
		
		long unsigned int size = n;
		Passenger bus[size];
		
		while(n--){
			Passenger aux;
			cin >> aux.name >> aux.dir >> aux.dis;
			bus[n] = aux;
		}	

		sort(bus, bus+size, [](const Passenger &a, const Passenger &b){
			return tie(a.dis, a.dir, a.name) < tie(b.dis, b.dir, b.name);
		});

		for(auto p: bus){
			cout << p.name << endl;
		}
	
	}
		return 0;
}
