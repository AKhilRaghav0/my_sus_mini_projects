#!/bin/bash

# Check if rclone configuration file exists
if [ ! -f "$HOME/.config/rclone/rclone.conf" ]; then
    # If it doesn't exist, prompt the user to create it
    echo "rclone configuration file not found. Please create it."
    rclone config
fi

# Prompt the user for the directory to upload
while true; do
    read -p "Enter the directory to upload: " upload_dir
    if [ -d "$upload_dir" ]; then
        break
    fi
    echo "Invalid directory. Please try again."
done

# Upload the directory to OneDrive using rclone
rclone copy "$upload_dir" remote:onedrive --progress

echo "Upload complete."

