/*Exec A*/

/*Tokens*/

MAIOR [>]
MENOR [<]
SOMA [+]
SUB [-]
I [i]
W [w]
IGUAL [=]
X [x]
E [e]
DIG_1 [1]
ABR [(]
FECH [)]

/*Estados finitos*/

N {A}{SOMA}{B}|{B}{SUB}{A}|{A}{SUB}{B}
P {X}{IGUAL}{A}|{X}{IGUAL}{B}
PARENT_1 {ABR}{N}{MAIOR}{DIG_1}{FECH}
PARENT_W {ABR}{P}{MAIOR}{DIG_1}{FECH}
ESTA_FIM {N}{X}{IGUAL}{X}{SUB}{A}
ESTA_FIM_1 {N}{E}{N}

A [123]
B [456]

RESULT {I}{PARENT_1}{ESTA_FIM_1}|{W}{PARENT_W}{ESTA_FIM}

/*Exercício C*/

VOGAL      [aeiouAEIOU]
LETRA      [a-zA-Z]

%%

{RESULTADO} {printf("%s eh uma cadeia valida\n", yytext);}

({DIG_1}{DIG_1}{DIGITOZERO})|({DIG_1}{DIG_1}{DIGITOZERO}{DIGITOZERO}) {printf("MULT, %s\n", yytext);}

{VOGAL}{LETRA}{VOGAL} {printf("PAL, %s\n", yytext); }

%%

int main(){

    yylex();
    return 0;
}