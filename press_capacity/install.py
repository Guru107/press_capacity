import frappe
from press_capacity.press_capacity.setup import after_install as create_custom_fields

def after_install():
    try:
        print("Setting up custom fields...")
        create_custom_fields()
    except Exception as e:
        print(f"Error setting up custom fields: {e}")
        raise e