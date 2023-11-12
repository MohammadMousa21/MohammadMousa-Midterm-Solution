tabs=[]
def open_tab():
  title = input("Enter the title of the website: ")
  url = input("Enter the URL: ")
  tab = {"title": title, "url": url}
  tabs.append(tab)
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
