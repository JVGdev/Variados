#include <iostream>
#include <map>
#include <iomanip>

using namespace std;
int main(){
	map<string, int> trees; 
	int n, total = 0;
	cin >> n;
	cin.ignore();
	cin.ignore();
	while(n--){
		string s;
		while(getline(cin, s)){
			if(s.empty()) { break; }
			trees[s]++;
			total++;
		}
		
		for(auto t: trees){
			cout << t.first << " " << fixed << setprecision(4) << (t.second/((double)total))*100 << endl;
		}
		
		trees.clear();
		total = 0;
		if(n != 0) { cout << endl; }
	}	

	return 0;
}
