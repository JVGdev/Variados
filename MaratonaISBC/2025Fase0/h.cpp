#include <iostream>
#include <cmath>
#include <bitset>
#include <string>

std::string removeZeroInator(std::string str){
    int len = 59;
    int readUntil = 0;
    bool z = true;
    std::string ret = "";

    for (int i = 0; i < 59; i++){
        if (!z){
            ret += str.at(i);
        }

        else if (str.at(i) != '0'){ // Executa no primeiro no 0
            z = false;
            ret += str.at(i);
        }

        else {
            len--;
        }
    }

    // Inverter e copiar a macumba
    	std::cout << ret << std::endl;
    	std::string ret2 = ret;
	int l = ret.length();
	int a = l-1;
    	for(int i = 0; i < l; i++){
		if(ret.at(i) != ret2.at(a)){
			if(ret.at(a) == '0'){
				ret.at(i) = '0';
			} else {
				ret.at(a) = '0';
			}
		}
		a--;
		if(a < i) break;
	}
    	std::cout << ret << std::endl;
    return ret;
}

int main(){
    unsigned long int n;
    std::cin >> n;

    std::string b = std::bitset<59>(n).to_string();


    std::cout << std::stol(removeZeroInator(b), nullptr, 2) << std::endl;

    return 0;
}
