frappe.ui.form.on('Press Part Demand', {
    refresh: function(frm) {
        if (frm.doc.is_press_part) {
            frappe.call({
                method: 'frappe.client.get',
                args: {
                    doctype: 'Item',
                    name: frm.doc.item_code
                },
                callback: function(r) {
                    if (r.message) {
                        frm.set_value('item_name', r.message.item_name);
                        frm.set_value('pc_no_operation', r.message.pc_no_operation);
                    }
                }
            });
        }
    },
    item_code: function(frm) {
        if (frm.doc.is_press_part) {
            frappe.call({
                method: 'frappe.client.get',
                args: {
                    doctype: 'Item',
                    name: frm.doc.item_code
                },
                callback: function(r) {
                    if (r.message) {
                        frm.set_value('item_name', r.message.item_name);
                        frm.set_value('pc_no_operation', r.message.pc_no_operation);
                    }
                }
            });
        }
    }
});