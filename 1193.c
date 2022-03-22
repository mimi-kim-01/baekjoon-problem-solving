#include <stdio.h>

int main(){
    int X, m = 0, i, j;
    scanf("%d", &X);
    for (i = 1; i <= X; i++){
        m += i;
        if (m >= X) break;
    }
    for (j = 1; j <= i; j++){
        if (m - i + j == X) break; 
    }
    if (i % 2 != 0) printf("%d/%d", i-j+1, j);
    else if (i % 2 == 0) printf("%d/%d", j, i-j+1);

    return 0;
}