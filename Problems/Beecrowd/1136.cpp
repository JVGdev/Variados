#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;
int main(){
	
	int n, b;
	int passed = 0;
	vector<int> bs;
	while(cin >> n >> b) {
		if(b < 2){
			return 0;
		}
		
		for(int i = 0; i<b ; i++){
			int a;
			cin >> a;
			bs.push_back(a);
		}
		for(int i = b-1; i >= 0; i--){
			for(int j: bs){
				if (bs[i]==j) break;
				for(int k = 0; k < n; k++){
					if(abs(bs[i]-j) == k){
						passed++;
						break;
					}
				}
			}
			bs.pop_back();
		}
	bs.clear();
	cout << ((passed >= n+1) ? 'Y' : 'F') << endl;
	passed = 0;
	}

	return 0;
}
