from Config.Util import *
from Config.Config import *
try:
    import concurrent.futures
    import time
    import socket
except Exception as e:
   ErrorModule(e)
   
Title("Ip Pinger")

try:
    def PingIp(hostname, port, bytes):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(2)
                start_time = time.time()
                sock.connect((hostname, port))
                data = b'\x00' * bytes
                sock.sendall(data)
                end_time = time.time()
                elapsed_time = (end_time - start_time) * 1000
                print(f'{BEFORE + current_time_hour() + AFTER} {ADD} Hostname: {white}{hostname}{red} time: {white}{elapsed_time:.2f}ms{red} port: {white}{port}{red} bytes: {white}{bytes}{red} status: {white}succeed{red}')
        except:
            elapsed_time = 0
            print(f'{BEFORE + current_time_hour() + AFTER} {ERROR} Hostname: {white}{hostname}{red} time: {white}{elapsed_time}ms{red} port: {white}{port}{red} bytes: {white}{bytes}{red} status: {white}fail{red}')

    Slow(wifi_banner)

    hostname = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Ip -> " + color.RESET)

    try:
        port_input = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Port (enter for default) -> " + color.RESET)
        port = int(port_input) if port_input else 80
        
        bytes_input = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Bytes (enter for default) -> " + color.RESET)
        bytes = int(bytes_input) if bytes_input else 64
    except:
        ErrorNumber()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        while True:
            time.sleep(0.1)
            executor.submit(PingIp, hostname, port, bytes)

except Exception as e:
    Error(e)
