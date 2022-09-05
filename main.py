import os
import subprocess

if not os.path.exists("videos"):
    raise Exception("Please create the videos folder to put the content!")

elif not os.path.exists("videos\mkv"):
    raise Exception("Please create the mkv and put mkv files")

elif not os.path.exists("videos\mp4"):
    raise Exception("Please create the mp4 and put mkv files")

# Create Results Folders
if not os.path.exists("result"):
    os.mkdir("result")
if not os.path.exists("result\mp4"):
    os.mkdir("result\mp4") 
if not os.path.exists("result\mkv"):
    os.mkdir("result\mkv") 
        


print("""
      1. MKV to MP4
      2. MP4 to MKV
      3. Run all
      """)

option = int(input("Select an option   : "))

if (option == 1): 
    mkv_list = os.listdir("videos\mkv")
        
    for mkv in mkv_list:
        name, ext = os.path.splitext(mkv)
        if ext != ".mkv":
            raise Exception("Only MKV files here !")

        output_name = name + ".mp4"
        try:
            subprocess.run(
            ["ffmpeg", "-i", f"videos/mkv/{mkv}", "-codec", "copy", f"result/mp4/{output_name}"], check=True
        )
        except:
            raise Exception(
                 "Please DOWNLOAD, INSTALL FFMPEG Properly!"
        )


    print(f"{len(mkv_list)} video(s) converted to MP4!")   
    
elif(option == 2):
    mp4_list = os.listdir("videos\mp4")

    for mp4 in mp4_list:
        name, ext = os.path.splitext(mp4)
        if ext != ".mp4":
            raise Exception("Only MP4 files here !")

        output_name = name + ".mkv"
        try:
            subprocess.run(
            ["ffmpeg", "-i", f"videos/mp4/{mp4}", "-codec", "copy", f"result/mkv/{output_name}"], check=True
        )
        except:
            raise Exception(
                 "Please DOWNLOAD, INSTALL FFMPEG Properly!"
        )

    print(f"{len(mp4_list)} video(s) converted to MKV!")   
else:
    print("Invalid Option")
    