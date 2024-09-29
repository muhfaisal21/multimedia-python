from moviepy.editor import VideoFileClip

# Memuat file video
video = VideoFileClip('vidio.mp4')

# Menyimpan file video
video.write_videofile('result.mp4')

short_video = video.subclip(0, 10)  # Mendapatkan 10 detik pertama
short_video.write_videofile('short_result.mp4')

from moviepy.editor import concatenate_videoclips

combined_video = concatenate_videoclips([video, short_video])
combined_video.write_videofile('combined_result.mp4')

from moviepy.editor import vfx

reversed_video = short_video.fx(vfx.time_mirror)  # Membalikkan video
reversed_video.write_videofile('reversed_result.mp4')

sped_up_video = short_video.fx(vfx.speedx, 2)  # Mempercepat video 2x
sped_up_video.write_videofile('sped_up_result.mp4')