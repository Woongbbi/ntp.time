import configparser as parser

import module.ntp as ntp
import module.time as time

from datetime import datetime, timedelta

if __name__ == '__main__':
    res_time = False

    config = parser.ConfigParser()
    config.read('./config.ini')

    main_time_server = config['SERVER']['MAIN']
    backup_time_server = config['SERVER']['BACKUP']

    offset = ntp.get([main_time_server, backup_time_server])

    if offset is not None:
        now = datetime.now()
        correct_time = now + timedelta(seconds=offset)

        print(now.strftime('%Y-%m-%d %H:%M:%S.%f'))
        print(correct_time.strftime('%Y-%m-%d %H:%M:%S.%f'))

        time.set(correct_time.strftime('%Y-%m-%d %H:%M:%S.%f'))

