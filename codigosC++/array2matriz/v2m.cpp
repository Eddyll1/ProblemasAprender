#include <iostream>		
#include <stdio.h>
#include <stdlib.h>

using namespace std;


void amatriz(float &vector, float matriz[][], int col);

int main()
{
	int A[2][2]= {
		{2,5},
		{6,4}
	};
	cout << A << endl; 	
	return 0;
}