import inspect
import logging
import os


class LogGen:

    @staticmethod
    def loggenWeld():
        # os.remove('.\\Logs\\automation.log')
        # open('.\\Logs\\automation.log', 'a').close()
        logs_directory = os.path.join(os.getcwd(), 'Logs')
        os.makedirs(logs_directory, exist_ok=True)

        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)

        if not logger.handlers:
            logger.setLevel(logging.INFO)
            log_file_path = os.path.join(logs_directory, 'automation.log')

            fhandler = logging.FileHandler(log_file_path)
            formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(name)s %(message)s',
                                      datefmt='%m/%d/%Y %I:%M:%S %p')
            fhandler.setFormatter(formatter)
            logger.addHandler(fhandler)
        
            return logger

