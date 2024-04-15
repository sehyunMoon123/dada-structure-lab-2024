#pragma once
#include <iostream> // input output 쉽게 하기 위해
#include <string>
using namespace std; // std 라이브러리

// SmartHome
class SmartHome {
private:
    //class 변수들 (member veriable or attribute or field)
    string owner; // 문자열
    int temperature; // 정수형
    int humidity;
    bool security;  //true or false
public:
    //class 함수들 (member function or class method)
    //생성자. 만약 SmartHome()이면 소멸자
    SmartHome(string owner, int temperature, int humidity, bool security) {
        this->owner = owner; // 지금 만드려는 객체 owner에 owner를 넣는다
        this->temperature = temperature;
        this->humidity = humidity;
        this->security = security; // owner, temperature 등등 = 매개변수(parameter)
    }
    SmartHome(string o, int t, int h, bool sec) //위 코드랑 동일한 내용
        : temperature(t), humidity(h), security(s) {
        strcpy(owner, o); // 매개변수 안에 들어가는 값 o = 인수(argument) 
    }

    void setTemperature(int temperature) {
        this->temperature = temperature;
    }
    void setHumidity(int humidity) {
        this->humidity = humidity;
    }
    void setSecurity(bool security) {
        this->security = security;
    }
    string getOwner() { // 위쪽 코드는 void라 출력이 없어도 되지만 이 코드는 string이라 출력값이 있어야 함 대신 입력값이 없어도 됨
        return this->owner;
    }
    int getTemperature() {
        return this->temperature;
    }
    int getHumidity() {
        return this->humidity;
    }
    bool getSecurity() {
        return this->security;
    }
    void printStatus() {
        cout << ": " << this->owner << endl; // << = printf처럼 옆으로 쭉 나옴. endl = 줄바꿈
        cout << "온도: " << this->temperature << "도" << endl;
        cout << "습도: " << this->humidity << "%" << endl;
        if (this->security) {
            cout << " security on" << endl;
        }
        else {
            cout << "security off" << endl;
        }
    }
};

