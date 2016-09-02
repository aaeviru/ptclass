#include "acp.h"

double edist(vector<double> a,vector<double> b){
	double sum = 0;
	for(int i =0;i<a.size();i++){
		sum += (a[i]-b[i]) * (a[i]-b[i]);
	}
	return sqrt(sum);
}

double norm(vector<double> a){
	for(int i =0;i<a.size();i++){
		sum += a[i] *a[i];
	}
	return sqrt(sum);

}
int main(int argc,char** argv){

	return 0;
}
