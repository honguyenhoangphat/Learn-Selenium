from pymongo import MongoClient
from datetime import datetime

client = MongoClient('localhost', 27017)
client.drop_database('facebook_py')
db = client["facebook_py"]

users_collection = db["users"]
posts_collection = db["posts"]
comments_collection = db["comments"]

users_data = [
    { "user_id": 1, "name": "Nguyen Van A", "email": "a@gmail.com", "age": 25 },
    { "user_id": 2, "name": "Tran Thi B", "email": "b@gmail.com", "age": 30 },
    { "user_id": 3, "name": "Le Van C", "email": "c@gmail.com", "age": 22 }
]
users_collection.insert_many(users_data)

posts_data = [
    {"post_id": 1, "user_id": 1, "content": "Hôm nay thật đẹp trời!", "created_at": datetime(2024,9,1)},
    {"post_id": 2, "user_id": 2, "content": "Minh vừa xem một phim hay!", "created_at": datetime(2024,9,2)},
    {"post_id": 3, "user_id": 3, "content": "Chúc mọi người một ngày tốt lành!", "created_at": datetime(2024,9,3)},
    {"post_id": 1, "user_id": 1, "content": "Post id1", "created_at": datetime(2024, 10, 1)},
    {"post_id": 2, "user_id": 2, "content": "Post id2", "created_at": datetime(2024, 10, 2)},
    {"post_id": 3, "user_id": 3, "content": "Post id3", "created_at": datetime(2024, 10, 3)}
]
posts_collection.insert_many(posts_data)

comments_data = [
    { "comment_id": 1, "post_id": 1, "user_id": 2, "content": "Thật tuyệt vời!", "created_at": datetime(2024,9,1) },
    { "comment_id": 2, "post_id": 2, "user_id": 3, "content": "Mình cũng muốn xem bộ phim này!", "created_at": datetime(2024,9,2) },
    { "comment_id": 3, "post_id": 3, "user_id": 1, "content": "Cảm ơn bạn!", "created_at": datetime(2024,9,3)},
    { "comment_id": 1, "post_id": 1, "user_id": 2, "content": "Cmt p1", "created_at": datetime(2024,10,1) },
    { "comment_id": 2, "post_id": 2, "user_id": 3, "content": "Cmt p2", "created_at": datetime(2024,10,2) },
    { "comment_id": 3, "post_id": 3, "user_id": 1, "content": "Cmt p3", "created_at": datetime(2024,10,3) }
]
comments_collection.insert_many(comments_data)

#TRUY VAN DU LIEU
print("Tat ca user")
for user in users_data:
    print(user)

#XEM TAT CA BAI DANG CUA NGUOI DUNG user1
print("Posts của user1 la:")
user_posts = posts_collection.find({"user_id": 1})
for user_post in user_posts:
    print(user_post)

#Xem tat ca binh luan cua post1
print("Cmt cua post1 is:")
comment_posts = comments_collection.find({"post_id": 1})
for comment_post in comment_posts:
    print(comment_post)

#Xem tuoi nguoi tren 25
print("Tuoi nguoi tren 25 la:")
user_age = users_collection.find({"age":{"$gte": 25}})
for age in user_age:
    print(age)

#Truy van bai dang duoc tao trong thang 10
print("Bai dang trong thang 10:")
post_10 = posts_collection.find({"created_at": {"$gte": datetime(2024,10,1), "$lt": datetime(2024,11,1)}})
for post in post_10:
    print(post)

#CAP NHAT NOI DUNG BAI DANG VOI POST_ID = 1
posts_collection.update_one({"user_id":1}, {"$set":{"content": "Up post 1"}})
print("Post duoc cap nhat:")
for post_up in posts_collection.find():
    print(post_up)

#Xoa cmt voi comment_id=2
print("Cmt sau khi cap nhat:")
comments_collection.delete_one({"comment_id":2})
for comment in comments_collection.find():
    print(comment)