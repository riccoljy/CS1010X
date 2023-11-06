#
# CS1010X --- Programming Methodology
#
# Sidequest 12.1 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

import json

# Reading json file
def read_json(filename):
    """
    Reads a json file and returns a list of modules
    To find out more about json, please google ;)

    For example, cs1010x-fbdata.json contains:

    {
       "members": {
          "data": [
             {
                "name": "Aadit Kamat",
                "id": "1003982836283025"
             },
             {
                "name": "Rakshit Gogia",
                "id": "10204299775189027"
             },
             ...
          ]
       },
       "description": "This is the official FB Group for ...",
       "name": "CS1010X",
       "feed": {
          "data": [
             {
                "message": "Might be useful for the business analytics ...",
                "from": {
                   "name": "Ben Leong",
                   "id": "10152805891837166"
                },
                "name": "Machine Learning with Python - BDU"
                "id": "409054432560329_1002582839874149",
                "likes": {
                   "data": [
                      {
                         "id": "10208170707289199",
                         "name": "Lim Kian Hwee"
                      },
                      {
                         "id": "10204292869386114",
                         "name": "Siidheesh Theivasigamani"
                      },
                      ...
                   ]
                },
                ...
             },
             ...
          ]
       },
       "id": "409054432560329"
    }

    """
    datafile = open(filename, 'r',  encoding='utf-8')
    return json.loads(datafile.read())

# CS1010X Facebook Group Data as a dictionary object
fb_data = read_json('cs1010x-fbdata.json')

##########
# Task a #
##########

def count_comments(data):
    counter = 0
    all_posts = data["feed"]["data"]
    num_of_posts = len(all_posts)
    for i in range(num_of_posts):
        if "comments" in all_posts[i]:
            num_of_comments_in_that_post = len(all_posts[i]['comments']['data'])
            counter += num_of_comments_in_that_post    
    return counter

print("Number of Comments in CS1010X: ", count_comments(fb_data))

##########
# Task b #
##########

def count_likes(data):
    counter = 0
    all_posts = data["feed"]["data"]
    num_of_posts = len(all_posts)
    for i in range(num_of_posts):
        if "likes" in all_posts[i]:
            num_of_likes_in_that_post = len(all_posts[i]['likes']['data'])
            counter += num_of_likes_in_that_post
            
        if "comments" in all_posts[i]:
            num_of_comments_in_that_post = len(all_posts[i]['comments']['data'])
            for j in range(num_of_comments_in_that_post):
                if "like_count" in all_posts[i]['comments']['data'][j]:
                    counter += all_posts[i]['comments']['data'][j]["like_count"]
    return counter

print("Number of Likes in CS1010X: ", count_likes(fb_data))

##########
# Task c #
##########

def create_member_dict(data):
    result = {}
    all_members = data["members"]["data"]
    num_of_members = len(all_members)
    for i in range(num_of_members):
        member = all_members[i]
        member_id = member["id"]
        result[member_id] = {}
        for data in member:
            if data != "id":
                result[member_id][data] = member[data]
    return result

member_dict = create_member_dict(fb_data)
print(member_dict["10205702832196255"])

# Q: Why did we choose the id of the member data object to be the key?
# A: Because id of member data object will not repeat and are all unique. Each member will definitely have a unique ID.

# Q: It is inappropriate to use the name as the key. What will happen if we use the name as the key of member_dict?
# A: If the names of members are used as key, then in the event that there are members with the exact same name, the values will overlap and be replaced during the iteration.


##########
# Task d #
##########

def posts_freq(data):
    result = {}
    all_posts = data["feed"]["data"]
    num_of_posts = len(all_posts)
    for i in range(num_of_posts):
        writer_id = all_posts[i]["from"]["id"]
        try:
            result[writer_id] += 1
        except KeyError:
            result[writer_id] = 1
    return result

print("Posts Frequency: ", posts_freq(fb_data))

##########
# Task e #
##########

def comments_freq(data):
    result = {}
    all_posts = data["feed"]["data"]
    num_of_posts = len(all_posts)
    for i in range(num_of_posts):
        if "comments" in all_posts[i]:
            num_of_comments_in_that_post = len(all_posts[i]['comments']['data'])
            for j in range(num_of_comments_in_that_post):
                commenter_id = all_posts[i]['comments']['data'][j]["from"]["id"]
                try:
                    result[commenter_id] += 1
                except KeyError:
                    result[commenter_id] = 1
    return result

print("Comments Frequency: ", comments_freq(fb_data))

##########
# Task f #
##########

def likes_freq(data):
    result = {}
    all_posts = data["feed"]["data"]
    num_of_posts = len(all_posts)
    for i in range(num_of_posts):
        if "likes" in all_posts[i]:
            num_of_likes_in_that_post = len(all_posts[i]['likes']['data'])
            for j in range(num_of_likes_in_that_post):
                liker_id = all_posts[i]['likes']['data'][j]["id"]
                try:
                    result[liker_id] += 1
                except KeyError:
                    result[liker_id] = 1
    return result

print("Likes Frequency: ", likes_freq(fb_data))

##########
# Task g #
##########

def popularity_score(data):
    # Returns a dict where key is fb_id and value is the number of likes
    # a person's posts and comments have
    result = {}
    all_posts = data["feed"]["data"]
    num_of_posts = len(all_posts)
    for i in range(num_of_posts):
        if "likes" in all_posts[i]:
            writer_id = all_posts[i]["from"]["id"]
            num_of_likes_in_that_post = len(all_posts[i]['likes']['data'])
            if num_of_likes_in_that_post != 0:
                try:
                    result[writer_id] += num_of_likes_in_that_post
                except KeyError:
                    result[writer_id] = num_of_likes_in_that_post
                        
        if "comments" in all_posts[i]:
            num_of_comments_in_that_post = len(all_posts[i]['comments']['data'])
            for j in range(num_of_comments_in_that_post):
                if "like_count" in all_posts[i]['comments']['data'][j]:
                    commenter_id = all_posts[i]['comments']['data'][j]["from"]["id"]
                    if all_posts[i]['comments']['data'][j]['like_count'] != 0:
                        try:
                            result[commenter_id] += all_posts[i]['comments']['data'][j]['like_count']
                        except KeyError:
                            result[commenter_id] = all_posts[i]['comments']['data'][j]['like_count']
    return result

print("Popularity Score: ", popularity_score(fb_data))

##########
# Task h #
##########

def member_stats(data):
    # Expand the member dict to include the keys:
    # 'posts_count', 'comments_count' and 'likes_count'
    dict_of_members = create_member_dict(data)
    
    dict_of_posts = posts_freq(data)
    dict_of_comments = comments_freq(data)
    dict_of_likes = likes_freq(data)

    for member_id in dict_of_members:
        dict_of_members[member_id]["posts_count"], dict_of_members[member_id]["comments_count"], dict_of_members[member_id]["likes_count"] = 0, 0, 0
                

    for member_id in dict_of_posts:
        try:
            dict_of_members[member_id]["posts_count"] = dict_of_posts[member_id]
        except KeyError:
            continue

    for member_id in dict_of_comments:
        try:
            dict_of_members[member_id]["comments_count"] = dict_of_comments[member_id]
        except KeyError:
            continue

    for member_id in dict_of_likes:
        try:
            dict_of_members[member_id]["likes_count"] = dict_of_likes[member_id]
        except KeyError:
            continue

    
    
    return dict_of_members

stats = member_stats(fb_data) ##for some reason member '10153001427297573' is not inside list of members?
print(stats["10152805891837166"])

##########
# Task i #
##########

def activity_score(data):
    dict_of_members = create_member_dict(data)
    result = {}
    for member_id in dict_of_members:
        result[member_id] = 0 #set score 0 for all first

    stats = member_stats(data)
    for member_id in stats:
        result[member_id] = stats[member_id]['posts_count'] * 3 + stats[member_id]['comments_count'] * 2 + stats[member_id]['likes_count'] * 1 
    
    return result

scores = activity_score(fb_data)
print(scores["10153020766393769"]) # => 30
print(scores["857756387629369"]) # => 8


##########
# Task j #
##########

def active_members_of_type(data, k, type_fn):
    # This is a higher order function, where type is a function and
    # can be either posts_freq, comments_freq, likes_freq, etc
    # and filters out the pairs that have frequency >= k
    dict_of_fn = type_fn(data)
    dict_of_members = create_member_dict(data)
    full_list = []
    for member_id in dict_of_fn:
        try:
            member_name = dict_of_members[member_id]["name"]
            member_value = dict_of_fn[member_id]
            full_list.append([member_name, member_value])
        except KeyError:
            continue
    filtered_list = list(filter(lambda x: x[1] >= k, full_list))
    filtered_list.sort(key = lambda x: (-x[1], x[0])) #negative number to sort reverse, and forward for name
    return filtered_list 

print(active_members_of_type(fb_data, 2, posts_freq))

print(active_members_of_type(fb_data, 20, comments_freq))

print(active_members_of_type(fb_data, 40, likes_freq))

print(active_members_of_type(fb_data, 20, popularity_score))

print(active_members_of_type(fb_data, 80, activity_score))




########### DO NOT REMOVE THE TEST BELOW ###########

def gradeit():
    print("\n*** Facebook Stalker Autograding ***")
    print('==================')
    answers = json.loads(open('grading.json', 'r',  encoding='utf-8').read())
    total, correct = 0, 0
    def pass_or_fail(code, answer):
        nonlocal total
        total += 1
        if code == answer:
            nonlocal correct
            correct += 1
            return 'Passed!'
        else:
            return 'Failed.'
            
    print('Testing count_comments... ', pass_or_fail(count_comments(fb_data), answers['count_comments']))
    print('Testing count_likes... ', pass_or_fail(count_likes(fb_data), answers['count_likes']))
    print('Testing create_member_dict... ', pass_or_fail(create_member_dict(fb_data), answers['create_member_dict']))
    print('Testing posts_freq... ', pass_or_fail(posts_freq(fb_data), answers['posts_freq']))
    print('Testing comments_freq... ', pass_or_fail(comments_freq(fb_data), answers['comments_freq']))
    print('Testing likes_freq... ', pass_or_fail(likes_freq(fb_data), answers['likes_freq']))
    print('Testing popularity_score... ', pass_or_fail(popularity_score(fb_data), answers['popularity_score']))
    print('Testing member_stats... ', pass_or_fail(member_stats(fb_data), answers['member_stats']))
    print('Testing activity_score... ', pass_or_fail(activity_score(fb_data), answers['activity_score']))
    print('Testing members with >= 1 posts... ', pass_or_fail(active_members_of_type(fb_data, 1, posts_freq), answers['active_posters']))
    print('Testing members with >= 4 comments... ', pass_or_fail(active_members_of_type(fb_data, 4, comments_freq), answers['active_commenters']))
    print('Testing members with >= 4 likes... ', pass_or_fail(active_members_of_type(fb_data, 4, likes_freq), answers['active_likers']))
    print('Testing members who have >= 3 likes... ', pass_or_fail(active_members_of_type(fb_data, 3, popularity_score), answers['popular']))
    print('Testing members with an activity score of >= 10... ', pass_or_fail(active_members_of_type(fb_data, 10, activity_score), answers['overall_active']))
    print('==================')
    print('Grades: ' + str(correct) + '/' + str(total) + '\n')

gradeit()
