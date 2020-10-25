import logging
# types of levels = debug < info < warning < error < critical
logger = logging.getLogger(__name__)
#creating streamhandler and filehandler
st = logging.StreamHandler()
fi = logging.FileHandler("/home/mmohdbilal/bilal/logger-module/file_handler")
#setting level
st.setLevel(logging.WARNING)
fi.setLevel(logging.ERROR)
# formating streamhandler and filehandler
for_st = logging.Formatter('%(levelname)s - %(asctime)s, %(name)s - %(message)s', 
datefmt='%d/%h/%Y %I:%M:%S')
st.setFormatter(for_st)
fi.setFormatter(for_st)
# adding streamhandler and filehandler
logger.addHandler(st)
logger.addHandler(fi)
# creating error and warning
logger.warning("this is a warning")
logger.error("this is a error")
