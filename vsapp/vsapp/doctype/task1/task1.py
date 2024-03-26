# Copyright (c) 2024, bhumika and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import get_last_doc



class Task1(Document):
	pass

doc = frappe.get_doc('Task1', '8cd1c6a4d9')
doc.title = 'Task Details'
doc.save()

doc = frappe.get_doc({
    'doctype': 'Task1',
    'title': ' Task1'
})
doc.insert()

# user = frappe.get_doc(doctype='User', email_id='test@example.com')
# user.insert()
task1 = get_last_doc('Task1')
# Task1 = frappe.get_last_doc('Task1', filters={"status": "Cancelled"})

frappe.db.get_list('Task1')
frappe.db.get_value('Task1', '8cd1c6a4d9', 'Task name')






	
