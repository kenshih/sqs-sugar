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

def mvOne(source, target):
    # get a msg off of dlq
    fromDlq = receive(source)
    # grab body
    body = ???
    # send body to normal q

    # if ^ success, delete orig dlq msg, otherwise fail with output

# runs

# sending a message
#print(send(dlq_url,'{"test":"test with anna here"}'))

# receive a message
#print(receive(dlq_url))

# receive and delete
'''
getone = receive(dlq_url)
print("resp from receive: %s" % getone)
receipt_handle = getone['Messages'][0]['ReceiptHandle']
print(receipt_handle)
resp = delete(dlq_url, receipt_handle)
print("resp from delete: %s" % resp)
'''
