#include <iostream>
#include <algorithm>

using namespace std;

int main(){
	int n;
	cin >> n;	
	
	int line[n];
	int size = n;
	while(n--){
		cin >> line[size-1-n];
	}
	cin >> n;
	while(n--){
		int rem;
		cin >> rem;
		
		auto it = find(line, line+size, rem);
		*it = 0;
	}
	bool first = true;
	for(auto i: line){
		if(i!=0){
			if(!first){
				cout << ' ';
			} else {
				first = false;}
			cout << i;

		}
	}
	cout << endl;
	return 0;
}
