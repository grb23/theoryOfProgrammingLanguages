
#include <iostream>

int main() {
  using F = void(*)(int);
  F fn = (F)5;
  fn(3); // 5 applied to 3 (as lambda expr)
}
