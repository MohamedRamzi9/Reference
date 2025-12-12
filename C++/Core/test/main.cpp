#include "rmz_print.hpp"

int main() {

	using T=int; int a=8; a.~T();
	rmz::print("Hello, World!\n");
	return 0;
}