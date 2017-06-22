import psycopg2
def db_connect(config):
	con=psycopg2.connect(database=config['database'],
		user=config['user'],
		password=config['password'],
		host=config['host'],port=5432)
	cur=con.cursor()
	return con,cur
def create_structure(cur):
	cur.execute("create table customer (id int, name varchar(50), profit int)")
def get_config():
	config = {}
	try:
		f=open('config.csv')
		config_data =f.readlines()
		
		for i in config_data:
			k,v=i.split(',')
			config[k]=v.strip('\n')
	except Exception as err:
		print err
	return config


def main():

	config = get_config()
 	try:
		con,cur=db_connect(config)
		create_structure(cur)

	except Exception as err:
		print err
	finally:
		con.commit()
		cur.close()
		con.close()
if __name__ == "__main__":
	main()