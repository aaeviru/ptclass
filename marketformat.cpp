#include "marketformat.h"

using namespace std;

map<string,int> word;

int marketf(const char* path){
   FILE* fin = fopen(path,"r");
   char opfile[100];
   snprintf(opfile,100,"%s.dat",path);
   FILE* fout = fopen(opfile,"w");
   char buff[1000];
   fgets(buff,1000,fin);
   //no = 1;
   while( fgets(buff,1000,fin) != NULL){
      char term[200];
      //no++;
      //printf("%d\n",no);
      //fflush(stdout);
      int fq,wordid;
      if(buff[0] == '@'){
         fprintf(fout,"\n");
         continue;
      }
      sscanf(buff,"%d %s",&fq,term);
      wordid = word[string(term)];
      fprintf(fout,"%d ",wordid);
   }
   fprintf(fout,"\n");
   fclose(fin);
   fclose(fout);
   printf("%s\n",path);
   fflush(stdout);
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
                if(_dirName.at(_dirName.length()-2) == 'x')
                //      printf("%s\n",ent->d_name);
                        if(marketf(fullDirPath.c_str()) < 0)
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


int main(int argc, char *argv[]){
   FILE* fword = fopen("result/wordslist.txt","r");
   char term[200];
   int no = 0;
   while(fscanf(fword,"%s",term) != EOF){
      word[string(term)] = no;
      no++;
   }
   printf("read over\n");
   fclose(fword);
   List(argv[1]);
   return 0;
}
