import instaloader

loader = instaloader.Instaloader()

loader.login()

profile = instaloader.Profile.from_username(loader.context, 'isaque.franklin')

followers = profile.get_followers()
 
for follower in followers:
    print(follower)
