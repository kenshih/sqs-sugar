
# Overview

This is a script that moves Dead Letter Queue (DLQ) messages off of DLQ and back to the original Queue. After doing so, it deletes the DLQ message.

# Prerequisites

Set env for
* AWS_ACCESS_KEY_ID <- actually, set through `aws configure` instead; this is here to remind us to make this env controlled
* AWS_SECRET_ACCESS_KEY
* Q_URL <- sqs queue
* DLQ_URL <- the dead-letter queue for above queue
```
pip install boto3
```

# To run

```
# e.g. this moves 1000 messages over from DLQ_URL to Q_URL
python dlq2q.py --num 1000
```
