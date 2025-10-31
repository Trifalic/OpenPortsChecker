import socket
import argparse
from colorama import Fore, Style, init
import threading

init(autoreset=True)

class Scan:
    def __init__(self, host):
        self._host = host

    def Scan_Port(self, port, arr):
        bot = None
        try:
            bot = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            bot.settimeout(2)
            bot.connect((self._host, port))
            print(f"{Fore.GREEN}{port}{Fore.CYAN} is open")
            arr.append(port)
        except (ConnectionRefusedError, socket.timeout):
            # Port closed / no reply — treat as closed (not an ugly exception)
            print(f"{Fore.BLUE}{port}{Fore.YELLOW} is not open")
        except Exception as e:
            # Something unexpected happened — show it
            print(f"Some error occurred: {Fore.RED}{e}")
        finally:
            if bot:
                try:
                    bot.close()
                except Exception:
                    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-H", "--host", type=str, required=True,
                        help="Enter the address of the host")
    parser.add_argument("-I", "--initial", type=int, required=True,
                        help="Enter the initial port scanning range")
    parser.add_argument("-F", "--final", type=int, required=True,
                        help="Enter the final port scanning range")
    args = parser.parse_args()

    host = args.host
    initial_range = args.initial
    final_range = args.final

    open_ports = []
    threads = []

    scan = Scan(host)

    for port in range(initial_range, final_range + 1):
        thread = threading.Thread(target=scan.Scan_Port, args=(port, open_ports))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print("The list of open ports is:")
    for port in open_ports:
        print(f"{Fore.GREEN}{port}")
