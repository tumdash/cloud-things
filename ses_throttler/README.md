## Goal

Make SES outbound throttler based on scheduled events for Lambda

## Schema

Create FIFO SQS for queueing mail jobs. CRM producer puts jobs into queue, while
Lambda based on periodical scheduled event consume SQS and initiate SES calling

### SQS, Lambda and event create

```bash
$ aws cloudformation create-stack --stack-name ses-throttler \
--template-body file://./ses_throttler.yaml --profile <profile> --region <region> --capabilities "CAPABILITY_IAM"
```

### feed SQS as following:

```bash
nick@ubuntu:$ aws sqs send-message \
--queue-url https://<queue-url>/sample-queue.fifo --message-body 'my_message'
\c--message-group-id 'master' --profile <profile> --region <region>
{
    "MD5OfMessageBody": "11112222333344445555ffff66667777",
    "SequenceNumber": "11122233344455566677",
    "MessageId": "aaaabbbb-cccc-dddd-eeee-ffff11112222"
}
```
