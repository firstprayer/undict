# undict
Easier API for using Dictionary, especially with json

Replace

    first_friend_age = json.loads(json_string)['friends'][0]['facebook_user']['personal_info']['age']
    
with

    from undict import undict
    first_friend_age = undict(json.loads(json_string)).friends[0].facebook_user.personal_info.age
   
