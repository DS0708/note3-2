#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h> 
#include "constructHaarMatrix2.c"
// #include <Windows.h>

typedef uint32_t DWORD;
typedef int32_t LONG;
typedef uint8_t BYTE;

// Windows.h에서 사용되는 비트맵 헤더 대신 다음 구조체를 사용
typedef struct __attribute__((packed)) {
    uint16_t bfType;
    uint32_t bfSize;
    uint16_t bfReserved1;
    uint16_t bfReserved2;
    uint32_t bfOffBits;
} BITMAPFILEHEADER;

typedef struct __attribute__((packed)) {
    uint32_t biSize;
    int32_t biWidth;
    int32_t biHeight;
    uint16_t biPlanes;
    uint16_t biBitCount;
    uint32_t biCompression;
    uint32_t biSizeImage;
    int32_t biXPelsPerMeter;
    int32_t biYPelsPerMeter;
    uint32_t biClrUsed;
    uint32_t biClrImportant;
} BITMAPINFOHEADER;


//비트맵 헤더를 한묶음으로
typedef struct tagBITMAPHEADER {
	BITMAPFILEHEADER bf;
	BITMAPINFOHEADER bi;
	//RGBQUAD hRGB[256]; //이 코드에서는 필요없음 (8bit에만 필요)
}BITMAPHEADER;

//비트맵을 읽어와서 화소정보의 포인터를 리턴
BYTE* loadBitmapFile(int bytesPerPixel, BITMAPHEADER* bitmapHeader, int* imgWidth, int*imgHeight, char* filename);

//비트맵 파일 쓰기
void writeBitmapFile(int bytesPerPixel, BITMAPHEADER outputHeader, BYTE* output, int imgSize, char* filename);


int main() {
	/*******************************************************************/
	/*************************** Read image  ***************************/
	/*******************************************************************/
	BITMAPHEADER originalHeader;	//비트맵의 헤더부분을 파일에서 읽어 저장할 구조체
	BITMAPHEADER outputHeader;		//변형을 가한 헤더부분을 저장할 구조체
	int imgSize, imgWidth, imgHeight;					//이미지의 크기를 저장할 변수
	int bytesPerPixel = 3;			//number of bytes per pixel (1 byte for R,G,B respectively)

	//BYTE* image = loadBitmapFile(bytesPerPixel, &originalHeader, &imgWidth, &imgHeight, "image_lena_24bit.bmp"); //비트맵파일을 읽어 화소정보를 저장 (불러들이는 이미지는 .c와 같은 폴더에 저장)
	//BYTE* image = loadBitmapFile(bytesPerPixel, &originalHeader, &imgWidth, &imgHeight, "highfrequency/high_frequency.bmp"); //고해상도 이미지
	BYTE* image = loadBitmapFile(bytesPerPixel, &originalHeader, &imgWidth, &imgHeight, "lowfrequency/low_frequency.bmp"); //저해상도 이미지
	if (image == NULL) return 0;

	imgSize = imgWidth * imgHeight; // total number of pixels
	BYTE* output = (BYTE*)malloc(bytesPerPixel * sizeof(BYTE) * imgSize);				//결과값을 저장할 포인터 선언 및 메모리 할당
	outputHeader = originalHeader;										//헤더정보를 출력헤더정보에 할당





	/*******************************************************************/
	/************************ Perform HWT/IHWT *************************/
	/*******************************************************************/
	//이미지 행렬 A 구성 (RGB값이 있으므로 픽셀당 값 하나씩만 읽어서 imgWidth x imgHeight 행렬 구성)
	int** A; //original image matrix
	A = (int**)malloc(sizeof(int*) * imgHeight);
	for (int i = 0; i < imgHeight; i++) {
		A[i] = (int*)malloc(sizeof(int) * imgWidth);
	}

	for (int i = 0; i < imgHeight; i++)
		for (int j = 0; j < imgWidth; j++)
			A[i][j] = image[(i*imgWidth+j)*bytesPerPixel];

	//printMatrixInt32X32(A,imgHeight,imgWidth,"A: Orginal image matrix");
	// printMatrixInt(A, imgHeight, imgWidth, "A: Original image matrix");

	//Haar matrix H 구성 (orthonormal column을 갖도록 구성)
	int n = imgHeight; //이미지가 정사각형(Height==Width)이라고 가정; n = 2^t,t=0,1,2,...
	double ** H = normalizeHaarMatrix(constructHaarMatrixRecursive(n),n);
	//printMatrixDouble32X32(H,n,n,"H");
	// printMatrix(H,n,n,"H");
	//...

	//HWT 수행: 행렬곱 B = H'*A*H
	double ** B = multiplyTwoSquareMatrices(transposeMatrix(H,n,n),multiplyTwoSquareMatrices(intToDoubleSquareMatrix(A,n),H,n),n);
	//printMatrixDouble32X32(B,n,n,"B");
	//printMatrix(B,n,n,"B");
	//...

	//행렬 B 자르기: B의 upper left corner(subsquare matrix)를 잘라 Bhat에 저장
	//Bhat은 B와 사이즈가 같으며 B에서 잘라서 저장한 부분 외에는 모두 0으로 채워짐
	int s = 6;
	int k = pow(2,s);
	double** B_HAT = cutSquareMatrix(B,n,k);
	// printMatrix(B_HAT,n,n,"B_HAT");
	//...
	
	//IHWT 수행: Ahat = H*Bhat*H'
	int** A_HAT = doubleToIntSquareMatrix(multiplyTwoSquareMatrices(multiplyTwoSquareMatrices(H,B_HAT,n),transposeMatrix(H,n,n),n),n);
	//...

	//printMatrixInt32X32(A,imgHeight,imgWidth,"A: Orginal image matrix");
	//printMatrixInt32X32(A_HAT,imgHeight,imgWidth,"A hat Matirx");


	/*******************************************************************/
	/******************* Write reconstructed image  ********************/
	/*******************************************************************/
	//Ahat을 이용해서 위의 image와 같은 형식이 되도록 구성 (즉, Ahat = [a b;c d]면 [a a a b b b c c c d d d]를 만들어야 함)
	BYTE* Are = (BYTE*) malloc(bytesPerPixel * sizeof(BYTE) * imgSize);

	for (int i = 0; i < imgHeight; i++) {
    	for (int j = 0; j < imgWidth; j++) {
        	int pixelValue = A_HAT[i][j];
       	 pixelValue = (pixelValue < 0) ? 0 : pixelValue;
       	 pixelValue = (pixelValue > 255) ? 255 : pixelValue;

      	  for (int k = 0; k < bytesPerPixel; k++) {
       	     Are[(i * imgWidth + j) * bytesPerPixel + k] = (BYTE)pixelValue;
      	  	}	
   	 	}
	}


	//...
	
	//writeBitmapFile(bytesPerPixel, outputHeader, Are, imgSize, "output7.bmp");
	//writeBitmapFile(bytesPerPixel, outputHeader, Are, imgSize, "highfrequency/output6.bmp");		//고해상도 Output image
	writeBitmapFile(bytesPerPixel, outputHeader, Are, imgSize, "lowfrequency/output6.bmp");	//저해상도 Output image


	free(image);
	free(output);
	for (int i = 0; i < imgHeight; i++)
		free(A[i]);
	free(A);
	free(Are);

	free(H);
	free(B);
	free(B_HAT);
	free(A_HAT);

	return 0;
}

BYTE* loadBitmapFile(int bytesPerPixel, BITMAPHEADER* bitmapHeader, int* imgWidth, int* imgHeight, char* filename)
{
	FILE* fp = fopen(filename, "rb");	//파일을 이진읽기모드로 열기
	if (fp == NULL)
	{
		printf("파일로딩에 실패했습니다.\n");	//fopen에 실패하면 NULL값을 리턴
		return NULL;
	}
	else
	{
		fread(&bitmapHeader->bf, sizeof(BITMAPFILEHEADER), 1, fp);	//비트맵파일헤더 읽기
		fread(&bitmapHeader->bi, sizeof(BITMAPINFOHEADER), 1, fp);	//비트맵인포헤더 읽기
		//fread(&bitmapHeader->hRGB, sizeof(RGBQUAD), 256, fp);	//색상팔렛트 읽기 (24bitmap 에서는 존재하지 않음)

		*imgWidth = bitmapHeader->bi.biWidth;
		*imgHeight = bitmapHeader->bi.biHeight;
		int imgSizeTemp = (*imgWidth) * (*imgHeight);	// 이미지 사이즈를 상위 변수에 할당

		printf("Size of image: Width %d   Height %d\n", bitmapHeader->bi.biWidth, bitmapHeader->bi.biHeight);
		BYTE* image = (BYTE*)malloc(bytesPerPixel * sizeof(BYTE) * imgSizeTemp);	//이미지크기만큼 메모리할당

		fread(image, bytesPerPixel*sizeof(BYTE), imgSizeTemp, fp);//이미지 크기만큼 파일에서 읽어오기

		fclose(fp);
		return image;
	}
}



void writeBitmapFile(int bytesPerPixel, BITMAPHEADER outputHeader, BYTE* output, int imgSize, char* filename)
{
	FILE* fp = fopen(filename, "wb");

	fwrite(&outputHeader.bf, sizeof(BITMAPFILEHEADER), 1, fp);
	fwrite(&outputHeader.bi, sizeof(BITMAPINFOHEADER), 1, fp);
	//fwrite(&outputHeader.hRGB, sizeof(RGBQUAD), 256, fp); //not needed for 24bitmap
	fwrite(output, bytesPerPixel*sizeof(BYTE), imgSize, fp);
	fclose(fp);
}



