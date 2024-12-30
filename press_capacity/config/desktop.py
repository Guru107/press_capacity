from frappe import _

def get_data():
    return [
        {
            "module_name": "Press Capacity",
            "color": "grey",
            "icon": "octicon octicon-file-directory",
            "type": "module",
            "label": _("Press Capacity"),
            "link": "List/Press Part Demand",
            "link_type": "List",
            "doctype": "Press Part Demand"
        }
    ]