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
  elif 0 <= index < len(tabs):
    tabs.pop(index)
  else:
      print("Invalid tab index.")
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
