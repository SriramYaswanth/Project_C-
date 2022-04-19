#ifndef SWITCH_H_
#define SWITCH_H_
#include<bits/stdc++.h>
using namespace std;
int Status_of_fan;
int Status_of_light;
int Status_of_fridge;
typedef enum switch_state_t
{
    OFF,
    ON
} switch_state_t;

typedef enum function_status_t
{
    SUCCESS,
    FAILURE
} function_status_t;

class Controls_Switch
{
public:
    switch_state_t m_switch_state;
    function_status_t m_function_status;
   
public:
    Controls_Switch(void)
    {
        m_switch_state = ON;
        std::cout << "The current state is OFF "<< "\n";
    }
    Controls_Switch(switch_state_t param_state){
        m_switch_state = param_state;
        
    }

    Controls_Switch(const Controls_Switch &ref_switch){
        m_switch_state = ref_switch.m_switch_state;
    }

    switch_state_t get_switch_state()
    {
        if (Status_of_fan == 1)
        {
            cout << "Fan is ON"<<"\n";
            return ON; 
        }
        else if (Status_of_fan == 2)
        {
            cout << "Fan is OFF"<<"\n";
            return OFF;
        }
         else if (Status_of_light == 1)
        {
            cout << "Light is ON"<<"\n";
            return ON; 
        }
        else if (Status_of_light == 2)
        {
            cout << "Light is OFF"<<"\n";
            return OFF;
        }
        else if (Status_of_fridge== 1)
        {
            cout << "Fridge is ON"<<"\n";
            return ON; 
        }
        else 
        {
            cout << "Fridge is OFF"<<"\n";
            return OFF;
        }
    }
    function_status_t set_switch_state(switch_state_t function_state)
    {
        if (function_state == ON)
        {
            cout << "SUCCESS" << "\n";
            return SUCCESS;
            
        }
       
        else
        {
            cout << "STOPPED"<< "\n";
        
        }
    }

  
};
 #endif
