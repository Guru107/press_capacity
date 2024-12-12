import frappe
from press_capacity.press_capacity.teardown import before_uninstall as remove_custom_fields

def before_uninstall():
    remove_custom_fields()

