try :
    server_config = {"region": "ap-south-1", "timeout": 30}
    server_config["database_password"]
except KeyError:
    print("Security Alert: Key not found!")