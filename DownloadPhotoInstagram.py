import instaloader
import requests

def download_instagram_photo(username):
    # Get instance
    loader = instaloader.Instaloader()
    try:
        # Use Profile class to access metadata of account
        profile = instaloader.Profile.from_username(loader.context, username)

        # Get profile phot url 
        profile_photo_url = profile.profile_pic_url

        # Download photo 
        response = requests.get(profile_photo_url)

        if response.status_code == 200:
            with open(f"{username}.jpg","wb") as file:
                file.write(response.content)
            print(f"Photo {username} was successfully completed")
        else:
            print(f"Photo {username} was not successfully completed")
    except instaloader.exceptions.ProfileNotExistsException:
        print(f"Account {username} does no exist.")
    except Exception as e :
        print(f"the error message: {e}")


if __name__=="__main__":
    username = input("Enter Instegran Username ")
    download_instagram_photo(username)