#include <stdio.h>
#include <math.h>

int main(){
	FILE* file1 = fopen("uni.dat","r");
	FILE* file2 = fopen("v_samples.dat","w");
	
	double sample = 0.0;
	
	while(fscanf(file1,"%lf",&sample)!=-1){
		fprintf(file2,"%f\n",-2*log(1-sample));
	}
	
	fclose(file1);
	fclose(file2);
	
	return 0;
}