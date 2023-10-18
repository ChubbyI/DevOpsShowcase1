#!/bin/bash

# Define the output file for the system health report
output_file="/var/log/system_health_report.txt"

# Get the current date and time
date_time=$(date '+%Y-%m-%d %H:%M:%S')

# Function to collect system information and append it to the report
collect_info() {
    echo "System Health Report: $date_time" > "$output_file"
    echo "--------------------------------------" >> "$output_file"

    echo -e "\n1. System Uptime:" >> "$output_file"
    uptime >> "$output_file"

    echo -e "\n2. CPU Usage:" >> "$output_file"
    top -n 1 -b | grep Cpu >> "$output_file"

    echo -e "\n3. Memory Usage:" >> "$output_file"
    free -m >> "$output_file"

    echo -e "\n4. Disk Usage:" >> "$output_file"
    df -h >> "$output_file"

    echo -e "\n5. Active Users:" >> "$output_file"
    who >> "$output_file"

    echo -e "\n6. Running Processes:" >> "$output_file"
    ps aux --sort=-%cpu >> "$output_file"
}

# Call the collect_info function and append the report
collect_info

# Print a confirmation message
echo "System health information has been collected and saved to $output_file."

