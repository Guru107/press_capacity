import frappe

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
            'insert_after': 'Supply Raw Materials for Purchase'  # Adjust this to place the field where you want
        })
        is_press_part_field.insert()
        frappe.db.commit()
    # Create qty_per_vehicle field
    if not frappe.db.exists('Custom Field', {'dt': 'Item', 'fieldname': 'qty_per_vehicle'}):
        qty_per_vehicle_field = frappe.get_doc({
            'doctype': 'Custom Field',
            'dt': 'Item', 
            'fieldname': 'qty_per_vehicle',
            'fieldtype': 'Int',
            'label': 'Qty/Vehicle',
            'insert_after': 'Is Press Part',
            'default': 1
        })
        qty_per_vehicle_field.insert()
        frappe.db.commit()

def remove_custom_fields():
    # List of custom fields to remove
    print("Removing custom fields...")
    custom_fields = ['is_press_part', 'qty_per_vehicle']

    for fieldname in custom_fields:
        # Check if the custom field exists
        if frappe.db.exists('Custom Field', {'dt': 'Item', 'fieldname': fieldname}):
            # Delete the custom field
            frappe.db.sql('DELETE FROM `tabCustom Field` WHERE dt=%s AND fieldname=%s', ('Item', fieldname))
            frappe.db.commit()