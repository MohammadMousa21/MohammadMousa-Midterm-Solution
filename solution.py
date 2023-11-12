tabs=[]
tab_index = 0
def open_tab():
  global tab_index
  title = input("Enter the title of the website: ")
  url = input("Enter the URL: ")
  tab = {"title": title, "url": url}
  tab_index = len(tabs)
  tabs.append(tab)
def close_tab():
  global tab_index
  index = int(input("Enter the index of the tab you want to close "))
  if index == None:
      index =tab_index
  elif 0 < index <= len(tabs):
    tabs.pop(index)
  else:
      print("Invalid tab index.")
def switch_tab():
  global current_tab_index
  index = int(input("Enter the index of the tab to switch"))
  if index== None:
      index =tab_index
  elif 0 > index or index > len(tabs):
      print("Invalid tab index.")
  url = tabs[index]["url"]
  page = urlopen(url)
  html_bytes = page.read()
  html = html_bytes.decode("utf-8")
  print(html)
def clear_all_tabs():
  global tabs, current_tab_index
  tabs = []
  tab_index = 0
def save_tabs():
  file_path = input("Enter the file path to save tabs: ")
  with open(file_path, 'w') as file:
    json.dump(tabs, file)
#https://stackoverflow.com/questions/67617733/saving-the-json-file-into-a-specified-directory-using-python
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
