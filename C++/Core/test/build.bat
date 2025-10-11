set main=%1

cls

del %main%.exe

g++ -std=c++26 -I D:\Programmig\C++\Libraries\headers -o %main%.exe %main%.cpp

%main%.exe

del %main%.exe