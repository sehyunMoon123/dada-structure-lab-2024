#include <cstdio>

void sub(int x, int arr[])
{
	x = 10;
	arr[0] = 10;
}
void main()
{
	int var;
	int list[MAX_SIZE];

	var = 0;
	list[0] = 0;
	sub(var, list);
	printf("var=%d, list[0]")
}