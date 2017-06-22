from db_structiure import db_connect,get_config
class customer(object):
	def __init__(self,**kwargs):
		self.id=kwargs.get("id",23)
		self.name=kwargs.get('name','dummy name')
		self.profit=kwargs.get('profit',0)
		self.con, self.cur =  db_connect(get_config())
	def insert(self):
		pass
	def update(self,data):
		pass
	def delete(self):
		pass
