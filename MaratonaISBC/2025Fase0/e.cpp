#include <iostream>
#include <numeric>

using namespace std;
/*long int gcd(long x, long y){
	if(x == 0) return 1;
	return gcd(y%x, y);
}*/

int main(){
	long y, k;
	long x = 1;
	cin >> y >> k;
	while(k--){
		/*
		//cout << x << " | " << k << endl;
		if(x < y) { x += gcd(y%x, x); }
		else if(x > y) x += gcd(x%y, y);
		else x += x;*/
		x += (x*y)/lcm(x, y);
	}
	cout << x << endl;
	return 0;
}

