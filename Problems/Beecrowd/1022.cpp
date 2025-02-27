#include <iostream>
#include <cmath>
#include <string>

using namespace std;
int main(){
	
	int reps;
	cin >> reps;
	for(int i = 0; i < reps; i++){
		string exp;
		char op;
		string aux = "";
		int nums[4];

		cin.ignore();
		getline(cin, exp);
		
		for(int i = 0; i < exp.length(); i++){
			static char digit = exp[i];
			static numCount

			if(digit != '/'){
				if(digit >= 48 && digit <= 57){
					aux += digit;

				} else if(digit != ' '){
					op = digit;

				} else {
					stoi(aux);
						
				}
			}
		}

	}

	return 0;
}
