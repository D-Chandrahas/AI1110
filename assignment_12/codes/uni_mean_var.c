#include <stdio.h>

int main(){
	FILE* file1 = fopen("uni.dat","r");
	
	double sum = 0.0;
	double current = 0.0;
	
	while(fscanf(file1,"%lf",&current)!=-1){
		sum += current;
	}
	
	double mean = sum/1000000.0;
	printf("mean = %f\n",mean);
	fclose(file1);
	
	sum = 0.0;
	file1 = fopen("uni.dat","r");
	
	while(fscanf(file1,"%lf",&current)!=-1){
		sum += (current-mean)*(current-mean);
	}
	
	double var = sum/1000000.0;
	printf("variance = %f",var);
	fclose(file1);
	
	return 0;
}