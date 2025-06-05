# 🚀 ULTIMATE PROXY CHECKER

A fast, colorful, and easy-to-use proxy checker in Python.  
✨ Removes duplicates, cleans proxies, checks in real time, and saves working proxies instantly.

---

## 🛠️ Features

- ⚡ **Super Fast:** Multi-threaded real-time proxy checking  
- 🔄 **Duplicate Removal:** Only unique proxies are checked  
- 🧹 **Cleans Proxies:** Removes trailing symbols/letters  
- 🟢 **Live Status:** Green for working, red for dead  
- 💾 **Auto-Save:** Working proxies saved to `proxy.txt` as soon as found  
- 📊 **Summary:** Clear stats at the end (total, working, dead, time)  
- 🖥️ **User-Friendly:** No clutter, just clean output

---

## 📦 Requirements

- Python 3.7 or higher
- Modules: `requests`, `colorama`


---

## 🚦 Usage

1. **Prepare your proxy list file** (e.g., `proxies.txt`), one proxy per line:
    ```
    123.45.67.89:8080
    98.76.54.32:3128
    1.2.3.4:1080
    ```
2. **Run the script:**
    ```
    python proxy_checker.py
    ```
3. **Follow prompts:**
    - Enter your proxy file name (e.g., `proxies.txt`)
    - Select proxy type (`HTTP`, `HTTPS`, `SOCKS4`, `SOCKS5`)
4. **Watch real-time results:**
    - 🟢 Working proxies in green, 🔴 dead in red
    - Each line shows `[+]` or `[-]` plus live stats

5. **All working proxies are saved in `proxy.txt` as they are found.**

---

## 📈 Example Output

[+] 123.45.67.89:8080 1/100 Checked | 1 Working | 0 Dead
[-] 98.76.54.32:3128 2/100 Checked | 1 Working | 1 Dead
...
[+] 5.6.7.8:1080 100/100 Checked | 12 Working | 88 Dead

✅ All working proxies saved in proxy.txt

---

## 💡 Notes

- Large proxy lists may take a few minutes to check.
- You can adjust thread count or timeout in the script for faster/slower checking.
- Only unique, cleaned proxies are checked.

---

## 👨‍💻 Author

Made with ❤️ for the Ultimate Proxy Checker project.

---
