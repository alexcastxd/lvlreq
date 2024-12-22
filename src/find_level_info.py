import requests
import sys

def main():
    ### ARGUMENTS
    request_id = sys.argv[1]
    secret = "Wmfd2893gb7"

    
    get_level_url = "http://www.boomlings.com/database/getGJLevels21.php"
    get_user_url = "http://www.boomlings.com/database/getGJUserInfo20.php"

    headers = {"User-Agent": ""}

    #################
    # GET LEVEL TITLE
    #################

    level_data = {
        "str": request_id,
        "type": 0,
        "secret": secret
    }

    req = requests.post(url=get_level_url, data=level_data, headers=headers).text
    print(req)

    if req != "-1":
        level = req[:req.find("|")].split(":")
        level_name = level[3]   # level name

        creators = req[req.find("#") + 1:]
        creator = creators[:creators.find("#")].split(":")
        creator_id = int(creator[2])

        ###################
        # GET LEVEL CREATOR
        ###################

        user_data = {
            "secret": secret,
            "targetAccountID": creator_id
        }

        req = requests.post(url=get_user_url, data=user_data, headers=headers).text

        user = req.split(":")
        creator_name = user[1]
        print(level_name, "by", creator_name)
    
    return level_name, creator_name

if __name__ == "__main__":
    main()

