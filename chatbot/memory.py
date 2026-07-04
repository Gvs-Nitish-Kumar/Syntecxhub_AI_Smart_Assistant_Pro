def save_name(name):
    with open("data/user_data.txt", "w") as file:
        file.write(name)

def get_name():
    try:
        with open("data/user_data.txt", "r") as file:
            return file.read()
    except:
        return ""