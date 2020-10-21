videos = ["video_1.mp4",
          "video_2.mp4",
          "video_3.mp4",
          "video_4.mp4"]

links = ["https://xa.com/video_1.mp4",
         "https://xa.com/video_2.mp4",
         "https://xa.com/video_3.mp4",
         "https://xa.com/video_4.mp4"]

# output = [
#   {1: {"name": "video_1.mp4", "link": "https://xa.com/video_1.mp4"}},
#   {2: {"name": "video_2.mp4", "link": "https://xa.com/video_2.mp4"}},
#   {3: {"name": "video_3.mp4", "link": "https://xa.com/video_3.mp4"}},
#   {4: {"name": "video_4.mp4", "link": "https://xa.com/video_4.mp4"}},
#   ]

# xa = [] 

# xa = [idx for idx in zip(videos, links)]
# print(xa)
xa = [{"name": idx[0], "link": idx[1]} for idx in zip(videos, links)]
xa = [{(idx): di} for idx, di in enumerate(xa, start=1)]



# ya = {idx[0]: idx[1] for idx in zip(videos, links)}
# za = {}
# ya = [za.setdefault(idx[0], idx[1]) for idx in zip(videos, links)]
# for idx in xa:
#   ya.append({"name": idx[0], "link": idx[1]})


# # za.setdefault() -> Adds key-value pair but doesnt update new values
# # za.update() -> Adds key-value pair but references to the latest values
# output = []
# for idx, di in enumerate(ya, start=1):
#   output.append({idx:di})

print(xa)
