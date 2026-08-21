def lambda_handler(event_type : str) :
    return "Triggering compression" if event_type == "image_upload" else "Unknown event"

result = lambda_handler("image_upload")
print(f"Result: {result}")