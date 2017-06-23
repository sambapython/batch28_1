from db_ops import customer
import logging
logging.basicConfig(level=logging.DEBUG, filename="log1.txt",
                    format="%(asctime)s;%(levelname)s;%(message)s")
def insert():
    logging.info("Takig details from the user")
    c_id=raw_input("Enter id:")
    c_name=raw_input("Enter name: ")
    profit=12
    logging.debug("user given details: name:%s, id:%s, profit: %s"%(c_id,c_name,profit))

    samba = customer(id=c_id,name=c_name,profit=profit)
    samba.insert()
def search():
    print "search by\n 1.id\n2.name\n3.profit"
    option=raw_input("Enter an option")
    c_id=None
    if option=="1":
        c_id=raw_input("Enter id:")
    unknow=customer()
    if c_id:
        print unknow.browse(id=c_id)

print "1: insert\n2.search"
option = raw_input("Enter an option:")

if option=="2":
    logging.info("user selected: search")
    search()
elif option=="1":
    logging.info("user selected: insert")
    insert()



