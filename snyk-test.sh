#!/bin/bash

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Function to print messages with timestamp
log_message() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Check if snyk is installed
if ! command_exists snyk; then
    log_message "Snyk not found. Installing..."

    # Download snyk
    if curl -L https://static.snyk.io/cli/latest/snyk-linux -o snyk; then
        log_message "Successfully downloaded Snyk CLI"
    else
        log_message "Failed to download Snyk CLI"
        exit 1
    fi

    # Make it executable
    if chmod +x ./snyk; then
        log_message "Successfully made Snyk executable"
    else
        log_message "Failed to make Snyk executable"
        exit 1
    fi

    # Move to bin directory
    if mv ./snyk /usr/local/bin/; then
        log_message "Successfully installed Snyk to /usr/local/bin/"
    else
        log_message "Failed to move Snyk to /usr/local/bin/. You might need sudo privileges."
        exit 1
    fi
else
    log_message "Snyk is already installed. Running code test..."

    # Create filename with timestamp
    timestamp=$(date '+%Y%m%d_%H%M%S')
    output_file="snyk-report-${timestamp}.txt"

    # Run snyk test and save output
    # if SNYK_TOKEN=508d2e44-9912-44f2-8154-9df904327bdf snyk code test --org=6d941d45-d5e1-412f-97f3-8e8697c7d495 > "${output_file}" 2>&1; then
    if SNYK_TOKEN="$(SNYK_TOKEN)" snyk code test --org="$(SNYK_ORG)" > "${output_file}" 2>&1; then
        log_message "Successfully completed Snyk test. Results saved to ${output_file}"
        cat ${output_file}
    else
        log_message "Snyk test completed with some findings. Results saved to ${output_file}"
        cat ${output_file}
    fi
fi
