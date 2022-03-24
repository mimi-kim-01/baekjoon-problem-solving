#include <stdio.h>
#include <math.h>

int main(){
    int D, H, W;
    float multi;
    scanf("%d %d %d", &D, &H, &W);
    multi = D/sqrt(pow(W, 2) + pow(H, 2));

    printf("%d %d", (int)(H*multi), (int)(W*multi));

    return 0;
}