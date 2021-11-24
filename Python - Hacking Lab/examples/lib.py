import requests

class Examples:

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
    def github_session(user_session = None):
        cookies = {
            "user_session" : user_session
        }
        r = requests.get("https://github.com/settings/profile", cookies=cookies)
        print("Status Code :", r.status_code)
        print("Redirect History :", r.history)
        print("Is Login Page :", "Sign in to GitHub" in r.text)

if __name__ == "__main__":
    # Examples.find_subfolders("localhost", "../wordlist/domain-folders.txt")
    # Examples.find_subfolders("localhost", "../wordlist/common.txt")
    # Examples.find_subdomains("serhatsonmez.com.tr", "../wordlist/domain-folders.txt")
    # Examples.find_subdomains("serhatsonmez.com.tr", "../wordlist/common.txt")
    Examples.github_session()