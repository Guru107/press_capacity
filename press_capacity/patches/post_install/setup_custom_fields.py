import frappe

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
