#ifndef ARGUMENTS_HPP
#define ARGUMENTS_HPP 1

#include <string>
#include <iostream>

#include <getopt.h>

typedef struct {
    bool help = false;
    bool version = false;
    bool interactive = false;
    std::string filename;
} Arguments;

Arguments parseArguments(int argc, char* argv[]);

void show_help(std::string program);

#endif