#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fstream>
#include <map>
#include<iostream>
using namespace std;
map<string, string> optable;
map<string, string>::iterator iter;
int loc[1000]={0};
int locPtr=0;
const char *del = " ";
void build_lable();
bool isOpcode(string s);
void CalLoc(string s);

bool isOpcode(char *s){
	string opStr(s);// cast char into string type
	iter = optable.find(opStr);
	if(iter == optable.end()){
        return false;
	}
	return true;
}

void CalLoc(char *s){
	if (isOpcode(s)==true){
		// printf("%d ", locPtr);
		loc[locPtr]=loc[locPtr-1]+3;
		locPtr++;
		// printf(" %d\n", loc[locPtr]);
	}
	else{
		char *label = s;
		char *opcode = strtok(NULL, del);
		char *operand = strtok(NULL, del);
		int intord=0;
		if(strcmp(opcode,"WORD")){
			loc[locPtr]=loc[locPtr-1]+3;
			locPtr++;
		}
		else if(strcmp(opcode,"RESW")){
			intord=atoi(operand);
			loc[locPtr]=loc[locPtr-1]+3*intord;
			locPtr++;
			cout << s <<","<<locPtr-1<<","<<loc[locPtr-1]<<endl;
		}
	}
}
void build_lable(){
	string inputstream;
	ifstream inputfile ( "input.txt" , ifstream::in );
	getline(inputfile, inputstream);
	char tmp[20];
	strcpy(tmp, inputstream.c_str());
	char *s = strtok(tmp, del);
	s = strtok(NULL, del);
	if( strcmp(s,"START")==0){
		s = strtok(NULL, del);
		loc[locPtr++]=atoi(s);// start of location.
	}
	else{
		loc[locPtr++]=0;
	}
	while (getline(inputfile , inputstream))
	{
		tmp[30];
		strcpy(tmp, inputstream.c_str());//c_str can cast type string into char type
		char *s = strtok(tmp, del);
		if(strcmp(s,"END")!=0){// will continue parsing until "END"
			if(strcmp(s,".")!=0){
				CalLoc(s);
			}
		}
	}
	inputfile.close();
}

int main() {
    string opcodestr;
	ifstream ifs2 ( "opcode.txt" , ifstream::in );
	while (getline(ifs2 , opcodestr))
	{
		// cout << opcodestr << endl;
		char tmp[20];
		strcpy(tmp, opcodestr.c_str());//c_str can cast type string into char type
		///////// function strtok is StringTokenizer in C++ ////////
		char *s = strtok(tmp, del);
		while(s != NULL) {
		  	char *key = s;
		  	s = strtok(NULL, del);
		  	char *value = s;
		  	s = strtok(NULL, del);
		  	string keyString(key);// cast char into string type
		  	string valueString(value);
		  	optable[keyString] = valueString;
		}
		//////////////////
	}
	ifs2.close();
	///////////////// build optable finish ! /////////////////////
	build_lable();
	for (int i = 0; i < locPtr; ++i)
	{	if(loc[i]>10000){
			printf("%d--", i);
		}
		cout << loc[i]<<endl;
	}
  	return 0;
}
