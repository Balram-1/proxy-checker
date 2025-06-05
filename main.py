import re
import requests
import concurrent.futures
import time
import os
import sys
from colorama import init, Fore, Style

init(autoreset=True)

ASCII_ART = r"""
 _   _  _ _____ __  __    _    _____ _____  
| | | || |_   _|  \/  |  / \  |_   _| ____|  
| | | || | | | | |\/| | / _ \   | | |  _|   
| |_| || | | | | |  | |/ ___ \  | | | |___   
 \___/ |_| |_| |_|  |_/_/   \_\ |_| |_____|
                                                          

"""

PROXY_TYPES = {
    "1": ("HTTP", "http"),
    "2": ("HTTPS", "https"),
    "3": ("SOCKS4", "socks4"),
    "4": ("SOCKS5", "socks5"),
}

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def ask_input_file():
    while True:
        fname = input(Fore.CYAN + "Enter the input file name containing proxies: " + Style.RESET_ALL).strip()
        if os.path.isfile(fname):
            return fname
        print(Fore.YELLOW + "File not found. Try again." + Style.RESET_ALL)

def ask_proxy_type():
    print(Fore.CYAN + "Select the proxy type:" + Style.RESET_ALL)
    for k, v in PROXY_TYPES.items():
        print(f"{k}. {v[0]}")
    while True:
        choice = input(Fore.CYAN + "Enter the number corresponding to the proxy type: " + Style.RESET_ALL).strip()
        if choice in PROXY_TYPES:
            print(Fore.GREEN + f"You selected proxy type: {PROXY_TYPES[choice][0]}" + Style.RESET_ALL)
            return PROXY_TYPES[choice][1]
        print(Fore.YELLOW + "Invalid choice. Try again." + Style.RESET_ALL)

def clean_proxy(proxy):
    # Remove trailing alphabets and symbols like -, !, + at the end
    return re.sub(r"[a-zA-Z!+\-\s]+$", "", proxy.strip())

def check_proxy(proxy, proxy_type, timeout=3):
    proxy = clean_proxy(proxy)
    proxies = {
        "http": f"{proxy_type}://{proxy}",
        "https": f"{proxy_type}://{proxy}",
    }
    try:
        r = requests.get("http://httpbin.org/ip", proxies=proxies, timeout=timeout)
        if r.status_code == 200:
            return (proxy, True)
    except:
        pass
    return (proxy, False)

def press_any_key_exit():
    print(Fore.MAGENTA + "\nPress any key to exit...", end='', flush=True)
    try:
        # Windows
        import msvcrt
        msvcrt.getch()
    except ImportError:
        # Unix
        import termios
        import tty
        tty.setraw(sys.stdin.fileno())
        sys.stdin.read(1)
    print()

def save_proxy(proxy, filename="proxy.txt"):
    with open(filename, "a") as f:
        f.write(proxy + "\n")

def print_stats_inline(proxy, is_working, checked, total, working, dead):
    status = Fore.GREEN + "[+]" if is_working else Fore.RED + "[-]"
    status += Style.RESET_ALL
    print(f"{status} {proxy} {checked}/{total} Checked | "
          f"{Fore.GREEN}{working} Working{Style.RESET_ALL} | "
          f"{Fore.RED}{dead} Dead{Style.RESET_ALL}")

def main():
    clear()
    print(Fore.MAGENTA + ASCII_ART + Style.RESET_ALL)
    fname = ask_input_file()
    proxy_type = ask_proxy_type()
    with open(fname, "r") as f:
        proxies = [line.strip() for line in f if line.strip()]
    # Remove duplicates and clean proxies
    original_count = len(proxies)
    proxies = [clean_proxy(p) for p in proxies]
    proxies = list(set(proxies))
    dupes_deleted = original_count - len(proxies)
    print(Fore.YELLOW + f"\nRemoved {dupes_deleted} duplicate proxies. {len(proxies)} unique proxies remain." + Style.RESET_ALL)
    print(Fore.CYAN + f"\nChecking {len(proxies)} proxies...\n" + Style.RESET_ALL)
    # Clear proxy.txt at start
    with open("proxy.txt", "w") as f:
        pass
    start = time.time()
    working, dead = [], []
    checked = 0
    total = len(proxies)
    from threading import Lock
    lock = Lock()
    def worker(proxy):
        nonlocal checked
        proxy, is_working = check_proxy(proxy, proxy_type)
        with lock:
            checked += 1
            if is_working:
                working.append(proxy)
                save_proxy(proxy)
            else:
                dead.append(proxy)
            print_stats_inline(proxy, is_working, checked, total, len(working), len(dead))
        return proxy, is_working
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        list(executor.map(worker, proxies))
    elapsed = time.time() - start
    print("\n" + Fore.MAGENTA + "="*40 + Style.RESET_ALL)
    print(Fore.CYAN + f"Total proxies checked: {len(proxies)}" + Style.RESET_ALL)
    print(Fore.GREEN + f"Working proxies:       {len(working)}" + Style.RESET_ALL)
    print(Fore.RED + f"Dead proxies:          {len(dead)}" + Style.RESET_ALL)
    print(Fore.YELLOW + f"Time taken:            {elapsed:.2f} seconds" + Style.RESET_ALL)
    print(Fore.MAGENTA + "="*40 + Style.RESET_ALL)
    print(Fore.GREEN + f"\nAll working proxies saved in proxy.txt" + Style.RESET_ALL)
    press_any_key_exit()

if __name__ == "__main__":
    main()
