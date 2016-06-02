#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fstream>
#include <iomanip>
#include <map>
#include<iostream>
using namespace std;
map<string, string> optable;
map<string, string>::iterator iter;
map<string, int> locTable;
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
	if (isOpcode(s)==true){// 代表這一行只有2個token
		loc[locPtr]=loc[locPtr-1]+3;
		string tmp(s);
		locTable[tmp]=loc[locPtr];
		locPtr++;
	}
	else{ // 代表這一行有3個token
		char *label = s;
		char *opcode = strtok(NULL, del);
		char *operand = strtok(NULL, del);
		int intord=0;
		string tmp(label);
		if(strcmp(opcode,"WORD")==0){
			loc[locPtr]=loc[locPtr-1]+3;
			locTable[tmp]=loc[locPtr];
			locPtr++;
		}
		else if(strcmp(opcode,"RESW")==0){
			intord=atoi(operand);
			loc[locPtr]=loc[locPtr-1]+3*intord;
			locTable[tmp]=loc[locPtr];
			locPtr++;
		}
		else if(strcmp(opcode,"RESB")==0){
			intord=atoi(operand);
			loc[locPtr]=loc[locPtr-1]+intord;
			locTable[tmp]=loc[locPtr];
			locPtr++;
		}
		else if(strcmp(opcode,"BYTE")==0){
			// cout << operand[0];
			if(operand[0]=='X'){
				loc[locPtr]=loc[locPtr-1]+1;
			}
			else{
				intord = strlen(operand)-4-3;
				loc[locPtr]=loc[locPtr-1]+intord;
			}
			locTable[tmp]=loc[locPtr];
			locPtr++;				
		}
		else if(strcmp(label,"FIRST")==0){
			loc[locPtr]=loc[locPtr-1];
			locPtr++;
		}
		else if (isOpcode(opcode)==true){
			loc[locPtr]=loc[locPtr-1]+3;
			locTable[tmp]=loc[locPtr];
			locPtr++;
		}
		
		else{
			cout <<opcode<<" "<<isOpcode(opcode)<<":"<< "Syntax error !"<<endl;
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
		int hex;
		sscanf(s,"%x",&hex);
		loc[locPtr++]=hex;// start of location.
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
	{	
		cout <<hex<< loc[i]<<endl;
	}
	cout << ":::" << locTable["CLOOP"];
  	return 0;
}
