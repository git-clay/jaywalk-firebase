"""Documentation for pyrebase."""

# WRITE DATA

# push to db example
# data = {"name": "Mortimer 'Morty' Smith"}
# db.child("users").push(data)

# create custom keys
# data = {"name": "Mortimer 'Morty' Smith"}
# db.child("users").child("Morty").set(data)

# update
# db.child("users").child("Morty").update({"name": "Mortiest Morty"})

# delete
# db.child("users").child("Morty").remove()

# multi-location writes
# data = {
#     "users/"+ref.generate_key(): {
#         "name": "Mortimer 'Morty' Smith"
#     },
#     "users/"+ref.generate_key(): {
#         "name": "Rick Sanchez"
#     }
# }
# db.update(data)

# RETRIEVE DATA
"""eventsRef.orderFunction().queryFunction();"""

"""
orderFunctions:
orderByKey()
orderByChild('child_property')
orderByValue()
"""
"""
queryFunctions:
startAt('value')
endAt('value')
equalTo('child_key')
limitToFirst(10)
limitToLast(10)
"""

# val
# users = db.child("users").get()
# print(users.val())
# {"Morty": {"name": "Mortimer 'Morty' Smith"},
# "Rick": {"name": "Rick Sanchez"}}

# key
# user = db.child("users").get()
# print(user.key()) # users

# get
# all_users = db.child("users").get()

# live change listener
# def stream_handler(message):
#    print(message["event"]) # put
#    print(message["path"]) # /-K7yGTTEp7O549EzTYtI
#    print(message["data"]) # {'title': 'Pyrebase', "body": "etc..."}
# my_stream = db.child("posts").stream(stream_handler)
# my_stream.close()

# COMPLEX QUERIES

# example
# users_by_name = db.child("users").order_by_child("name").limit_to_first(3).get()

# equal to
# users_by_score = db.child("users").order_by_child("score").equal_to(10).get()

# start at end at
# users_by_score = db.child("users").order_by_child("score").start_at(3).end_at(10).get()

# order by key
# users_by_key = db.child("users").order_by_key().get()

# order by value
# users_by_value = db.child("users").order_by_value().get()
