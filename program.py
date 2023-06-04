import urllib.request
import os

# Your current program's version
current_version = 1.1

# URL to your 'version file'
version_file_url = 'https://raw.githubusercontent.com/MrByron11/PythonShit/main/version.txt?token=GHSAT0AAAAAACDPPJFBGN3TMITVQD5J3WVSZD4SDWQ'

# URL to your updated Python file
python_file_url = 'https://raw.githubusercontent.com/MrByron11/PythonShit/main/program.py?token=GHSAT0AAAAAACDPPJFB32OHAZJLJDD6URYSZD4SFCQ'

# Function to get the latest version
def get_latest_version(url):
    with urllib.request.urlopen(url) as f:
        return float(f.read().decode())

# Function to download the latest Python file
def download_file(url, filename):
    urllib.request.urlretrieve(url, filename)

# Check for updates
try:
    latest_version = get_latest_version(version_file_url)
    if latest_version > current_version:
        print('Update available. Updating...')
        download_file(python_file_url, os.path.basename(__file__))
        print('Program updated.')
    else:
        print('No updates available.')
except Exception as e:
    print('Error checking for updates.')
    print(e)

print('version 1.1')
