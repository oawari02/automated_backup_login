backup_data = {
    "Web_Server" : "Success",
    "DB_Server" : "Failed",
    "Mail_Server" : "Success"
}

def generate_log(data):
    try:
        log_file = open("backup_log.txt", "w")
        for key, value in data.items():
            log_file.write(f"{key} status is {value}\n")
        log_file.close()
    except:
        print("Error: Could not save the log file!")

generate_log(backup_data)