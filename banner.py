import socket
import argparse
from colorama import Fore, Style, init

init(autoreset=True)


class Banner:
    def __init__(self, host, port=80):
        self._host = host
        self._port = port

    def Get_Banner(self):
        try:
            bot = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            bot.settimeout(2)
            bot.connect((self._host, self._port))
            bot.send(b"HEAD / HTTP/1.0 \r\n\r\n")
            response = b""
            while True:
                data = bot.recv(4096)
                if not data:
                    break
                response += data
            decoded_reponse = response.decode(errors="ignore")
            print(decoded_reponse)

        except Exception as e:
            print(f"Some error occured:{Fore.RED}{e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-H", "--host", type=str, help="Enter the host address")
    parser.add_argument("-P", "--port", type=int, help="Enter the port of the target")
    args = parser.parse_args()

    host = args.host
    port = args.port

    banner = Banner(host, port)
    banner.Get_Banner()
