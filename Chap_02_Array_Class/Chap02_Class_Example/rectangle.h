#pragma once
#include <iostream>

class rectangle {
private:
	double width;
	double height;

public:
	rectangle(double w, double h) {
		width = w;
		height = h;
	}

	double getArea() {
		return width * height;
	}
	double getperimeter() {
		return 2 * (width + height);
	}
	bool isSquare() {
		return (width == height);
	}
};
