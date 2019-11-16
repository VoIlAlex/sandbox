#include <stdio.h>
#include <sys/stat.h>
#include <unistd.h>


int main(int argc, char const *argv[])
{
    //int retval = mknod(".trash", __S_IFIFO | 0666, 0);

    FILE * f = fopen(".trash", "r");
    char str[1024] = {0};
    fscanf(f, "%s", str);
    printf("%s", str);

    return 0;
}
