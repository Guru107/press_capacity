// Client script for Item DocType
frappe.ui.form.on('Item', {
    refresh: function(frm) {
        // Ensure the field visibility is set correctly on form load
        frm.toggle_display('qty_per_vehicle', frm.doc.is_press_part);
    },
    is_press_part: function(frm) {
        // Toggle the display of 'Qty/Vehicle' based on 'Is Press Part'
        frm.toggle_display('qty_per_vehicle', frm.doc.is_press_part);
        if(frm.doc['qty_per_vehicle']){
           
            // Optionally set a default value when checked
            if (frm.doc.is_press_part) {
                if(!frm.doc.qty_per_vehicle) {
                    frm.set_value('qty_per_vehicle', 1);
                } else {
                    frm.set_value('qty_per_vehicle', 0);
                }
            }
        }
    }
});