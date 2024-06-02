import sqlite3

# Connect to the database (or create it if it doesn't exist)
con = sqlite3.connect("youtube_videos.db")
cursor = con.cursor()

# Create table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
""")

def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    con.commit()

def update_video(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
    con.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    con.commit()

def main():
    while True:
        print("\n***** Youtube Manager App with DB *****")
        print("1. List Videos")
        print("2. Add Video")
        print("3. Update Video")
        print("4. Delete Video")
        print("5. Exit App")
        choice = input("Enter your choice: ")

        match choice:
            case "1":
                list_videos()
            case "2":
                name = input("Enter the video name: ")
                time = input("Enter the video time: ")
                add_video(name, time)
            case "3":
                video_id = int(input("Enter video ID to update: "))  # Ensure the input is converted to an integer
                new_name = input("Enter the new video name: ")
                new_time = input("Enter the new video time: ")
                update_video(video_id, new_name, new_time)
            case "4":
                video_id = int(input("Enter video ID to delete: "))  # Ensure the input is converted to an integer
                delete_video(video_id)
            case "5":
                break
            case _:
                print("Invalid Choice")

    con.close()

if __name__ == "__main__":
    main()
