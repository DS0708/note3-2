/**********************************************
- written by H. Lee 10/25/2022 
**********************************************/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
// #include "matOperations.c"


double** constructHaarMatrixRecursive(int n);
double** constructHaarMatrixRecursive2(int n);
double** constructHaarMatrixRecursive512(int n);
double** concatenateTwoMatrices(double** hl, double** hr, int n);
double** applyKroneckerProduct(double** A, int n, double a, double b);

void printMatrix(double** A, int m, int n, char name[]); 
void printMatrixInt(int** A, int m, int n, char name[]);
void printMatrixInt32X32(int** A, int m, int n, char name[]);
void printMatrixDouble32X32(double** A, int m, int n, char name[]);
double** constructIdentity(int k); 
double** allocateMemory(int m, int n); 
void releaseMemory(double** A, int m);

double** normalizeHaarMatrix(double** H, int n); 
double** multiplyTwoMatrices(double** A, int m, int n, double** B, int l, int k);
double** multiplyTwoSquareMatrices(double** A, double** B, int n);
double** transposeMatrix(double** A, int m, int n);
double** normalizeVector(double** v, int n);
double calculateLength(double** v, int m);
double** scaleMatrix(double** A, int m, int n,int c);
double** addTwoMatrices(double** A, int m, int n, double** B, int l, int k);
double** addFourMatrices(double** A, double** B, double** C, double** D, int m, int n);
double** intToDoubleSquareMatrix(int** A, int m);
int** doubleToIntSquareMatrix(double** A, int m);
double** cutSquareMatrix(double** A, int m, int k);

/*
int main() {
	int n = 8;

	double** H = constructHaarMatrixRecursive(n);

	printMatrix(H,n,n,"H");

	releaseMemory(H, n);

	//double** I = constructIdentity(n);
	//printMatrix(I,n,n,"I");
	//releaseMemory(I, n);
}
*/

double** cutSquareMatrix(double** A, int m, int k) {
    if (k > m) {
        return A;
    }

    double** result = allocateMemory(m, m);

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < m; j++) {
            if (i < k && j < k) {
                result[i][j] = A[i][j]; // 처음 k x k 부분은 원래 값으로 유지
            } else {
                result[i][j] = 0.0; // 나머지 부분은 0으로 채움
            }
        }
    }

    return result;
}


double** intToDoubleSquareMatrix(int** A, int m) {
    double** B = allocateMemory(m, m);
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < m; j++) {
            B[i][j] = (double)A[i][j];
        }
    }
    return B;
}

int** doubleToIntSquareMatrix(double** A, int m) {
    int** B = (int**)malloc(sizeof(int*) * m);
    for (int i = 0; i < m; i++) {
        B[i] = (int*)malloc(sizeof(int) * m);
    }
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < m; j++) {
            B[i][j] = (int)A[i][j];
        }
    }
    return B;
}




double** constructHaarMatrixRecursive(int n) {
	double** h;
	if (n > 2)
		h = constructHaarMatrixRecursive(n/2);
	else {
		//double** h;
		h = allocateMemory(2,2);
		h[0][0] = 1; h[0][1] = 1; h[1][0] = 1; h[1][1] = -1; //H = [1 1; 1 -1]
		return h; 
	}

	// construct the left half (Kronecket product of h and [1;1])
	double** Hl = applyKroneckerProduct(h, n, 1, 1);
	releaseMemory(h, n/2);

	// construct the right half (Kronecker product of I and [1;-1])
	double** I = constructIdentity(n/2);
	double** Hr = applyKroneckerProduct(I, n, 1, -1); 
	releaseMemory(I, n/2);


	// merge hl and hr
	double** H = concatenateTwoMatrices(Hl, Hr, n); //H = [Hl Hr]
	releaseMemory(Hl, n);
	releaseMemory(Hr, n);

	return H;
}

double** constructHaarMatrixRecursive2(int n) {
    double** h;
    if (n > 2)
        h = constructHaarMatrixRecursive(n / 2);
    else {
        h = (double**)malloc(sizeof(double*) * 2);
        for (int i = 0; i < 2; i++) {
            h[i] = (double*)malloc(sizeof(double) * 2);
        }
        h[0][0] = 1.0; h[0][1] = 1.0; h[1][0] = 1.0; h[1][1] = -1.0; // H = [1 1; 1 -1]
        
        // Normalize the matrix by dividing all elements by sqrt(2).
        double norm = sqrt(2.0);
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 2; j++) {
                h[i][j] /= norm;
            }
        }
        return h;
    }

    // construct the left half (Kronecker product of h and [1;1])
    double** Hl = applyKroneckerProduct(h, n, 1.0, 1.0);

    // construct the right half (Kronecker product of I and [1;-1])
    double** I = constructIdentity(n / 2);
    double** Hr = applyKroneckerProduct(I, n, 1.0, -1.0);

    // merge hl and hr
    double** H = concatenateTwoMatrices(Hl, Hr, n);

    return H;
}

double** constructHaarMatrixRecursive512(int n) {
    double** h = allocateMemory(n, n);

    if (n == 2) {
        h[0][0] = 1.0;
        h[0][1] = 1.0;
        h[1][0] = 1.0;
        h[1][1] = -1.0;

        // 정규화: 모든 요소를 sqrt(2.0)로 나눠줍니다.
        double norm = sqrt(2.0);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                h[i][j] /= norm;
            }
        }
    } else {
        // 크기가 2x2 이 아닌 경우, 재귀적으로 Haar 행렬을 구성합니다.
        double** h_sub = constructHaarMatrixRecursive512(n / 2);
        double** I = constructIdentity(n / 2);

        // 왼쪽 절반 (Kronecker product of h_sub and [1; 1])
        double** Hl = applyKroneckerProduct(h_sub, n, 1.0, 1.0);
        releaseMemory(h_sub, n / 2);

        // 오른쪽 절반 (Kronecker product of I and [1; -1])
        double** Hr = applyKroneckerProduct(I, n, 1.0, -1.0);
        releaseMemory(I, n / 2);

        // 두 부분을 합치기
        h = concatenateTwoMatrices(Hl, Hr, n);
        releaseMemory(Hl, n);
        releaseMemory(Hr, n);
    }

    return h;
}




double** applyKroneckerProduct(double** A, int n, double a, double b) {
	double** h = allocateMemory(n, n/2);
	
	for (int j = 0; j < n/2; j++) {
		for (int i = 0; i < n/2; i++) {
			h[2*i][j] = A[i][j] * a;
			h[2*i+1][j] = A[i][j] * b;
		}
	}
	return h;
}

double** concatenateTwoMatrices(double** hl, double** hr, int n) {
	double** H = allocateMemory(n, n);

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (j < n/2)
				H[i][j] = hl[i][j];
			else
				H[i][j] = hr[i][j-n/2];
		}
	}
	return H; 
}


void printMatrix(double** A, int m, int n, char name[]) {
	printf("\n%s = \n", name);
	for (int i = 0; i < m; i++) {
		for (int j = 0; j < n; j++)
			printf("%lf ", A[i][j]);
		printf("\n");
	}
}

void printMatrixInt(int** A, int m, int n, char name[]) {
    printf("\n%s = \n", name);
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++)
            printf("%d ", A[i][j]);
        printf("\n");
    }
}

void printMatrixInt32X32(int** A, int m, int n, char name[]) {
    printf("\n%s (First 8x8) = \n", name); // 처음 32 부분만 출력
    int maxRows = (m > 32) ? 32 : m; // 최대 32행까지 출력
    int maxCols = (n > 32) ? 32 : n; // 최대 32열까지 출력

    for (int i = 0; i < maxRows; i++) {
        for (int j = 0; j < maxCols; j++) {
            printf("%d ", A[i][j]);
        }
        printf("\n");
    }
}

void printMatrixDouble32X32(double** A, int m, int n, char name[]) {
    printf("\n%s (First 32x32) = \n", name); // 처음 32x32 부분만 출력
    int maxRows = (m > 32) ? 32 : m; // 최대 32행까지 출력
    int maxCols = (n > 32) ? 32 : n; // 최대 32열까지 출력

    for (int i = 0; i < maxRows; i++) {
        for (int j = 0; j < maxCols; j++) {
            printf("%lf ", A[i][j]);
        }
        printf("\n");
    }
}



double** constructIdentity(int k) {
 	double** I = allocateMemory(k,k);

 	for (int i = 0; i < k; i++) {
 		for (int j = 0; j < k; j++) {
 			if (i != j)
 				I[i][j] = 0.0;
 			else
 				I[i][j] = 1.0;
 		}
 	}
 	return I;
}

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

// float** constructIdentity(int k) {
// 	float** I;
// 	I = (float**)malloc(sizeof(float*) * k);
// 	for (int i = 0; i < k; i++)
// 		I[i] = (float*)malloc(sizeof(float*) * k);

// 	for (int i = 0; i < k; i++) {
// 		for (int j = 0; j < k; j++) {
// 			if (i != j)
// 				I[i][j] = 0.0;
// 			else
// 				I[i][j] = 1.0;
// 		}
// 	}

// 	return I;
// }
	
double** normalizeHaarMatrix(double** H, int n) {
    double** normalized_H = allocateMemory(n, n);

    for (int j = 0; j < n; j++) {
        double length = 0.0;
        for (int i = 0; i < n; i++) {
            length += H[i][j] * H[i][j];
        }
        length = sqrt(length);

        for (int i = 0; i < n; i++) {
            normalized_H[i][j] = H[i][j] / length;
        }
    }

    return normalized_H;
}

double **multiplyTwoMatrices(double **A, int m, int n, double **B, int l, int k)
{	
	if (n != l) return NULL;

	double** C = allocateMemory(m,k);

	for(int i=0 ; i<m ; i++){
		for (int j=0 ; j<k ; j++){
			for(int k=0; k<n ; k++){
				C[i][j] += A[i][k] * B[k][j];
			} 
		}
	}

    return C;
}

double** multiplyTwoSquareMatrices(double** A, double** B, int n){
	return multiplyTwoMatrices(A,n,n,B,n,n);
}

double** transposeMatrix(double **A, int m, int n) {
	double** B = allocateMemory(n, m);

	for (int i = 0; i < m; i++)
		for (int j = 0; j < n; j++)
			B[j][i] = A[i][j];	
	
	return B;
}

double** normalizeVector(double** v, int m) {
	double** w;
	double len = 0.0;

	for (int i = 0; i < m; i++)
		len += v[i][0]*v[i][0];	
	len = sqrt(len);

	w = allocateMemory(m,1);
	for (int i = 0; i < m; i++)
		w[i][0] = v[i][0]/len;
	
	return w;
}

double calculateLength(double **v, int m)
{	
	double len = 0.0;

	for (int i=0; i<m ; i++){
		len += v[i][0]*v[i][0];
	}

    return sqrt(len);
}

double **scaleMatrix(double **A, int m, int n, int c)
{	
	double** B = allocateMemory(m, n);

	for (int i = 0; i < m; i++)
		for (int j = 0; j < n; j++)
			B[i][j] = A[i][j]*c;	
	
	return B;
}


double **addTwoMatrices(double **A, int m, int n, double **B, int l, int k)
{
	if (m!=l || n!=k) return NULL;

	double** C = allocateMemory(m,k);

	for(int i=0; i<m ; i++){
		for(int j=0; j<n ; j++){
			C[i][j] = A[i][j] + B[i][j];
		}
	}

    return C;
}

double** addFourMatrices(double** A, double** B, double** C, double** D, int m, int n) {
    double** result = allocateMemory(m, n);

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            result[i][j] = A[i][j] + B[i][j] + C[i][j] + D[i][j];
        }
    }

    return result;
}

