#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include "travedir.h"

using namespace std;

vector<string> word;
FILE* fout;

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
                if(_dirName.at(_dirName.length()-1) == 'q'){//filename pattern
                        char term[200];
                        int tmpnum;
                        FILE* fp = NULL;
			map<string,int> vec;
			map<string,int>::iterator it;
                        fp = fopen(fullDirPath.c_str(),"r");
                        printf("%s\n",fullDirPath.c_str());
                        while(fscanf(fp,"%s %d",term,&tmpnum) != EOF){
				vec[string(term)] = tmpnum;
                        }
                        vector<string>::iterator word_it;
                        for(word_it=word.begin();word_it!=word.end();++word_it){
                                it = vec.find(*word_it);
				if(it != vec.end()){
					fprintf(fout,"%d ",it->second);
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



int main(){
   char term[200];
   FILE* fp = NULL;
   fp = fopen("/home/ec2-user/git/statresult/wordslist_dsw.txt","r");
   while(fscanf(fp,"%s\n",term) != EOF){
      word.push_back(string(term));
   }
   fclose(fp);

   fout = fopen("/home/ec2-user/data/classinfo/matrix.txt","w");
   matrix("/home/ec2-user/data/classinfo/");
   fclose(fout);
   printf("over\n");
}
