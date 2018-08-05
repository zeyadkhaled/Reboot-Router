# Reboot Router using Python
I am learning Python so decided to code down this quick Router Rebooting script to fix one of daily issues.

## Usage
- Just fill in the 5 variables by refering to the examples
  ```python
  user_data = {} #Example: {'user':'admin','password':'admin'}
  reboot_data = {} #Example: {'reboot':'true'}
  headers = {} #Example: {'Content-Type': 'application/x-www-form-urlencoded'} 
  login_url = '' #Example: http://192.168.1.1/api/user/login
  reboot_url = '' #Example: http://192.168.1.1/api/user/reboot
  ```

- Thats it. Now you can run the script

## Requirments
- requests module
  ```
  pip requests install
  ```
- Python 3
