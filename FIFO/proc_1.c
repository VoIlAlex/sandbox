#include <stdio.h>
#include <sys/stat.h>
#include <unistd.h>


int main(int argc, char const *argv[])
{
    int retval = mknod(".trash", __S_IFIFO | 0666, 0);
    
    FILE * f = fopen(".trash", "w");
    fprintf(f, "Hello");

    getchar();   

    return 0;
}