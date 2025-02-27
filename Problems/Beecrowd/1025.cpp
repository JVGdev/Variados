#include <iostream>
#include <algorithm>

using namespace std;
int main(){
	int c = 0;
	while(true){
	c++;
	int n, q;
	cin >> n >> q;
	if(n == 0 && q == 0){break;}
	int line[n];
	
	for(int i = 0; i < n; i++){
		cin >> line[i];
	}

	sort(line, line + n);

	cout << "CASE# " << c << ":" << endl;
	for(int i = 0; i < q; i++){
		int query;
		cin >> query;
		
		auto ptr = find(line, line + n, query);
		int idx = ptr - line;
		
		if(idx >= n){
			cout << query << " not found" << endl;
		} else {
			cout << query <<" found at " << idx+1 << endl;
		}
	
	}
	}

	return 0;
}
