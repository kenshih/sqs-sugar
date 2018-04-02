import boto3

# Create SQS client
sqs = boto3.client('sqs')

import os
print()

dlq_url = os.environ['DLQ_URL']
q_url = os.environ['Q_URL']

# returns SQS response object
def send(qurl, msg):
    # Send message to SQS queue
    response = sqs.send_message(
        QueueUrl=qurl,
        DelaySeconds=10,
        MessageBody=msg
    )
    return response

# returns SQS response object
def receive(qurl):
    response = sqs.receive_message(
        QueueUrl=qurl
    )
    return response

# returns SQS response object
def delete(qurl, receipt_handle):
    response = sqs.delete_message(
        QueueUrl=qurl,
        ReceiptHandle=receipt_handle
    )
    return response


# runs

# sending a message
#print(send(dlq_url,'{"test":"test"}'))

print(receive(dlq_url))
#message = response['Messages'][0]
#receipt_handle = message['ReceiptHandle']
