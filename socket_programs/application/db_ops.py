from db_structiure import db_connect,get_config
import logging
class customer(object):
	def __init__(self,**kwargs):
		self.id=kwargs.get("id",23)
		self.name=kwargs.get('name','dummy name')
		self.profit=kwargs.get('profit',0)
		self.con, self.cur =  db_connect(get_config())
		self.table="customer"
	def insert(self):
		logging.info("Customer details to insert: name:%s, \
			id:%s,profit:%s"%(self.name,self.id,self.profit))
		try:
			self.cur.execute("insert into %s values(%s,'%s',%s)"%(self.table,self.id,
			                                         self.name,self.profit))
			self.con.commit()
		except Exception as err:
			logging.exception(str(err))
	def update(self,data):
		pass
	def delete(self):
		pass
	def browse(self,id=None,name=None,profit=None):
		"""
		select * from customer
		select * from customer where id=12, name=name12, profit=20
		"""
		q="select * from %s"%self.table
		try:
			if id or name or profit:
				q=q+" where"
				if id:
					q=q+" id=%s,"%id
				if name:
					q=q+" name=%s,"%name
				if profit:
					q=q+" profit=%s"%profit
				q=q.strip(',')
				logging.debug("Query: q")
				self.cur.execute(q)
				return self.cur.fetchall()
		except Exception as err:
			logging.exception(str(err))
			return []

