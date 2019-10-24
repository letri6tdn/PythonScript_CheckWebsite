# PythonScript_CheckWebsite

## Objective: 
  This script checks website's integrity to see if there's any updates. This is a simple script for website monitoring, specialized in detecting small text changes in HTML (or whatever the user opt to: like change in specific classes, picture, etc.). The script runs in the background and checking the website between interval of times (low interval can resulted in DoS warning and make website unreachable). If there is any changes, the system will play a sound repeatedly, warning the user.
  
## Usage: 
  This was developed by me to check if an item is not out of stock anymore (for limited group buys). Other usage can be further achieved by modifying this script.
  
## Milestones:
  - [x] Basic track changes for the whole HTML as LXML (for specific keywords)
  - [x] Tracking changes for a specific class
  - [ ] Changing from manual string comparison to a hash comparison
  - [ ] Maybe implementing a UI
  
 ## ***Posible issues***:
  - DDoS signal to the website server
  - How to ignore minor changes (?)
  - Is the HTML always stable (?)
  - Possible other illegal exploits (?)
