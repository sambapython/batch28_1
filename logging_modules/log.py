import logging
#logging.basicConfig(level=logging.INFO)
#logging.basicConfig(level=logging.DEBUG)
#logging.basicConfig(level=logging.WARN)
#logging.basicConfig(level=logging.DEBUG, filename="log1.txt")
logging.basicConfig(level=logging.DEBUG, filename="log1.txt",
	format="%(asctime)s->%(levelname)s>>>>>>>>>%(message)s")
logging.info("info statements")
logging.debug("debug statements")
logging.warn("warning statement")
logging.exception("exception statements")
logging.error("Error statement")