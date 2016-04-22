#include <stdio.h>  
#include <dirent.h>  
#include <sys/types.h>  
#include <sys/stat.h>  
#include <string>  
#include <string.h>  
//#include <iostream>
#include <vector>
#define OUTPATH "/mnt/nas2a/ko/classinfobak/"
using namespace std;
int totalnum;

int classf(const char* path){
	FILE *fp = fopen(path,"r");
	char buff[1000],*filebuff,opfile[500];
	long lSize;size_t result;
	snprintf(opfile,500,"%s.fq",path);
//	printf("%s\n",opfile);
	FILE *fin = fopen(opfile,"r");
	fseek (fin , 0 , SEEK_END);
	lSize = ftell (fin);
  	rewind (fin);
//	printf("%d\n",lSize);
  	// allocate memory to contain the whole file:
  	filebuff = (char*) malloc (sizeof(char)*lSize);
	if (filebuff == NULL) {fputs ("Memory error\n",stderr); exit (2);}
  	// copy the file into the buffer:
  	result = fread (filebuff,1,lSize,fin);
  	if (result != lSize) {fputs ("Reading error\n",stderr); exit (3);}

  	/* the whole file is now loaded in the memory buffer. */

  	// terminate
	fclose(fin);
	char class1,class3;
        int class2,class4,class5,check = 0;
	while( fgets(buff,1000,fp) != NULL){
		if(buff[1] == '5' && buff[2] == '1'){
			while( fgets(buff,1000,fp) != NULL){
				if(buff[0] == ' '){
					if(strlen(buff) < 9){
						printf("%s\n%s\n",path,buff);
						return -1;
					}
					char tmp = buff[3];
					//sscanf(buff," %c",&tmp);
					if(tmp >= 'A' && tmp <= 'Z')
						sscanf(&buff[3],"%c%d%c %d/%d",&class1,&class2,&class3,&class4,&class5);
					else
						continue;
					if(class1 - 'A' >= 8 || class2 >= 100 || class3 - 'A' >= 30){
						printf("%s\n%c%d%c %d/%d\n",path,class1,class2,class3,class4,class5);
						return -1;
					}
					if(class1 - 'A' < 0 || class2 < 0 || class3 - 'A' < 0 ){
                                                printf("%s\n%c%d%c %d/%d\n",path,class1,class2,class3,class4,class5);
                                                return -1;
                                        }
					check = 1;
                                        snprintf(opfile,50,"%s%c%d%c.txt",OUTPATH,class1,class2,class3);
                                        FILE* fout = fopen(opfile,"a");
					fwrite(filebuff,lSize,1,fout);
					fclose(fout);

				}else{
					fclose(fp);
					free (filebuff);
					if(check == 1)
						totalnum++;
					return 0;
				}
				
			}
		}
	}
	fclose(fp);
	free (filebuff);
	if(check == 1)
        	totalnum++;
	return 0;
}  
int List(const char *path) {  
    //printf("%s\n",path);
    struct dirent* ent = NULL;  
    DIR *pDir;  
    pDir = opendir(path);  
    if (pDir == NULL) {  
        //被当作目录，但是执行opendir后发现又不是目录，比如软链接就会发生这样的情况。  
        return 0;  
    }  
    while (NULL != (ent = readdir(pDir))) {  
        if (ent->d_type == 8) {  
            	//file  
		string _path(path);
            	string _dirName(ent->d_name);
            	string fullDirPath = _path + "/" + _dirName;
		if(_dirName.at(_dirName.length()-1) == 't')
		//	printf("%s\n",ent->d_name);
			if(classf(fullDirPath.c_str()) < 0)
				return -1;
		//getchar(); 
        } else {  
            if (strcmp(ent->d_name, ".") == 0 || strcmp(ent->d_name, "..") == 0) {  
                continue;  
            }  
            //directory  
            string _path(path);  
            string _dirName(ent->d_name);  
            string fullDirPath = _path + "/" + _dirName;  
            if(List(fullDirPath.c_str()) < 0)
		return -1;  
        }  
    }  
    closedir(pDir);
    return 0;
}  
int main(int argc, char *argv[]) {  
	//memset(vec,'\0',sizeof(vec));
  	totalnum = 0;
    	List(argv[1]); 
/*
 	int tmp1,tmp2,tmp3,tmp4;
	int max1 = 0,max2 = 0,max3 = 0,max4 = 0;
	int num1 = 0,num2 = 0,num3 = 0,num4 = 0;
	int total = 0;
	for(int i=0;i<8;i++){
		tmp1 = 0;
		for(int j=0;j<100;j++){
			tmp2 = 0;
			for(int k=0;k<30;k++){
				if(vec[i][j][k] > 0){
					//printf("%c%d%c %d/%d:%d\n",i+'A',j,k+'A',l,m,vec[i][j][k][l][m]);
					if(vec[i][j][k] >max3)
						max3 = vec[i][j][k];
					tmp2 += vec[i][j][k];
					num3++;
				}
			}
			if(tmp2 > 0){
				//printf("%c%d:%d\n",i+'A',j,tmp2);
				tmp1 += tmp2;
				num2++;
				if(tmp2 > max2)
					max2 = tmp2;
			}
		}
		if(tmp1 > 0){
                	printf("%c:%d\n",i+'A',tmp1);
			num1++;
			total += tmp1;
			if(tmp1 > max1)
				max1 = tmp1;
		}

	}
	printf("max1:%d max2:%d max3:%d\n",max1,max2,max3);
	printf("num1:%d num2:%d num3:%d%d\n",num1,num2,num3);
*/
	printf("totalnum:%d\n",totalnum);
//	printf("%lf %lf %lf\n",1.0*total/num1,1.0*total/num2,1.0*total/num3);
    	return 0;  
}  
