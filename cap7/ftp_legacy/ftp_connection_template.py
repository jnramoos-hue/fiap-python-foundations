from ftplib import FTP

print("FTP is a legacy protocol and should not be used with real credentials.")
host = input("Enter an FTP host that you are authorized to access, or leave blank to cancel: ").strip()

if host:
    try:
        with FTP(host, timeout=10) as ftp:
            print("Server welcome message:", ftp.getwelcome())
            print("No login or file transfer was performed.")
    except Exception as error:
        print("Connection failed:", error)
else:
    print("Operation cancelled.")
