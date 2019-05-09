## Goal

Build SQS->Lambda->Kinesis->firehose->S3bucket pipeline

### Manually create SQS

### Create pipeline

```bash
$ aws cloudformation create-stack --stack-name pipeline \
--template-body file://./processing_pipeline.yaml --parameters \
ParameterKey=queueArn,ParameterValue=<arn-created-step-1-queue>  \
ParameterKey=bucketName,ParameterValue=<unique-bucket-name-for-delivery> \
--profile <profile> --region <region> --capabilities "CAPABILITY_IAM"
```

### Template defaults

Template defines set of parameters which could be used for customized deployment.
See parameters section of CFN for details
