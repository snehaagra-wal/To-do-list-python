# To-do-list-python
A smart to do list application that uses JSON for data persistence. 
# key modules used 
JSON : used to serialize and deserialize task list, allowing to save data in structured format
os : to interact with file and check if storage file exists 
# TECHNICAL features
Data persistence- Automatically saves tasks to json file 
Startup check - usses os.pathexists() to verify if data is available
CRUD operation : User can create , read, update , and  delete task
Error handling: prevent crashes if json file is corrupted or missing 
# working 
Initialize: The program uses os module to look for tasks.json 
Load: if found it uses json.load() to bring tasks to memory 
Update: when task is added otr remove json.dump() to overwrite new data
Save: list is up to date on hard drive

