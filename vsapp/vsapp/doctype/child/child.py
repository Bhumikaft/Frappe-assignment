# Copyright (c) 2024, bhumika and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
class Child(Document):
	
	def validate(self):
		self.set_value()
	def set_value(self):
		frappe.db.set_value('Parent',"Ram",'Last_Name','Singh')


	# def validate (self):
		# frappe.msgprint("Hello")
	# def before_save(self):
	   #  frappe.throw("Hello")
    # def before_insert(self):
       #   frappe.throw("please insert a details")
    # def on_update(self):
      #   frappe.msgprint("update data succesfully")
    # def before_submit(self):
      # frappe.msgprint("details submitted sucessfully")
      # frappe.db.set_value(doctype , name, fieldname,Value)


	#   frappe.db.get_value(doctype , name, fieldname)
	# def validate(self):
	# 	self.get_value()
	# def get_value(self):
	# 	First_Name, Last_Name = frappe.db.get_value('Parent','7ee0c07bbf',['First_Name','Last_Name'])
	# 	frappe.msgprint(("The parent first name is {0}and last name is {1}").format(First_Name, Last_Name))



   
