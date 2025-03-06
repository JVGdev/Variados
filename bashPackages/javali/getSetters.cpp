#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

void getVarNames(string &aux, ifstream &fr, ofstream &fw){
	char c;
	string buff = "";
	int counter = 0;
	vector<string> types;
	vector<string> vars;

	while(fr.get(c)){
		if(c > 32){
			buff += c;
			if(buff == "//e"){break;}
		}
		if(c == ' '){
			counter++;
			if(counter == 2){
				types.push_back(buff);
			}
			buff = "";
		} else if(c == '\n'){
			counter++;
			if(counter == 3){
				buff.pop_back();
				vars.push_back(buff);
			}
			
			counter = 0;
			buff = "";
		}
        	fw << c;	
	}
	}

	fw << endl << endl << "	// -+-+-+-+-+-+- //"; 
	for(int i = 0; i < vars.size(); i++){
		string func = vars[i];
		func[0] = toupper(func[0]);
		fw << endl <<  "	public " << types[i] << " get" << func << "(){\n		return " << vars[i]  << ";\n	}";
		fw << endl <<  "	public void set" << func << "(" << types[i] << " " << vars[i] << "){\n		this." << vars[i]  << " = " << vars[i] << ";\n	}" << endl;
	}
	fw << "	// -+-+-+-+-+-+- //" << endl; 
}

int main(int argc, char **argv){
	string buffer = "temp-";
	string aux;

	ifstream fr(argv[1]);
	ofstream fw(buffer + argv[1]);
	while(getline(fr, aux)){
		if(aux == "	//s"){
			getVarNames(aux, fr, fw);
			continue;
		}
	
		fw << aux << endl;
	}
	fr.close();
	fw.close();
	return 0;
}
