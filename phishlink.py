import requests
import logo

print(logo.LOGO)

# Checks whether URL starts with http or https or not
def check_url(entered_url):
    if not entered_url.startswith(('https://', 'http://')):
        print("\033[31m[!] Invalid URL. Please use http or https.\033[0m")
        exit(1)

# Shorts the phishing URL using is.gd API 
def url_shortner(phish_url):
    gd_api_url  = f"https://is.gd/create.php?format=simple&url={phish_url}"
    response = requests.get(gd_api_url)
    if response.status_code == 200:
        return response.text
    
    else:
        print("\033[31m[!] Failed to shorten URL. Check the phishing URL.\033[0m")
        exit(1)

# Mask the phising URL with custom domain and social engineering words
def masked_url():
    print(logo.WELCOME)

    
    # Takes phishing URL in input and verify it using check_url function
    phish_url = input('Enter Phishing URL Here (with protocol eg. http or https): ')
    check_url(phish_url)

    print('Processing and Modifying Phishing URl...\n')

    # Shorts the phising link using url_shortner function after it is verified
    shortened_url = url_shortner(phish_url)
    shortner = shortened_url.replace('https://', '')

    # Takes phishing domain as input and check whether domain starts with http or https or not
    mask_domain = input('Domain to mask the phishing URL (with http or https), e.g., https://instagram.com: ')
    check_url(mask_domain)

    # Take Social Engineering Words as input to add in masked URl
    social_engineering_words = input('\nType social engineering words (e.g., free-money, unlimited-followers): ')
    if not social_engineering_words:
        print("\033[31m[!] No social engineering words provided.\033[0m")
        final_url = f"{mask_domain}@{shortner}"
    
    else:
        if " " in social_engineering_words:
            print("\033[31m[!] Invalid words. Please avoid spaces.\033[0m")
            final_url = f"{mask_domain}@{shortner}"
        else:
            final_url = f"{mask_domain}-{social_engineering_words}@{shortner}"

    print("\nGenerating Masked Phishing Link...\n")
    print(f"Here is the Masked URL: \033[32m{final_url}\033[0m\n")

if __name__ == '__main__':
    masked_url()