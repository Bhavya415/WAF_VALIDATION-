import requests
import time
from bs4 import BeautifulSoup
from colorama import Fore, Style, init

base_url = "https://br-ssoca-cat.fiservapp.com"

endpoints = [
    "/as/authorization.oauth2",
    "/as/token.oauth2",
    "/as/revoke_token.oauth2",
    "?=<script>alert(1)</script>",# for testing purpose.
    "/idp/userinfo.openid",
    "/as/introspect.oauth2",
    "/pf/JWKS",
    "/as/clients.oauth2",
    "/pf-ws/rest/sessionMgmt/revokedSris",
    "/pf-ws/rest/sessionMgmt/sessions",
    "/pf-ws/rest/sessionMgmt/sessions",
    "/pf-ws/rest/sessionMgmt/users",
    "/idp/startSLO.ping",
    "/idp/startSSO.ping?PartnerSpId=https://addiko.accessplus.firstdataclients.eu.ping",
    "/sp/startSSO.ping?SpSessionAuthnAdapterId=control360ATB",
    "/idp/startSLO.ping?TargetResource=https://www.google.com",
    "/as/clients.oauth2?response_type=code&client_id=ESSClient&redirect_uri=https://ess.firstdataeservices.com/pa/oidc/cb&state=eyJ6aXAiOiJERUYiLCJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2Iiwia2lkIjoidl9aenI0ejFMTEtkTmFjRzltT3Z3d1dkbVRjIiwic3VmZml4IjoiM0dBTWFRLjE3NDc5MjQ0NDQifQ..uXO2EDYkiFmqz9m8zNKejg.17Tr9BJEAHIp2d8Aiz6BVCmeCHgxoyJqwHnL1SE7elr-gEh92d8-3Vfug_X_rq_rmj8QRMOBrEfAQaDZyKSF4g.JEZlb0k4GuebfNBGe2Sjfw&nonce=LjQ6tYIfDzyRf9OM2Gta0zZVr2Ff-KijCMT2iRYtP40&scope=openid address email phone profile&vnd_pi_requested_resource=https://ess.firstdataeservices.com/&vnd_pi_application_name=ESS firstdataeservices",



    
    # Add the rest of your endpoints here
]

def get_base_urls():
    choice = input("Do you want to test a single base URL or multiple base URLs? Enter \n1) single \n2) multiple ").strip().lower()
    base_urls = []
    if choice == '1':
        base_url = input("Enter the base URL").strip()
        base_urls.append(base_url)
    elif choice == '2':
        print("Enter each base URL on a new line. Enter a blank line to finish:") 
        while True:
            url = input().strip()
            if url == "":
                break
            base_urls.append(url)
    else:
        print("Invalid choice. Please enter 'single' or 'multiple'.")
        return get_base_urls()
    return base_urls

def test_endpoints(base_urls, endpoints):
    for base_url in base_urls:
        print("\n" + "="*60)
        print(f"Testing endpoints for BASE URL: {base_url}".upper())
        print("="*60)
        for endpoint in endpoints:
            url = base_url.rstrip("/") + endpoint
            try:
                response = requests.get(url)
                soup = BeautifulSoup(response.text, 'html.parser')
                title_tag = soup.title.string.strip() if soup.title else "No <title> tag found"
                print(f"Testing {url}")
                if response.status_code == 200 and title_tag == "Unauthorized Request Blocked":
                    print(Fore.RED + f"Status Code: {response.status_code}" + Style.RESET_ALL)
                    print(Fore.RED + f"<title>: {title_tag}" + Style.RESET_ALL)
                else:
                    print(f"Status Code: {response.status_code}")
                    print(f"<title>: {title_tag}")
                print("-" * 40)
            except requests.exceptions.RequestException as e:
                print(f"An error occurred with {url}: {e}")

if __name__ == "__main__":
    base_urls = get_base_urls()
    test_endpoints(base_urls, endpoints)
