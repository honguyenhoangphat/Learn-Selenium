from pymongo import MongoClient
from datetime import datetime

client = MongoClient('localhost', 27017)
client.drop_database('facebook_py')
db = client["facebook_py"]

files_collection = db["files"]

files_data = [
    { "file_id": 1, "name": "Report.pdf", "size": 2048, "owner": "Nguyen Van A", "created_at": datetime(2024,1,10), "shared": "false" },
    { "file_id": 2, "name": "Presentation.pptx", "size": 5120, "owner": "Tran Thi B", "created_at": datetime(2024,1,15), "shared": "true" },
    { "file_id": 3, "name": "Image.png", "size": 1024, "owner": "Le Van C", "created_at": datetime(2024,1,20), "shared": "false" },
    { "file_id": 4, "name": "Spreadsheet.xlsx", "size": 3072, "owner": "Pham Van D", "created_at": datetime(2024,1,25), "shared": "true" },
    { "file_id": 5, "name": "Notes.txt", "size": 512, "owner": "Nguyen Thi E", "created_at": datetime(2024,1,30), "shared": "false" }
]
files_collection.insert_many(files_data)
#Xem tat ca tep trong bst files
print("All files is: ")
for file in files_data:
    print(file)

#Tim tep co kich thuoc lon hon 2000kb
print("Tep lon hon 2000 la: ")
files_size = files_collection.find({"size": {"$gt": 2000}})
for size in files_size:
    print(size)

#DEM TONG SO TEP
count_files = files_collection.count_documents({})
print(f"Tong so tep la:{count_files} ")

#Tim tat ca tep duoc chia se share = true
share_files = files_collection.find({"shared": "true"})
for share in share_files:
    print(share)

#Thong ke so luong tep theo chu so huu
aggregate_files = files_collection.aggregate([
    {"$group":{"_id": "$owner", "count": {"$sum": 1}}}
])
for agg in aggregate_files:
    print(agg)
    print("Owner:",agg["_id"],"So luong tep:", agg["count"])

##UPDATE
#Cap nhat share id1 = true
files_collection.update_one({"file_id": 1}, {"$set": {"shared": "true"}})

#Xoa tep voi file_id = 3
files_collection.delete_one({"file_id": 3})

#Xem lai tat ca du lieu sau khi cap nhat va xoa
print("Cac file sau khi cap nhat va xoa")
for all in files_collection.find():
    print(all)