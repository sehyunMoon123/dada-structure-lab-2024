#pragma once
#include <cstdio>

class Car {
protected:
	int speed;
	char name[40];
public:
	int gear;
	car(){ }
	~car(){ }
	car(int s, char* n, int g)
		: speed(s), gear(g) {
		strcpy_s(name, n);
	}
	void changeGear(int g = 4) {
		gear = g;
	}
	void speedUp() {
		speed += 5;
	}
	void display() {
		printf("[% s] : ���=%d�� �ӵ�=%dkmph\n", name, gear, speed);
	}
	void whereAmI() { printf("��ü�ּ� = %x\n", this); }
};
