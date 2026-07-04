
#include "rmz_print.hpp"
#include <ranges>



int main() {
    std::u8string_view str = u8"Hello, World!";
    for (auto [i, c] : std::views::enumerate(str)) {
        rmz::println("Index: {}, Character: {}", i, char(c));
    }

}