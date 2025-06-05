ULTIMATE PROXY CHECKER
======================

A fast, colorful, and easy-to-use proxy checker in Python.
Removes duplicates, cleans proxies, checks in real-time, and saves working proxies instantly.

----------------------------------------------------------
FEATURES
----------------------------------------------------------
- Supports HTTP, HTTPS, SOCKS4, SOCKS5 proxies
- Removes duplicate proxies automatically
- Cleans trailing symbols/letters from proxies
- Real-time checking with colored status output
- Working proxies saved to proxy.txt as soon as found
- Clear summary at the end (total, working, dead, time)
- Easy to use, cross-platform, no progress bar clutter

----------------------------------------------------------
REQUIREMENTS
----------------------------------------------------------
- Python 3.7 or higher
- Modules: requests, colorama

Install requirements (if needed):
    pip install requests colorama

----------------------------------------------------------
USAGE
----------------------------------------------------------
1. Prepare your proxy list file (e.g., proxies.txt), one proxy per line.
   Example:
       123.45.67.89:8080
       98.76.54.32:3128
       1.2.3.4:1080

2. Run the script:
       python proxy_checker.py

3. Follow the prompts:
   - Enter your input proxy file name (e.g., proxies.txt)
   - Select the proxy type (HTTP, HTTPS, SOCKS4, SOCKS5)

4. Watch proxies being checked in real time.
   - Working proxies are shown in green, dead in red.
   - Each line shows current stats (checked, working, dead).

5. All working proxies are saved in 'proxy.txt' as they are found.

6. At the end, view the summary and press any key to exit.

----------------------------------------------------------
NOTES
----------------------------------------------------------
- If your proxy list is large, checking may take a few minutes.
- Only unique, cleaned proxies are checked.
- You can adjust thread count or timeout in the script for faster/slower checking.

----------------------------------------------------------
EXAMPLE OUTPUT
----------------------------------------------------------
[+] 123.45.67.89:8080 1/100 Checked | 1 Working | 0 Dead
[-] 98.76.54.32:3128 2/100 Checked | 1 Working | 1 Dead
...
[+] 5.6.7.8:1080 100/100 Checked | 12 Working | 88 Dead

All working proxies saved in proxy.txt

----------------------------------------------------------
AUTHOR
----------------------------------------------------------
Made with ❤️ for the Ultimate Proxy Checker project.
