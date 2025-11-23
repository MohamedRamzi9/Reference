

int main() {

	struct BitFieldStruct { 
		char a : 3; // bit-field only uses 3 bits
		char b : 5; // bit-field uses remaining bits of the previous member if any
		unsigned int c : 10; // bit-field can span multiple bytes
	};
	BitFieldStruct bfs;
	bfs.a = 5; // valid, fits in 3 bits
	bfs.b = 10; // valid, fits in 5 bits
	bfs.c = 512; // valid, fits in 10 bits
	return 0;
}