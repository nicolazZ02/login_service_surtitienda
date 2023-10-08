import logging
from app.common import settings
import os
class Logger():

    @staticmethod
    def get_level():
        return settings.LEVEL_LOG
    @staticmethod
    def get_filename():
        return settings.FILENAME_LOG
    @staticmethod
    def get_format():
        return settings.FORMAT_LOG
    @staticmethod
    def get_date_format():
        return settings.DATEFORMAT_LOG 
    @staticmethod
    def get_logger(name):
        logger = logging.getLogger(name)
        logger.setLevel(Logger.get_level())

        formatter = logging.Formatter(
            Logger.get_format(),
            Logger.get_date_format())
        
        log_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))+os.sep+'logs'
        log_file = os.path.join(log_dir, Logger.get_filename())

        if not os.path.exists(log_dir):
            print('Se esta creeando directorio de logs:' + log_dir)
            os.makedirs(log_dir)
        file_hdlr = logging.FileHandler(log_file, mode='a', encoding='utf-8')
        file_hdlr.setFormatter(formatter)

        steam_hdlr = logging.StreamHandler()
        handler = logging.StreamHandler()
        handler.setLevel(Logger.get_level())

        logger.addHandler(hdlr=file_hdlr)
        logger.addHandler(hdlr=steam_hdlr)

        return logger
