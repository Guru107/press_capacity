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
            "fieldname": "section_break_press_op",
            "label": "Press Capacity Planning",
            "fieldtype": "Section Break",
            "insert_after": "pc_is_press_part",
            "depends_on":"pc_is_press_part"
        },
        {
            'doctype': 'Custom Field',
            'dt': 'Item', 
            'fieldname': 'pc_qty_per_vehicle',
            'fieldtype': 'Int',
            'label': 'Qty/Vehicle',
            'insert_after': 'section_break_press_op',
            'default': 1
        },
        {
            'doctype':'Custom Field',
            'fieldname': 'column_break_press_op',
            'fieldtype':'Column Break',
            'insert_after': 'section_break_press_op'
        },
        {
            'doctype': 'Custom Field',
            'dt': 'Item', 
            'fieldname': 'pc_min_forecast',
            'fieldtype': 'Int',
            'label': 'Press Capacity Min Forecast',
            'insert_after': 'column_break_press_op',
            'default': 0
        },
        {
            'doctype': 'Custom Field',
            'dt': 'Item', 
            'fieldname': 'pc_max_forecast',
            'fieldtype': 'Int',
            'label': 'Press Capacity Max Forecast',
            'insert_after': 'column_break_press_op',
            'default': 0
        },
        {
            'doctype': 'Custom Field',
            'dt': 'Item', 
            'fieldname': 'pc_avg_forecast',
            'fieldtype': 'Int',
            'label': 'Press Capacity Avg Forecast',
            'insert_after': 'column_break_press_op',
            'default': 0
        }
    ]
}