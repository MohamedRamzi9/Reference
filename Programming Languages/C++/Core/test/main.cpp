#include "rmz_print.hpp"
#include <meta>

enum E {
    SUNDAY, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY
};

int main() {
    template for (constexpr auto info : define_static_array(enumerators_of(^^E))) {
        rmz::println(display_string_of(info));
    }
}