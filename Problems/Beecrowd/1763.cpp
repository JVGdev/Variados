#include <iostream>
#include <unordered_map>

using namespace std;

int main(){
	unordered_map<string, string> langs{
		{"brasil", "Feliz Natal!"},
		{"alemanha", "Frohliche Weihnachten!"},
		{"austria", "Frohe Weihnacht!"},
		{"coreia", "Chuk Sung Tan!"},
		{"espanha", "Feliz Navidad!"},
		{"grecia", "Kala Christougena!"},
		{"estados-unidos", "Merry Christmas!"},
		{"inglaterra", "Merry Christmas!"},
		{"australia", "Merry Christmas!"},
		{"portugal", "Feliz Natal!"},
		{"suecia", "God Jul!"},
		{"turquia", "Mutlu Noeller"},
		{"argentina", "Feliz Navidad!"},
		{"chile", "Feliz Navidad!"},
		{"mexico", "Feliz Navidad!"},
		{"antardida", "Merry Christmas!"},
		{"canada", "Merry Christmas!"},
		{"irlanda", "Nollaig Shona Dhuit!"},
		{"belgica", "Zalig Kerstfeest!"},
		{"italia", "Buon Natale!"},
		{"libia", "Buon Natale!"},
		{"siria", "Milad Mubarak!"},
		{"marrocos", "Milad Mubarak!"},
		{"japao", "Merii Kurisumasu!"}};
	string s;
	while(cin >> s){
		if(langs.count(s)){
			cout << langs[s] << endl;
		} else {
			cout << "--- NOT FOUND ---" << endl;
		}
	}

	return 0;
}


