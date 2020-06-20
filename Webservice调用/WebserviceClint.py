import suds
from suds.client import Client

url="https://localhost:44338/WebService1.asmx"
client = Client(url)



result = client.service.ceshi("123","456")

print (result)