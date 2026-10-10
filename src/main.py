from checks import status_check


def main():
    print(status_check("https://google.com").status)
    
main()