#include <iostream>
#include <vector>

using namespace std;


int hashfn(int val, int size){
	return val % size;
}

int main(){
	
	int n;
	cin >> n;
	while(n--){
	

		int s, m;
		cin >> s >> m;
		
		vector<int> hashtable[s];
		
		while(m--){
			int c;
			cin >> c;
			hashtable[hashfn(c, s)].push_back(c);	
		}

		for(int i = 0; i < s; i++){
			cout << i << " -> ";
			for(auto a: hashtable[i]){ 
				cout << a << " -> ";
			}
			cout << "\\" << endl;
		}
	

		if(n > 0) { cout << endl; }
	}

	return 0;
}


