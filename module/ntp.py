import socket
import ntplib
from datetime import datetime, timezone, timedelta

timezone_kst = timezone(timedelta(hours=9))

def ntp(addr):
    try:
        client = ntplib.NTPClient()
        return client.request(addr, version=3)
    except (ntplib.NTPException, socket.gaierror) as e:
        return None


def get(addr_farm):
    for addr in addr_farm:
        response = ntp(addr)

        if response is None:
            continue

        print(f"server: {addr}")
        print(f"request packet sent (as LOCAL client time, orig_time): "
              f"{datetime.fromtimestamp(response.orig_time, timezone_kst)}")
        print(f"request packet received (as NTP server time, recv_time): "
              f"{datetime.fromtimestamp(response.recv_time, timezone_kst)}")
        print(f"response packet sent (as NTP server time, tx_time): "
              f"{datetime.fromtimestamp(response.tx_time, timezone_kst)}")
        print(f"response packet received (as LOCAL client time, dest_time): "
              f"{datetime.fromtimestamp(response.dest_time, timezone_kst)}")
        print(f'round trip duration: {response.delay} s')
        print(f'# adjusted time, tx_time + delay/2: '
              f'{datetime.fromtimestamp(response.tx_time + response.delay / 2, timezone_kst)}')
        print(f'# adjusted time, dest_time + offset: '
              f'{datetime.fromtimestamp(response.dest_time + response.offset, timezone_kst)}')
        print(f'correction to client: {response.delay / 2 - response.offset} s\n')

        return response.delay / 2 - response.offset

    return None
