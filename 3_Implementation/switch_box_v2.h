#ifndef SWITCH_BOX_V2_H_
#define SWITCH_BOX_V2_H_
 
#include "switch_controls.h"
 
class switch_box_v2
{
private:
    double m_number_of_switches;
    control_switch* m_switch_box_v2;
public:
    switch_box_v2();
    switch_box_v2(double);
    switch_box_v2(double, switch_state_t);
    switch_box_v2(const switch_box_v2&);
 
    function_status_t add_switch_to_switch_box(double);
    function_status_t delete_switch_from_switch_box(double);
 
    int get_number_of_switches_with_state(switch_state_t);
    bool is_all_switch_states_equal();
    function_status_t set_all_switch_states(switch_state_t);
 
    ~switch_box_v2();
};
 
#endif  /* SWITCH_BOX_V2_H_ */
