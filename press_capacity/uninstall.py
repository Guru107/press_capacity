import frappe
from press_capacity.patches.post_install.setup_custom_fields import remove_custom_fields

def after_uninstall():
    remove_custom_fields()