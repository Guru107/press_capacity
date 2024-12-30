CUSTOM_FIELDS = {
    "Item":[
       {
            'doctype': 'Custom Field',
            'dt': 'Item',
            'fieldname': 'pc_is_press_part',
            'fieldtype': 'Check',
            'label': 'Is Press Part',
            'insert_after': 'is_sub_contracted_item'  # Adjust this to place the field where you want
        },
        {
            "fieldname": "pc_tab_break",
            "label": "Press Capacity Planning",
            "fieldtype": "Tab Break",
            "insert_after": "Manufacturing",
            "depends_on":"pc_is_press_part"
        },
        {
            'doctype': 'Custom Field',
            'dt': 'Item', 
            'fieldname': 'pc_qty_per_vehicle',
            'fieldtype': 'Int',
            'label': 'Qty/Vehicle',
            'insert_after': 'pc_tab_break',
            'default': 1
        },
        {
            'doctype': 'Custom Field',
            'dt': 'Item', 
            'fieldname': 'pc_min_forecast',
            'fieldtype': 'Int',
            'label': 'Min Forecast',
            'insert_after': 'pc_qty_per_vehicle',
            'default': 0
        },
        {
            'doctype': 'Custom Field',
            'dt': 'Item', 
            'fieldname': 'pc_avg_forecast',
            'fieldtype': 'Int',
            'label': 'Avg Forecast',
            'insert_after': 'pc_min_forecast',
            'default': 0
        },
        {
            'doctype': 'Custom Field',
            'dt': 'Item', 
            'fieldname': 'pc_max_forecast',
            'fieldtype': 'Int',
            'label': 'Max Forecast',
            'insert_after': 'pc_avg_forecast',
            'default': 0
        },
        {
            "doctype":'Custom Field',
            'dt':'Item',
            'fieldname':'pc_item_operation',
            'fieldtype':'Table',
            'options':'Item Operations',
            'label': 'Item Operations',
            'insert_after':'pc_max_forecast'
        }
    ]
}