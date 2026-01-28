set main=%1
set module=%2
set hedears=D:\Programmig\C++\Libraries\headers
cls

del %main%.exe

g++ -std=c++26 -fmodules-ts -I %hedears% -c module-partion2.cpp
g++ -std=c++26 -fmodules-ts -I %hedears% -c module-partion1.cpp
g++ -std=c++26 -fmodules-ts -I %hedears% -c module.cpp 
g++ -std=c++26 -fmodules-ts -I %hedears% -o %main%.exe %main%.cpp module.o module-partion1.o module-partion2.o

%main%.exe

del %main%.exe
del module.o
del module-partion1.o
del module-partion2.o