#include "rmz_print.hpp"

struct S {
	int a;
	float b;
	operator auto() const {
		return false;
	}
};

int main() {

	S s{42, 3.14f};
	if (auto [a, b] = s) {
		rmz::println("a: {}, b: {}", a, b);
	} else {
		rmz::println("Conversion to bool failed");
	}
	
}