import frappe

def add_is_press_part_checkbox():
    # Check if the custom field already exists
    if not frappe.db.exists('Custom Field', {'dt': 'Item', 'fieldname': 'is_press_part'}):
        # Create a new custom field
        custom_field = frappe.get_doc({
            'doctype': 'Custom Field',
            'dt': 'Item',
            'fieldname': 'is_press_part',
            'fieldtype': 'Check',
            'label': 'Is Press Part',
            'insert_after': 'Supply Raw Materials for Purchase'  # Adjust this to place the field where you want
        })
        custom_field.insert()
        frappe.db.commit()