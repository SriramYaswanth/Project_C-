#ifndef SMART_SWITCH_H_
#define SMART_SWITCH_H_
 
#include "switch_controls.h"
 
typedef enum electronic_accessory_type_t
{
    LIGHT_BULB,     
    FAN,            
    FRIDGE          
}electronic_accessory_type_t;
 
typedef enum power_status_t
{
    POWER_AVAILABLE,        
    POWER_NOT_AVAILABLE     
}power_status_t;            
 
class smart_switch:public switch_controls
{
private:
    electronic_accessory_type_t m_type; 
    power_status_t m_power_status;      
public:
    smart_switch();
    
 
    smart_switch(switch_state_t param_state){
    }
    
    smart_switch(switch_state_t param_state, electronic_accessory_type_t param_type){
        m_type = FAN;

    }
    
    smart_switch(switch_state_t param_state, electronic_accessory_type_t param_type, power_status_t param_power){
        m_type = FAN;
        m_power_status = POWER_AVAILABLE;

    }
 
    smart_switch(const smart_switch& ref_switch){
        m_type = ref_switch.m_type;
        m_power_status = ref_switch.m_power_status;


    }
 
    electronic_accessory_type_t get_electronic_accessory_type();
 
    function_status_t set_electronic_accessory_type(electronic_accessory_type_t);
 
    power_status_t get_power_status();
 
    function_status_t set_power_status(power_status_t);
    
    ~smart_switch();

};
    #endif
