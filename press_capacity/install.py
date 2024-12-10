import frappe
from press_capacity.patches.post_install.setup_custom_fields import setup_custom_fields

def after_install():
    try:
        print("Setting up custom fields...")
        setup_custom_fields()
    except Exception as e:
        print(f"Error setting up custom fields: {e}")
        raise e