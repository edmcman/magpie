#include <iostream>
#include <string>

std::string getMessage() {
    return "Hello, World!";
}

void printMessage() {
    std::string message = getMessage();
    std::cout << message << std::endl;
}

int main() {
    printMessage();
    return 0;
}
