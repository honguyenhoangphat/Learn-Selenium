from pymongo import MongoClient
from datetime import datetime

#Kết nối mongodb
client = MongoClient('localhost', 27017)
client.drop_database('tiktok_py')
db = client["tiktok_py"]

#Tao collection
users_collection = db["users"]
videos_collection = db["videos"]
#Them data
users_data = [
    {"user_id":1, "user_name": "user1", "full_name": "Ho Nguyen Hoang Phat", "followers": 10000, "following": 1},
    {"user_id": 2, "user_name": "user2", "full_name": "Nguyen Hoang Vu", "followers": 5000, "following": 1000},
    {"user_id": 3, "user_name": "user3", "full_name": "Pham Quoc An", "followers": 7000, "following": 50},
    {"user_id": 4, "user_name": "user4", "full_name": "Nguyen Thi Thanh Tam", "followers": 400, "following": 10},

]
users_collection.insert_many(users_data)

videos_data = [
    {"video_id": 1, "user_id": 1, "title": "Video 1", "views": 10000, "likes": 500},
    {"video_id": 2, "user_id": 2, "title": "Video 2", "views": 50000, "likes": 10000},
    {"video_id": 3, "user_id": 2, "title": "Video 3", "views": 4000, "likes": 156},

]
videos_collection.insert_many(videos_data)

#Truy van du lieu tren python
#1. Xem tat ca nguoi dung
print("Tat ca nguoi dung: ")
for user in users_collection.find():
    print(user)

#2. Tim video view cao nhat
print("Video co luot xem cao nhat: ")
max_viewed_video = videos_collection.find().sort('views', -1).limit(1)
for video in max_viewed_video:
    print(video)

#3.Tim tat ca video cua nguoi dung co username la "user1"
print("Video cua user1 la: ")
user_videos = videos_collection.find({"user_id": 1})
for video in user_videos:
    print(video)

#CAP NHAT DU LIEU
#CAP NHAT SO NGUOI THEO DOI CUA USER 1
users_collection.update_one({"user_id":1}, {"$set":{"followers": 900000}})

#XOA VIDEO 3
videos_collection.delete_one({"video_id": 3})

#Xem lai du lieu sau khi cap nhat
print("Tat ca nguoi dung sau khi cap nhat: ")
for user in users_collection.find():
    print(user)

print("Du lieu video sau khi cap nhat:")
for video in videos_collection.find():
    print(video)

client.close()