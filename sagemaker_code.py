import boto3

# Create a low-level client representing Amazon SageMaker Runtime
sagemaker_runtime = boto3.client("sagemaker-runtime", region_name='ap-northeast-1')

# The endpoint name
endpoint_name = 'canvas-pima-deployment-09-13-2024-8-33-PM'

# Specify the content type of the input data
content_type = 'application/json'

# Gets inference from the model hosted at the specified endpoint:
response = sagemaker_runtime.invoke_endpoint(
    EndpointName=endpoint_name, 
    ContentType=content_type,
    Body=bytes('{"features": [5,140,70,33,0,33,0.5,40]}', 'utf-8')
)

# Decodes and prints the response body:
print(response['Body'].read().decode('utf-8'))

# Output = 1,0.7868633270263672,"[0.2131366729736328, 0.7868633270263672]","['0', '1']"
