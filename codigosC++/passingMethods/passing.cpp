#include <iostream>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

void swap(int &x, int &y)
{
	int temp;
	temp = x;
	x = y;
	y = temp;
}

int main()
{	
	int num1 = 10, num2 = 26565;

	cout << "The first number is: " << num1<< endl;
	cout << "The second number is: " << num2<< endl;

	swap(num1, num2);

	cout << "The first number is: " << num1<< endl;
	cout << "The second number is: " << num2<< endl;

	swap(num1, num2);

	cout << "The first number is: " << num1<< endl;
	cout << "The second number is: " << num2<< endl;
	
	return 0;
}