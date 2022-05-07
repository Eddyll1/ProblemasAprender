#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
    int n;
    cout << "enter size"<< endl;
    cin >> n;
	int A[n];
    A[0]=2;
    //A[0]=12;
    //A[1]=15;
    //A[2]=25;
    //A[3]=12;

    for (int x:A)
    {
        cout << x<<endl;
    }
    
    //cout<<sizeof(A)<<"\n";
   // cout<<A[7]<<endl;
    //printf("%d\n",A[9]);
    
    return 0;    
}
