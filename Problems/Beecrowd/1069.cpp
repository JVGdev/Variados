#include <iostream>
#include <string>
#include <stack>

using namespace std;

void store(const char c, stack<char> &s, int &d){
	if(s.top() == '<' && c == '>'){
		d++;
		s.pop();
	}
	else{ s.push(c); }
}

int main(){
	string line;
	int n = 0;
	cin >> n;
	cin.ignore();
	stack<char> mem;

	mem.push('a');
	
	for(int a = 0; a < n; a++){
	
	int diamond = 0;
		
	getline(cin, line);	
	
	for(int i = 0; i < line.length(); i++){
		if(line[i] == '>') {
			store(line[i], mem, diamond);	

		} else if (line[i] == '<') {		
			store(line[i], mem, diamond);
		}
	}
	cout << diamond << endl;
	
	mem = stack<char>();
	mem.push('a');

	}
	
	return 0;
}
