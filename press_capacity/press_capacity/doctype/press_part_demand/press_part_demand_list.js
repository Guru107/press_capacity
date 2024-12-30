// This file contains JavaScript code for the part_demand list view, handling dynamic month fields based on the selected financial year.

frappe.listview_settings['Press Part Demand'] = {
    onload: function(listview) {
        listview.page.add_field({
            fieldtype: 'Select',
            label: 'Financial Year',
            options: ['FY-24-25', 'FY-25-26', 'FY-26-27'],
            onchange: function() {
                const selectedYear = this.value;
                listview.refresh();
                listview.set_month_fields(selectedYear);
            }
        });
    },
    set_month_fields: function(year) {
        const monthFields = ['Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar'];
        monthFields.forEach(month => {
            const fieldName = month + '-' + year.split('-')[1];
            if (!frappe.meta.get_docfield('Press Part Demand', fieldName)) {
                frappe.meta.add_field({
                    fieldname: fieldName,
                    fieldtype: 'Float',
                    label: month + ' ' + year.split('-')[1],
                    reqd: 0,
                    in_list_view: 1
                });
            }
        });
    }
};