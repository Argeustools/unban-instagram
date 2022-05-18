#
# This Is Free Tool By Soud Alanzi AKA @8Y
# Dont Try Sell It Cuz It's Fucking Free
# Github: https://github.com/Soud69
# Instagram: https://instagram.com/8Y
# Telegram: https://t.me/Soud69
# Discord: Soud#5866
#

try:
    import requests
    import os
    from os import system, path
    import threading
    import random
    system("title " + "Soud Was Here - @8Y - Soud#5866")
    import colorama
    from colorama import Fore
    colorama.init(autoreset=True)

except Exception as m:
    print("Something Went Wrong\n")
    print(m)
    input()
    exit()

if path.exists("proxy.txt"):
    proxyfile = open("proxy.txt", 'r').read().splitlines()
else:
    print("Pls Make proxy.txt file\n")
    input()
    exit()

sent, spam, banned = 0, 0, 0
logo = f"""
{Fore.CYAN}         _______   __                                
{Fore.CYAN}   ____ |  _  \ \ / /                                
{Fore.CYAN}  / __ \ \ V / \ V /                                 
{Fore.CYAN} / / _` |/ _ \  \ /                                  
{Fore.CYAN}| | (_| | |_| | | |                                  
{Fore.CYAN} \ \__,_\_____/ \_/                                  
{Fore.CYAN}  \____/                                                                                          
{Fore.GREEN} _   _       _                   _   _  _____  _____ 
{Fore.GREEN}| | | |     | |                 | | | |/ __  \|  _  |
{Fore.GREEN}| | | |_ __ | |__   __ _ _ __   | | | |`' / /'| |/' |
{Fore.GREEN}| | | | '_ \| '_ \ / _` | '_ \  | | | |  / /  |  /| |
{Fore.GREEN}| |_| | | | | |_) | (_| | | | | \ \_/ /./ /___\ |_/ /
{Fore.GREEN} \___/|_| |_|_.__/ \__,_|_| |_|  \___/ \_____(_)___/                      
"""
print(logo)
print(f"{Fore.RED}This Is Free Tool By Soud Alanzi And Not For Sale\n\n{Fore.RESET}{Fore.GREEN}Instagram: @8Y + @_agf\nDiscord: Soud#5866\n")
account_username = input("Username: ")
account_full_name = input("Account Name: ")
account_email = input("Email: ")
account_phone = int(input("Phone Number: "))
message_contact = input("Contact Message (Leave It Empty To Use Default Message): ")

if message_contact == "":
    message_contact = "Hello Instagram Support, my account have been disabled by mistake, pls reactive it"
threads_number = int(input("Threads: "))

def unban():
    global spam, sent, banned, account_full_name, account_email, account_username, account_phone, message_contact
    while 1:
        proxy_dict = []
        for proxy in proxyfile:
            proxy_dict.append(proxy)
            rnd = str(random.choice(proxy_dict))
        try:
            proxyfinal = {
                "http": f"http://{rnd}",
                "https": f"http://{rnd}"
            }
            url = "https://www.facebook.com/ajax/help/contact/submit/page"
            headers = {
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9",
                "content-type": "application/x-www-form-urlencoded",
                "origin": "https://www.facebook.com",
                "referer": "https://www.facebook.com/help/instagram/contact/606967319425038",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
                "x-fb-lsd": "AVpTUe7mhU0"
            }
            data = {
                "jazoest": 2934,
                "lsd": 'AVpTUe7mhU0',
                "name": account_full_name,
                "email": account_email,
                "instagram_username": account_username,
                "mobile_number": account_phone,
                "appeal_reason": message_contact,
                "support_form_id": 606967319425038,
                "support_form_hidden_fields": "{}",
                "support_form_fact_false_fields": "[]",
                "__user": 0,
                "__a": 1,
                "__dyn": "7xe6Fo4OQ1PyWwHBWo5O12wAxu13wqovzEy58ogbUuw9-3K4o1j8hwem0nCq1ewcG0KEswaq1xwEwt81sbzo5iaw4Ugao884y0lW1TwoU2swdq0Ho2ew",
                "__csr": "",
                "__req": "g",
                "__beoa": 0,
                "__pc": "PHASED:DEFAULT",
                "__bhv": 2,
                "__no_rdbl": 0,
                "dpr": 1,
                "__ccg": "GOOD",
                "__rev": "1003617880",
                "__s": "ufr3b8:q2h5ui:co1t38",
                "__hsi": "6950826502173272197-0",
                "__comet_req": 0,
                "__spin_r": 1003617880,
                "__spin_b": "trunk",
                "__spin_t": 1618365408
            }
            req = requests.post(url, data=data, headers=headers, proxies=proxyfinal, timeout=3)
            if ">Form submitted successfully" in req.text:
                sent += 1
                print(f"\rSent : {sent} | Spam : {spam} | Error: {banned}", end="")
            elif "You may want to slow down or stop to avoid a restriction on your account" in req.text:
                spam += 1
                print(f"\rSent : {sent} | Spam : {spam} | Error: {banned}", end="")
            elif "The username or short-link you provided does not belong to an inactive Instagram Account." in req.text:
                sent += 1
                print("\nUnbanned !")
                print(f"\n\rSent : {sent} | Spam : {spam} | Error: {banned}\n\n")
                input("Click Enter To Exit...")
                exit()
            else:
                banned += 1
                print(f"\rSent : {sent} | Spam : {spam} | Error: {banned}", end="")
        except:
            banned += 1
            print(f"\rSent : {sent} | Spam : {spam} | Error: {banned}", end="")


threads = []
for i in range(threads_number + 1):
    t = threading.Thread(target=unban)
    t.start()
    threads.append(t)
for i in threads:
    i.join()
