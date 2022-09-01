#!/bin/bash
pkill ffmpeg
ffmpeg \
-video_size 1920x950 \
-framerate 25 \
-f x11grab \
-i :0.0 \
-t 60 \
-y \
/home/bio/test.mp4