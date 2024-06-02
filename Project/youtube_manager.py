import json

file_name = "youtube.txt"

def load_data():
    """
    Loads data from a JSON file.

    This function attempts to open a file specified by the global variable `file_name`
    and load its contents as JSON. If the file does not exist, it returns an empty list.

    Returns:
        list: The data loaded from the JSON file, or an empty list if the file is not found.
    """
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
def save_data_helper(videos):
    with open(file_name, "w") as file:
        json.dump(videos, file)


def list_videos(videos):
    """
    Prints a formatted list of videos with their names and durations.

    Args:
        videos (list of dict): A list of dictionaries where each dictionary 
                               represents a video with 'name' and 'time' keys.

    Example:
        videos = [
            {'name': 'Video 1', 'time': '3:45'},
            {'name': 'Video 2', 'time': '4:20'}
        ]
        list_videos(videos)
    """
    print("\n\n")
    print("*" * 70)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']} ")
    print("*" * 70)
    print("\n")
def add_videos(videos):
    """
    Adds a new video to the list of videos.

    Prompts the user to enter the name and time of the video, then appends
    a dictionary containing this information to the provided list of videos.
    Finally, it calls the save_data_helper function to save the updated list.

    Args:
        videos (list): A list of dictionaries where each dictionary represents a video with 'name' and 'time' keys.

    Returns:
        None
    """
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({"name": name, "time": time})
    save_data_helper(videos)
def update_video(videos):
    """
    Updates the details of a video in the list of videos.

    Args:
        videos (list): A list of dictionaries where each dictionary represents a video with keys 'name' and 'time'.

    Returns:
        None
    """
    list_videos(videos)
    index = int(input("Enter the video number to update: "))
    if 1 <= index <= len(videos):
        name = input("Enter the new video name: ")
        time = input("Enter the new video time: ")
        videos[index - 1] = {"name": name, "time": time}
        save_data_helper(videos)
        print("******Video Updation successful******")
    else:
        print("Invalid index selected")
def delete_video(videos):
    list_videos(videos)
    index = int(input("Enter the video  number to  be deleted : "))
    if 1 <= index <= len(videos):
        del videos[index - 1]
        save_data_helper(videos)
        print("******Video Deletion sucessfull******")
    else:
        print("Invaild index selected")


def main():
    """
    Main function to manage YouTube videos. Provides a menu for the user to choose actions such as
    listing, adding, updating, and deleting YouTube videos.

    The function runs in a loop until the user chooses to exit the application.
    """
    videos = load_data()

    while True:
        print("\nYoutube Manager || choose an option")
        print("1. List all youtube videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video")
        print("4. Delete a youtube videos")
        print("5. Exit the app")

        choice = input("Enter your choice: \n")

        match choice:
            case "1":
                list_videos(videos)
            case "2":
                add_videos(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                print("\nExiting the app...")
                break
            case _:
                print("Invalid choice. Please choose a valid option.")
if __name__ == "__main__":
    main()