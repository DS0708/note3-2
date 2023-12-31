#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "constructHaarMatrix2.c"

//functions for convenience
/*
double** allocateMemory(int m, int n); 
void releaseMemory(double** A, int m);
void printMatrix(double** A, int m, int n, char name[]);
*/

//functions to implement in prj0
//transposeMatrix, normalizeVector, calculateLength
//scaleMatrix, multiplyTwoMatrices, addTwoMatrices
void problem_2_b();



int main() {

	//Test Haar Matrix
	// int m = 3;
	// double** H;
	// double** H_T;
	// H = constructHaarMatrixRecursive(m);
	// printMatrix(H,m,m,"Haar Matirx");
	// releaseMemory(H, m);

	int n = 8;

	double** H = normalizeHaarMatrix(constructHaarMatrixRecursive(n),n);
	double** H_T = transposeMatrix(H,n,n);
	double** HXHT = multiplyTwoSquareMatrices(H,H_T,n);
	double** scale_Matirx = scaleMatrix(HXHT,n,n,3);

	printMatrix(H,n,n,"H");
	printMatrix(H_T,n,n,"H_T");
	printMatrix(HXHT,n,n,"HXHT");
	printMatrix(scale_Matirx,n,n,"H Scaled");


	releaseMemory(H, n);
	releaseMemory(H_T,n);
	releaseMemory(HXHT,n);
	releaseMemory(scale_Matirx,n);

	// double** A;
	// double** B;
	// double** C;
	// double** D;
	// double** E;
	// double** v; //vector
	// double** w;	//vector
	//int m = 3; 	//number of rows
	// int n = 10;	//number of columns

	/*
	//Test transposeMatrix
	A = allocateMemory(m,n);
	for (int i = 0; i < m; i++)
		for (int j = 0; j < n; j++)
			A[i][j] = (double) (i)*(j);
	printMatrix(A,m,n,"A");

	printf("\nB is A's transpose.");
	B = transposeMatrix(A,m,n);
	printMatrix(B,n,m,"B");

	//Test scaleMatrix
	printf("\nC is scaled with scalar 2.");
	C = scaleMatrix(A,m,n,2);
	printMatrix(C,m,n,"C");

	//Test multiplyTwoMatrices
	printf("\nD is A * B");
	D = multiplyTwoMatrices(A,m,n,B,n,m);
	if(D==NULL) printf("\nD is NULL\n");
	else printMatrix(D,m,m,"D");

	//Test AddTwoMatrices
	printf("\nE is A + C");
	E = addTwoMatrices(A,m,n,C,m,n);
	if(E==NULL) printf("\nE is NULL\n");
	printMatrix(E,m,n,"E");

	//Test normalizeVector
	v = allocateMemory(m,1);
	for (int i = 0; i < m; i++)
		v[i][0] = i;

	w = normalizeVector(v,m);
	printMatrix(v,m,1,"v");

	//Test calculateLength
	printf("\nv's length = %f\n", calculateLength(v,m));

	printMatrix(w,m,1,"v_normalized");

	problem_2_b();
	*/

	//release all the memory allocated
	// releaseMemory(A, m);
	// releaseMemory(B, n);
	// releaseMemory(C, m);
	// releaseMemory(D, m);
	// releaseMemory(E, m);
	// releaseMemory(v, m);
	// releaseMemory(w, m);

	return 0;
}


//functions for convenience
/*
double** allocateMemory(int m, int n) {
	double** A;
	A = (double**) malloc(sizeof(double*) * m);
	for (int i = 0; i < m; i++) {
		A[i] = (double*) malloc(sizeof(double) * n);
	}
	return A;
}


void releaseMemory(double** A, int m) {
	for (int i = 0; i < m; i++)
		free(A[i]);
	free(A);
}

void printMatrix(double** A, int m, int n, char name[]) {
	printf("\n%s = \n", name);
	for (int i = 0; i < m; i++) {
		for (int j = 0; j < n; j++)
			printf("%lf ", A[i][j]);
		printf("\n");
	}
}
*/

//functions to implement in prj0 	


void problem_2_b()
{
	int m = 2;
	int n = 2;
	double** A = allocateMemory(m,n);
	double** H = allocateMemory(m,n);
	double** H_Tilde = allocateMemory(m,n);
	double** B = allocateMemory(m,n);
	double** C = allocateMemory(m,n);
	double** temp = allocateMemory(m,1);
	double len ;

	A[0][0] = 1.0;
	A[0][1] = 2.0;
	A[1][0] = 3.0;
	A[1][1] = 4.0;

	H_Tilde[0][0] = 1.0;
	H_Tilde[0][1] = 1.0;
	H_Tilde[1][0] = 1.0;
	H_Tilde[1][1] = -1.0;

	printf("\nProblem 2-(b)\n");

	printMatrix(A,m,n,"A");
	printMatrix(H_Tilde,m,n,"H_Tilde");

	//normalize H_Tilde
	for(int i=0; i<n ; i++){
		for(int j=0; j<m ; j++){
			temp[j][0] = H_Tilde[j][i];
		}
		temp = normalizeVector(temp,m);
		for(int j=0; j<m ; j++){
			H[j][i] = temp[j][0];
		}
	}

	printMatrix(H,m,n,"H");

	B = multiplyTwoMatrices(transposeMatrix(H,m,n),n,m,multiplyTwoMatrices(A,m,n,H,m,n),m,n);
	printMatrix(B,m,n,"B");

	C = multiplyTwoMatrices(multiplyTwoMatrices(H,m,n,B,m,n),m,n,transposeMatrix(H,m,n),n,m);
	printMatrix(C,m,n,"C");

	releaseMemory(A,m);
	releaseMemory(H_Tilde,m);
	releaseMemory(H,m);
	releaseMemory(B,m);
	releaseMemory(C,m);
	releaseMemory(temp,m);
}




