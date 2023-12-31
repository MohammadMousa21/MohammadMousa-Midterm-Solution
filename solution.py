tabs=[] #used to save the tab info as a list
tab_index = 0 #used to save the current tab index
nested_tabs=[] #list to save nested tabs on it 
from urllib.request import urlopen # a liberay to open url 
import json # used to save files
def open_tab():#function used to save tab info
  global tab_index # used global sense i need to change the value of tab_index outside the function
  title = input("Enter the title of the website: ")
  url = input("Enter the URL: ")
  tab = {"title": title, "url": url} #create tab as a dictionary
  if title == "" or url[:3] == "www." or url[-1:-4] == "moc." : # no title 
    print("wrong input")
  elif:
    tab_index = len(tabs)
    tabs.append(tab)
def close_tab():# function used to delete tab
  global tab_index
  index = int(input("Enter the index of the tab you want to close "))
  if not index: # condition if the value is not numerical or no index is given 
      index =tab_index
  elif 0 < index <= len(tabs):
    tabs.pop(index) # to delete the tap
  else:
      print("Invalid tab index.")
def display_all_tabs():
  for i in range(len(tabs)):
    print(i,tabs[i]["title"])
    for n in range(len(nested_tabs)):
      if tabs[i]["title"] == nested_tabs[n]["title"]: 
       print("  "+nested_tabs[n]["nest_tab"]) #print below the orginail link
def open_nested_tab():
  index = int(input("Enter the index tab you want to insert a nested tab on it: "))
  if 0 <= index < len(tabs):
      nested_tab_title = input("Enter the title of the nested tab: ")
      url = input("Enter the URL of the nested tab: ")
      nested_tabs = {"title": tabs[index]["title"],"nested_tab_title":nested_tab_title, "url": url}
  else:
      print("Invalid parent tab index.")
def clear_all_tabs():
  global tabs, tab_index
  tabs = []
  tab_index = 0
def switch_tab():
  global tab_index
  index = int(input("Enter the index of the tab to switch"))
  if index== None:
      index =tab_index
  elif 0 > index or index > len(tabs):
      print("Invalid tab index.")
  url = tabs[index]["url"] #https://stackoverflow.com/questions/4302027/how-to-open-a-url-in-python
  page = urlopen(url)
  html_bytes = page.read()
  html = html_bytes.decode("utf-8")
  print(html)
def save_tabs():
  file_path = input("Enter the file path to save tabs: ")
  with open(file_path, 'w') as file:
    json.dump(tabs, file)
#https://stackoverflow.com/questions/67617733/saving-the-json-file-into-a-specified-directory-using-python
def import_tabs():
  file_path = input("Enter the file path ")
  with open(file_path, 'r') as file:
    tabs = json.load(file)
while True:
   print(""""
     1. Open Tab
     2. Close Tab
     3. Switch Tab
     4. Display All Tabs
     5. Open Nested Tab
     6. Clear All Tabs
     7. Save Tabs
     8. Import Tabs
     9. Exit
    """)
   choice = input("Enter your choice: ")
   if choice == "1":
      open_tab()
   elif choice == "2":
      close_tab()
   elif choice == "3":
      switch_tab()
   elif choice == "4":
      display_all_tabs()
   elif choice == "5":
      open_nested_tab()
   elif choice == "6":
      clear_all_tabs()
   elif choice == "7":
      save_tabs()
   elif choice == "8":
      import_tabs()
   elif choice == "9":
      print("Exiting the program")
      break

