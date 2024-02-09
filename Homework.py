# 1.Get so’rovi orqali https: // jsonplaceholder.typicode.com / comments?postId = 1 teng bulgan commentlarni chiqaring.
# 2.Json moduldan foydalanib https: // jsonplaceholder.typicode.com / users userlar ro’yxatni chiqaring.
# 3.Json moduldan foydalanib https: // jsonplaceholder.typicode.com / users userlarni email, address, phone ro’yxatni chiqaring



# 1.Get so’rovi orqali https: // jsonplaceholder.typicode.com / comments?postId = 1 teng bulgan commentlarni chiqaring.


# import requests
# url = "https://jsonplaceholder.typicode.com/comments?postId=1"
# response = requests.get(url=url)
# print(response.text)





# 2.Json moduldan foydalanib https://jsonplaceholder.typicode.com/users userlar ro’yxatni chiqaring.
# import requests
# url = "https://jsonplaceholder.typicode.com/users"
# response = requests.get(url=url)
#
# print(response.text)




# 3.Json moduldan foydalanib https: // jsonplaceholder.typicode.com / users userlarni email, address, phone ro’yxatni chiqaring
# import requests
# url = "https://jsonplaceholder.typicode.com/users"
#
# response = requests.get(url=url)
# for i in response.json():
#
#     # print(i["User"]["Email"]["Address"]["Phone"])
#     print(i["phone"], i["address"])

