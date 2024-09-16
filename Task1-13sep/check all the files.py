from google.cloud import storage

# Initialize a Cloud Storage client
client = storage.Client()

# List all the buckets in the project
buckets = client.list_buckets()

print("Buckets in project:")
for bucket in buckets:
    print(bucket.name)
