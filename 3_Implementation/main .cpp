#include<bits/stdc++.h>
#include "switch_controls.h"
using namespace std;

void Fan_Speed()
{
    int Fan_Speed;
    cout<<"Range of speed of Fan is 1 to 5 "
         << "\n";
    cin>>Fan_Speed;
    if(Fan_Speed<=5)
    {
        cout<<"Speed of Fan is at " << Fan_Speed << "\n";
    }
    else
    {
        cout<<"Speed of fan exceeds its value" << "\n";
    }
}
void Light_Intensity()
{
    int Light_Intensity;
    cout<<"Range of intensity is 1 to 5 "
         <<"\n";
    cin>>Light_Intensity;
    if(Light_Intensity<=5)
    {
        cout<<"Intensity of Light is at "<< Light_Intensity << "\n";
    }
    else
    {
        cout<<"Intensity of light has exceeds its value" << "\n";
    }
}
void Fridge_Temp()
{
    int Fridge_Temp;
    cout<<" Temperature range of fridge is 1 to 5 "
         <<"\n";
    cin >> Fridge_Temp;
    if(Fridge_Temp<=5)
    {
        cout<<"Temperature of the fridge is " << Fridge_Temp << "\n";
    }
    else
    {
        cout<<"Temperature of fridge has exceeds its value" << "\n";
    }   
}

int main()
{
    switch_controls s_FAN;
    switch_controls s_LIGHT;
    switch_controls s_FRIDGE;
    int opt;
    int speed;
    cout<< "Welcome to the smart switch"
        << "\n";
    cout<< "Select the Appliance"
         << "\n";
    cout<< "1. FAN\n 2. BULB\n 3. FRIDGE"
         << "\n";
    cin>>opt;

    switch (opt)
    {
    case 1:
        cout << "FAN"
             << "\n";
        cout << "To Turn ON FAN - Press 1"
             << "\n";
        cout << "To Turn OFF FAN - Press 2"
             << "\n";
        cout << "To control the Speed of Fan - Press 3"
             << "\n";
        cin >> Status_of_fan;
        if (Status_of_fan == 1)
        {
            s_FAN.get_switch_state();
            s_FAN.set_switch_state(ON);
        }
        if (Status_of_fan == 2)
        {
            s_FAN.get_switch_state();
            s_FAN.set_switch_state(OFF);
        }
        if (Status_of_fan == 3)
        {
            Fan_Speed();
        }
        break;

    case 2:
        cout << "LIGHT"
             << "\n";
        cout << "To ON - Press 1"
             << "\n";
        cout << "To OFF - Press 2"
             << "\n";
        cout << "To control Intensity of Light - Press 3"
             << "\n";
        cin >> Status_of_light;
        if (Status_of_light == 1)
        {
            s_LIGHT.get_switch_state();
            s_LIGHT.set_switch_state(ON);
        }
        if (Status_of_light == 2)
        {
            s_LIGHT.get_switch_state();
            s_LIGHT.set_switch_state(OFF);
        }
        if (Status_of_light == 3)
        {
            Light_Intensity();
        }
        break;

    case 3:
        cout << "FRIDGE"
             << "\n";
        cout << "To ON - Press 1"
             << "\n";
        cout << "To OFF - Press 2"
             << "\n";
        cout << "To control temperature - Press 3"
             << "\n";
        cin >> Status_of_fridge;
        if (Status_of_fridge == 1)
        {
            s_FRIDGE.get_switch_state();
            s_FRIDGE.set_switch_state(ON);
        }
        if (Status_of_fridge == 2)
        {
            s_FRIDGE.get_switch_state();
            s_FRIDGE.set_switch_state(OFF);
        }
        if (Status_of_fridge == 3)
        {
            Fridge_Temp();
        }
        break;

    case 4:
        exit(0);

    default:
        break;
    }
}
