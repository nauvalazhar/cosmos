// This is an extended C++ example to test overflow, syntax highlighting, and various aspects of C++ syntax.

#include <iostream>
#include <vector>
#include <map>
#include <thread>
#include <functional>

void printMessage(const std::string& message) {
    std::cout << message << std::endl;
}

int main() {
    std::vector<std::string> vec = {"Element 1", "Element 2", "Element 3"};
    for (const auto& element : vec) {
        printMessage(element);
    }

    std::map<int, std::string> map;
    map[1] = "One";
    map[2] = "Two";

    for (const auto& pair : map) {
        std::cout << "Key: " + std::to_string(pair.first) + ", Value: " + pair.second << std::endl;
    }

    std::thread t([]() {
        printMessage("This is a thread running in C++.");
    });
    t.join();

    return 0;
}
