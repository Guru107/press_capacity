import frappe

def setup_custom_fields():
    add_is_press_part_checkbox()
    create_item_press_operations_doctype()
    add_press_operations_table_to_item()
    frappe.db.commit()


def add_is_press_part_checkbox():
    # Check if the custom field already exists
    if not frappe.db.exists('Custom Field', {'dt': 'Item', 'fieldname': 'is_press_part'}):
        # Create a new custom field
        is_press_part_field = frappe.get_doc({
            'doctype': 'Custom Field',
            'dt': 'Item',
            'fieldname': 'is_press_part',
            'fieldtype': 'Check',
            'label': 'Is Press Part',
            'insert_after': 'is_sub_contracted_item'  # Adjust this to place the field where you want
        })
        is_press_part_field.insert()

    # Call the functions to create the DocType and populate it
    #create_press_part_summary_doctype()
    #populate_press_part_summary()

def add_qty_field():
    # Create qty_per_vehicle field
    if not frappe.db.exists('Custom Field', {'dt': 'Item', 'fieldname': 'qty_per_vehicle'}):
        qty_per_vehicle_field = frappe.get_doc({
            'doctype': 'Custom Field',
            'dt': 'Item', 
            'fieldname': 'qty_per_vehicle',
            'fieldtype': 'Int',
            'label': 'Qty/Vehicle',
            'insert_after': 'is_press_part',
            'default': 1
        })
        qty_per_vehicle_field.insert()


def create_item_press_operations_doctype():
    """Create the Item Press Operations DocType if it doesn't exist"""
    print("Creating Item Press Operations DocType...")
    if frappe.db.exists('DocType', 'Item Press Operations'):
        return
    
    doc = frappe.new_doc('DocType')
    doc.update({
        'name': 'Item Press Operations',
        'module': 'Press Capacity',
        'custom': 1,
        'istable': 1,  # This makes it a child table
        'fields': [
            {
                'fieldname': 'workstation_type',
                'fieldtype': 'Link',
                'label': 'Workstation Type',
                'options': 'Workstation Type',  # Links to existing Workstation Type doctype
                'reqd': 1
            },
            {
                'fieldname': 'no_of_operations',
                'fieldtype': 'Int',
                'label': 'No. of Operations',
                'reqd': 1
            }
        ]
    })
    
    doc.insert(ignore_permissions=True)


def add_press_operations_table_to_item():
    """Add press operations table to Item DocType"""
    if not frappe.db.exists('Custom Field', {'dt': 'Item', 'fieldname': 'press_operations'}):
        doc = frappe.get_doc({
            'doctype': 'Custom Field',
            'dt': 'Item',
            'fieldname': 'press_operations',
            'fieldtype': 'Table',
            'options': 'Item Press Operations',
            'insert_after': 'qty_per_vehicle',  # Insert in manufacturing section
        })
        doc.insert()


def remove_custom_fields():
    # List of custom fields to remove
    print("Removing custom fields...")
    custom_fields = ['is_press_part', 'qty_per_vehicle','press_operations']

    for fieldname in custom_fields:
        # Check if the custom field exists
        if frappe.db.exists('Custom Field', {'dt': 'Item', 'fieldname': fieldname}):
            # Delete the custom field
            frappe.db.sql('DELETE FROM `tabCustom Field` WHERE dt=%s AND fieldname=%s', ('Item', fieldname))
            frappe.db.commit()

