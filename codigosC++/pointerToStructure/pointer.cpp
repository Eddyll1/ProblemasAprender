#include <iostream>
#include <stdio.h>
#include <stdlib.h>


using namespace std;

struct Rectangle
{
	int length;
	int breadth;
};

int main()
{
	// Rectangle r={10,5};
	// cout << r.length << endl;
	// cout << r.breadth << endl;

	// Rectangle *p = &r;

	Rectangle *p;
	p = new Rectangle;

	p -> length = 15;
	p-> breadth = 10;

	
	cout << p-> length << endl;
	cout << p-> breadth << endl;

	return 0;
}