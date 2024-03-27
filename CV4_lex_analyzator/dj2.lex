/*** Definition Section has one variable
which can be accessed inside yylex() 
and main() ***/
%{
int integerCount = 0;
int floatCount = 0;
int operationCount = 0;
int commaCount = 0;
int leftBracketCount = 0;
int rightBracketCount = 0;
%}
 
/*** Rule Section ***/
%%
[1-9][0-9]*|0               { printf("INTEGER: %s\n", yytext); integerCount++; }
[1-9][0-9]*\.[0-9]*[1-9]    { printf("FLOAT: %s\n", yytext); floatCount++; }
[1-9][0-9]*\.0              { printf("FLOAT: %s\n", yytext); floatCount++; }
[+*/~]                      { printf("OPERATION: %s\n", yytext); operationCount++; }
,                           { printf("COMMA\n"); commaCount++; }
\(                          { printf("LEFT_BRACKET\n"); leftBracketCount++; }
\)                          { printf("RIGHT_BRACKET\n"); rightBracketCount++; }
[ \t\n]   ;                 // Ignore whitespace
.                           { printf("Invalid character: %s\n", yytext); }
%%
 
/*** Code Section prints the counts ***/
int yywrap(){}
int main(){
 
// Explanation:
// yywrap() - wraps the above rule section
/* yyin - takes the file pointer 
          which contains the input*/
/* yylex() - this is the main flex function
          which runs the Rule Section*/
// yytext is the text in the buffer
 
// Uncomment the lines below 
// to take input from file
FILE *fp;
char filename[50];
printf("Enter the filename: \n");
scanf("%s",filename);
fp = fopen(filename,"r");
yyin = fp;
 
yylex();
printf("\nNumber of integers - %d\n", integerCount);
printf("\nNumber of floats - %d\n", floatCount);
printf("\nNumber of operations - %d\n", operationCount);
printf("\nNumber of commas - %d\n", commaCount);
printf("\nNumber of left brackets - %d\n", leftBracketCount);
printf("\nNumber of right brackets - %d\n", rightBracketCount);
 
return 0;
}