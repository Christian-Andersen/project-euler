#include <stdio.h>

int sum_below(int n) {
  int total = 0;
  for (int i = 0; i < n; i++) {
    if (((i % 3) == 0) || ((i % 5) == 0)) {
      total += i;
    }
  }
  return total;
}

int main() {
  printf("%d\n", sum_below(1000));
  return 0;
}
