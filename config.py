from quatro import sigm_connect, log_connect
from os.path import dirname, abspath
import calendar


class Config:
    def __init__(self, main_file_path):
        self.main_file_path = main_file_path
        self.parent_dir = dirname(abspath(main_file_path))
        self.pdf_dir = self.parent_dir + '\\files\\pdf'
        self.ninja = self.parent_dir + '\\files\\crystal reports ninja\\CrystalReportsNinja.exe'
        self.sigm_connection = None
        self.sigm_db_cursor = None
        self.log_connection = None
        self.log_db_cursor = None

        self.TASK_SCHEDULE = {
            'outstanding_pos_task': [
                {
                    'name': 'morning',
                    'hour': 8,
                    'minute': 0
                }
            ]
        }

    def sql_connections(self):
        self.sigm_connection, self.sigm_db_cursor = sigm_connect()
        self.log_connection, self.log_db_cursor = log_connect()
