import boto3, json, sys, io

def inject_sqs_msg(queue_url, group_id, source, destination, template):
    ses_msg = {
        'source': source,
        'destinations': [{'Destination':{'ToAddresses':[destination]}}],
        'template': template
    },
    input_msg = json.dumps(ses_msg)
    sqs = boto3.client('sqs')
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=input_msg,
        DelaySeconds=0,
        MessageGroupId=group_id
    )
    return response['MessageId']

if __name__ =='__main__':
    if len(sys.argv) == 5:
        group_id='master'
        out_id = inject_sqs_msg(sys.argv[1], group_id,
                                sys.argv[2], sys.argv[3], sys.argv[4])
        print ("Message", out_id, "injected")
    else:
        print ("wrong parameters number", len(sys.argv))
