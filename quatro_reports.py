from quatro import init_app_log_dir, log, start_scheduler, configuration as c
from config import Config
from tasks import outstanding_pos_task


def main():
    c.config = Config(__file__)
    init_app_log_dir()
    log(f'Starting {__file__}')
    c.config.sql_connections()
    start_scheduler(outstanding_pos_task)


if __name__ == "__main__":
    main()
