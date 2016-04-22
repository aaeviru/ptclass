#include "travedir.h"
#include <iostream>
#include <stdio.h>
#include <set>
#include <string>
using namespace std;

set<string> word;
set<string> stopword;

int wordlist(const char *path) {
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
                if(_dirName.at(_dirName.length()-1) == 'q'){
			char term[100];
                        int tmpnum;
      			FILE* fp = NULL;
      			fp = fopen(fullDirPath.c_str(),"r");
      			printf("%s\n",fullDirPath.c_str());
      			while(fscanf(fp,"%s %d",term,&tmpnum) != EOF){
                                if(stopword.find(string(term)) != stopword.end()) continue;
         			word.insert(string(term));
      			}
/*
      			set<string>::iterator word_it;
      			for(word_it=word.begin();word_it!=word.end();++word_it){
         			cout<<*word_it<<endl;
      			}
*/
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
            if(wordlist(fullDirPath.c_str()) < 0)
                return -1;
        }
    }
    closedir(pDir);
    return 0;
}

int main(){
        char term[100];
        int tmpnum;
        FILE* fp = NULL;
        fp = fopen("/mnt/nas2a/ko/stopword2.txt","r");
        while(fscanf(fp,"%s %d",term,&tmpnum) != EOF){
        	stopword.insert(string(term));
        }
        fclose(fp);

        fp = fopen("/mnt/nas2a/ko/onlyonce.txt","r");
        while(fscanf(fp,"%s",term) != EOF){
                stopword.insert(string(term));
        }
        fclose(fp);

	wordlist("/mnt/nas2a/ko/classinfo/");
	set<string>::iterator word_it;
        fp = fopen("/home/ko/class/result/wordslist.txt","w");
	for(word_it=word.begin();word_it!=word.end();++word_it){
        	fprintf(fp,"%s\n",word_it->c_str());
        }
	fclose(fp);
	cout<<word.size()<<endl;
   	return 0;
}
