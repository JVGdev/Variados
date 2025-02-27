#include <iostream>
#include <string>

using namespace std;
int main() {

	int n;
	cin >> n;
	while(n--){
		int r = 0;
		string line;
		cin >> line;
		if(line[0] == line[2]){
			r = (line[2] - '0') * (line[0] - '0');
		}
		else if(isupper(line[1])){
			r = (line[2] - '0') - (line[0] - '0');
		} else if (islower(line[1])){
			r = (line[2] - '0') + (line[0] - '0');
		}
		
		cout << r << endl;
	}

	return 0;
}
