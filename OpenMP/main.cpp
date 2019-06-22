/*

g++ -g --openmp -o main.out  main.cpp && ./main.out

 */


#include <iostream>

int main()
{
    std::cout << "It's supposed to be range [0, 10] (but it's not): ";
#pragma omp parallel
#pragma omp for
for(int i = 0; i < 10; i++)
    std::cout << i;


}
