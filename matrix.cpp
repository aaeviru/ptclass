#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include "travedir.h"

using namespace std;

vector<string> word;
FILE* fout;
#define WORDLIST "/home/ec2-user/git/statresult/wordslist_dsw.txt"


int matrix(const char *path) {
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
                //if(_dirName.at(_dirName.length()-1) == 'f' && _dirName.at(_dirName.length()-7) == 'q'){//for tfidf
					 if(_dirName.at(_dirName.length()-1) == 'q'){//for normal

                        char term[200];
                        //double tmpnum;//for tfidf
								int tmpnum;//for normal
                        FILE* fp = NULL;
								//map<string,double> vec;//for tfidf
								//map<string,double>::iterator it;//for tfidf
								map<string,int> vec;//for normal
								map<string,int>::iterator it;//for normal

                        fp = fopen(fullDirPath.c_str(),"r");

                        printf("%s\n",fullDirPath.c_str());
                        //while(fscanf(fp,"%s %lf",term,&tmpnum) != EOF){//for tfidf
								while(fscanf(fp,"%s %d",term,&tmpnum) != EOF){//for normal

									vec[string(term)] = tmpnum;
                        }
                        vector<string>::iterator word_it;
                        for(word_it=word.begin();word_it!=word.end();++word_it){
                                it = vec.find(*word_it);
				if(it != vec.end()){
					//fprintf(fout,"%lf ",it->second);//for tfidf
					fprintf(fout,"%d ",it->second);//for normal

				}else{
					fprintf(fout,"0 ");
				}
                        }
			fprintf(fout,"\n");
                        fclose(fp);
                }

        } else {
            if (strcmp(ent->d_name, ".") == 0 || strcmp(ent->d_name, "..") == 0) {
                continue;
            }
            //directory  
            string _path(path);
            string _dirName(ent->d_name);
            string fullDirPath = _path + "/" + _dirName;
            if(matrix(fullDirPath.c_str()) < 0)
                return -1;
        }
    }
    closedir(pDir);
    return 0;
}



int main(int argc,char** argv){
	if(argc != 3){
		printf("input:classfile-folder output-file\n");
		return -1;
	}else
		printf("wordlist:%s\n",WORDLIST);
	
   char term[200];
   FILE* fp = NULL;
   fp = fopen(WORDLIST,"r");
   while(fscanf(fp,"%s\n",term) != EOF){
      word.push_back(string(term));
   }
   fclose(fp);

   fout = fopen(argv[2],"w");
	//matrix.txt for normal
	//matrix-tfidf uses tfidf instead of tf
   matrix(argv[1]);
   fclose(fout);
   printf("over\n");
}
