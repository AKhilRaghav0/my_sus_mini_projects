#!/bin/bash

# function to embed data in video file
function embed_data {
    echo "Embedding data in video file..."
    ffmpeg -i "$1" -c:v libx264 -crf 23 -preset fast -vf "stegano=seeds=1:key=0:carrier=watermark.png:msg=$2" "$3"
    echo "Data embedded successfully."
}

# function to extract data from video file
function extract_data {
    echo "Extracting data from video file..."
    ffmpeg -i "$1" -c:v libx264 -crf 23 -preset fast -vf "stegano=seeds=1:key=0:extract=1" -f rawvideo -y - | tail -c +44 | head -c 50 > extracted_data.txt
    echo "Data extracted successfully."
}

# get input video file path from user
read -p "Enter the path of the input video file: " input_file

# get output video file path from user
read -p "Enter the path of the output video file: " output_file

# get data to be embedded from user
read -p "Enter the data to be embedded in the video: " data

# embed data in video file
embed_data "$input_file" "$data" "$output_file"

# extract data from video file
extract_data "$output_file"

