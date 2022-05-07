#include <iostream>
#include <stdio.h>
#include <stdlib.h>

using namespace std;


struct  Rectangle
{
    int length;
    int breadth;
};
int main()
{
    //int a = 10;
    //int *p = &a;
    
    //cout << a << endl;
    //cout << p << endl;
    //cout << *p << endl;
    //cout << &a << endl;

    // int A[5] = {2,4,6,8,10};
    //cout << A << endl;
    int *p;
    p = new int [5];
    //p=A;
    
    p = (int *)malloc(5*sizeof(int));
    p[0] = 10; p[1]=15; p[2]=25; p[3]=36; p[4]=40;
    cout << *p << endl;


    for (int i= 0; i<5; i++)
    {
        cout << p[i]<< endl;
    };
    delete [] p;
    //free(p);


    int *p1;
    char *p2;
    float *p3;
    double *p4;
    struct Rectangle *p5;


    cout << sizeof(p1)<< endl;
    cout << sizeof(p2)<< endl;
    cout << sizeof(p3)<< endl;
    cout << sizeof(p4)<< endl;
    cout << sizeof(p5)<< endl;

    return 0;
}
