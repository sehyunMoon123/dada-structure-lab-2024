#pragma once
#include <iostream> // input output ���� �ϱ� ����
#include <string>
using namespace std; // std ���̺귯��

// SmartHome
class SmartHome {
private:
    //class ������ (member veriable or attribute or field)
    string owner; // ���ڿ�
    int temperature; // ������
    int humidity;
    bool security;  //true or false
public:
    //class �Լ��� (member function or class method)
    //������. ���� SmartHome()�̸� �Ҹ���
    SmartHome(string owner, int temperature, int humidity, bool security) {
        this->owner = owner; // ���� ������� ��ü owner�� owner�� �ִ´�
        this->temperature = temperature;
        this->humidity = humidity;
        this->security = security; // owner, temperature ��� = �Ű�����(parameter)
    }
    SmartHome(string o, int t, int h, bool sec) //�� �ڵ�� ������ ����
        : temperature(t), humidity(h), security(s) {
        strcpy(owner, o); // �Ű����� �ȿ� ���� �� o = �μ�(argument) 
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
    string getOwner() { // ���� �ڵ�� void�� ����� ��� ������ �� �ڵ�� string�̶� ��°��� �־�� �� ��� �Է°��� ��� ��
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
        cout << ": " << this->owner << endl; // << = printfó�� ������ �� ����. endl = �ٹٲ�
        cout << "�µ�: " << this->temperature << "��" << endl;
        cout << "����: " << this->humidity << "%" << endl;
        if (this->security) {
            cout << " security on" << endl;
        }
        else {
            cout << "security off" << endl;
        }
    }
};

