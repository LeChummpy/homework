#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>

int main (int argc, char*argv[]) {
  std::ifstream assfile_stream;
  std::string path = argv[0]
  cout << path;
  assfile_stream.open(path);

  if assfile.is_open() {
    std::string content;
    assfile_stream >> content;

  }

  return 0
}
