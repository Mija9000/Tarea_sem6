import boto3

ficheroUpload = "data.csv"
nombreBucket = "mishabuckett"

s3 = boto3.client('s3')
response = s3.upload_file(ficheroUpload, nombreBucket, "Taller_semana6/" + ficheroUpload)
print(response)

print("Ingesta completada")