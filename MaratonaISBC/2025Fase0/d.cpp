#include <iostream>
#include <iomanip>

using namespace std;
int main(){
	int n; 
	float s = 0; 
	float t = 0;
	char c;
	cin >> n;

	for(int i = 0; i < n; i++){
		cin >> c;
		if(c == '*') {
			t++;
		}	
	}

	for(int i = 0; i < n; i++){
		cin >> c;
		if(c == '*') { 
			s++;
		}
	}

	cout << setprecision(2) << fixed << 1-(s/t) << endl;

	return 0;
}
