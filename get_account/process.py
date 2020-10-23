from InstagramAPI import InstagramAPI

api = InstagramAPI("cutecats_cm", "JcbzAntho12.Cutecats")
api.login()
print(api.getProfileData())

