import ftplib
import os

def connect_to_ftp(server, username, password):
    try:
        ftp = ftplib.FTP(server)
        ftp.login(user=username, passwd=password)
        print("Connected to FTP server.")
        return ftp
    except ftplib.all_errors as e:
        print(f"FTP connection error: {e}")
        return None

def backup_wave(ftp):
    backup_name = input("Enter the backup name (without extension): ")
    if not backup_name:
        print("Backup canceled.")
        return

    save_path = input("Enter the directory path to save the backup: ")
    if not save_path:
        print("Backup canceled.")
        return

    local_file = os.path.join(save_path, f"{backup_name}.qgl.bak")
    remote_file = "/dev_blind/vsh/resource/qgl/lines.qrc"

    try:
        with open(local_file, "wb") as f:
            ftp.retrbinary(f"RETR {remote_file}", f.write)
        print(f"Backup saved as {local_file}")
    except ftplib.all_errors as e:
        print(f"Error backing up file: {e}")

def install_wave(ftp):
    # this shit will give 451 action abvorted please hlep fix ty bye make pr please

    file_path = input("Enter the full path to the lines.qrc file: ")
    if not file_path or not os.path.isfile(file_path):
        print("Installation canceled.")
        return

    remote_file = "/dev_blind/vsh/resource/qgl/lines.qrc"

    try:
        with open(file_path, "rb") as f:
            ftp.storbinary(f"STOR {remote_file}", f)
        print(f"New wave installed from {file_path}")
    except ftplib.all_errors as e:
        print(f"Error installing file: {e}")

def main():
    server = input("Enter FTP server address: ")
    username = input("Enter FTP username: ")
    password = input("Enter FTP password: ")

    ftp = connect_to_ftp(server, username, password)
    if not ftp:
        return

    while True:
        print("\nMenu:")
        print("1. Back up wave")
        print("2. Install new wave")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            backup_wave(ftp)
        elif choice == "2":
            print("Directly installing waves is not supported right now due to my stupid code. If you would like to fix it and avoid the inevitable 451 Action Aborted error, please make a pull request. Please manually upload your lines.qrc file to /dev_blind/vsh/resource/qgl/.")
        elif choice == "3":
            ftp.quit()
            print("Disconnected from FTP server.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()