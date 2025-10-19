#include <stdio.h>

int f(int n) {
  int total = 0;
  int a = 1;
  int b = 2;
  while (1) {
    if (a > n) {
      break;
    }
    if ((a % 2) == 0) {
      total += a;
    }
    if (b > n) {
      break;
    }
    if ((b % 2) == 0) {
      total += b;
    }
    a += b;
    b += a;
  }
  return total;
}

int main() {
  printf("%d\n", f(4000000));
  return 0;
}
