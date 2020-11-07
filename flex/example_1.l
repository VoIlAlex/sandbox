%{
int count = 0;
%}

%%
[I|i][L|l][Y|y][A|a] {count ++;}
. {}
end {return 0;}
%%

int yywrap() {}
int main() {
    yylex();
    printf("\nNumber if Ilyas - %d\n", count);
    return 0;
}