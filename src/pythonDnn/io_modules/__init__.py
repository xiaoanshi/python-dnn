
def setLogger(stderr=True,logFile='python-dnn.log',name=None):
	import logging,sys

	#get Logger
	logger = logging.getLogger(name)

	if stderr:
		# Send the logs to stderr
		stream_handler = logging.StreamHandler()
		# Format the log output and include the log level's name and the time it was generated
		formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
		# Use that Formatter on handler
		stream_handler.setFormatter(formatter)
		# Add the handler to it
		logger.addHandler(stream_handler)
	else :
		# Set up a log file
		file_handler = logging.FileHandler(logFile)
		file_handler.setFormatter(formatter)
		logger.addHandler(file_handler)
		
		
def create_folder_structure_if_not_exists(filepath):
	import logging,os,errno
	logger = logging.getLogger(__name__)
	try:
		path = os.path.dirname(filepath)
		os.makedirs(path)
		logger.info("Created folder structure %s.." % path)
	except OSError as exc: # Python >2.5
		if exc.errno == errno.EEXIST and os.path.isdir(path):
			logger.debug("Folder structure %s already exists.." % path)
		else:
			logger.critical("Folder structure %s could not be created.." % path) 
			raise
	return path
