from ftplib import FTP

print("Use this example only with an FTP server you are authorized to access.")
host = input("FTP host, or leave blank to cancel: ").strip()

if host:
    username = input("Username, or leave blank for anonymous access: ").strip()

    try:
        with FTP(host, timeout=10) as ftp:
            if username:
                print("For safety, this learning template does not collect a password.")
                print("Use a controlled local test server for authenticated practice.")
            else:
                ftp.login()
                print("Current directory:", ftp.pwd())
                ftp.retrlines("LIST")
    except Exception as error:
        print("FTP operation failed:", error)
else:
    print("Operation cancelled.")
