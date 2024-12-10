import frappe
from frappe import _
from frappe.module.document import Document

class PressPartsSummary(Document):
    pass
'''

    def populate_press_part_summary():
        # Fetch all items marked as 'is_press_part'
        items = frappe.get_all('Item', filters={'is_press_part': 1}, fields=['name', 'qty_per_vehicle'])
        
        for item in items:
            # Create a new document in Press Part Summary
            summary_doc = frappe.new_doc('Press Parts Summary')
            summary_doc.item_name = item.name
            summary_doc.qty_per_vehicle = item.qty_per_vehicle
            
            # Fetch operations for each workstation type
            operations = frappe.get_all('Item Press Operations', filters={'parent': item.name}, fields=['workstation_type', 'no_of_operations'])
            
            for operation in operations:
                # Add dynamic field for each workstation type
                if not frappe.db.exists('Custom Field', {'dt': 'Press Part Summary', 'fieldname': operation.workstation_type}):
                    frappe.get_doc({
                        'doctype': 'Custom Field',
                        'dt': 'Press Part Summary',
                        'fieldname': operation.workstation_type,
                        'fieldtype': 'Int',
                        'label': operation.workstation_type
                    }).insert()
                
                # Set the number of operations for the workstation type
                setattr(summary_doc, operation.workstation_type, operation.no_of_operations)
            
            summary_doc.insert(ignore_permissions=True)

'''