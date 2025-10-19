#include <math.h>
#include <stdbool.h>
#include <stdio.h>

bool is_prime(long p) {
  if (p < 2) {
    return false;
  }
  long sqrt_p = (long)sqrt(p);
  for (long i = 2; i <= sqrt_p; i++) {
    if ((p % i) == 0) {
      return false;
    }
  }
  return true;
}

long f(long n) {
  long largest_prime_factor = -1;
  for (long i = 1; i <= n; i++) {
    if (((n % i) == 0) && is_prime(i)) {
      n /= i;
      largest_prime_factor = i;
    }
  };
  return largest_prime_factor;
}

int main() {
  printf("%ld\n", f(600851475143));
  return 0;
}
