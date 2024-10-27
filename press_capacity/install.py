import frappe
from press_capacity.patches.post_install.setup_custom_fields import add_is_press_part_checkbox

def after_install():
    try:
        print("Setting up custom fields...")
        add_is_press_part_checkbox()
    except Exception as e:
        print(f"Error setting up custom fields: {e}")
        raise e