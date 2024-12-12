// Client script for Item DocType
/*
frappe.ui.form.on('Item', {
    refresh: function(frm) {
        // Ensure the field visibility is set correctly on form load
        frm.toggle_display(['qty_per_vehicle', 'press_operations'], frm.doc.is_press_part);
    },
    is_press_part: function(frm) {
        // Toggle the display of 'Qty/Vehicle' based on 'Is Press Part'
        frm.toggle_display(['qty_per_vehicle', 'press_operations'], frm.doc.is_press_part);
        if(frm.doc['qty_per_vehicle']){
           
            // Optionally set a default value when checked
            if (frm.doc.is_press_part) {
                if(!frm.doc.qty_per_vehicle) {
                    frm.set_value('qty_per_vehicle', 1);
                    frm.clear_table('press_operations');
                    frm.refresh_field('press_operations');
                } else {
                    frm.set_value('qty_per_vehicle', 0);
                }
            }
        }
    }
});
*/
/*
// Handle child table events
frappe.ui.form.on('Press Operations', {
    form_render: function(frm, cdt, cdn) {
        // Additional customization for the child table form if needed
    },

    no_of_operations: function(frm, cdt, cdn) {
        let row = locals[cdt][cdn];
        if (row.no_of_operations < 1) {
            frappe.model.set_value(cdt, cdn, 'no_of_operations', 1);
            frappe.throw(__('Number of Operations cannot be less than 1'));
        }
    }
});
*/