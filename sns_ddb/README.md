## Goal

Save SNS notifications to DDB options

## Schema 1

Doing SNS->Lambda->DDB single update

### DDB create

```bash
$ aws cloudformation create-stack --stack-name some-sample-ddb \
--template-body file://./ddb.yaml --profile <profile> --region <region>
```

### sns_lambda create

```bash
$ aws cloudformation create-stack --stack-name some-sns-lambda \
--template-body file://./sns_lambda.yaml --parameters ParameterKey=lambdaName,ParameterValue=simple-sns-lambda \
--profile <profile> --region <profile> --capabilities "CAPABILITY_IAM"
```

### sns_lambda update

```bash
aws cloudformation update-stack --stack-name some-sns-lambda \
--template-body file://./sns_lambda.yaml --parameters ParameterKey=lambdaName,ParameterValue=simple-sns-lambda --profile <profile> \
--region <profile> --capabilities "CAPABILITY_IAM"
```

## Schema 2

Doing SNS->SQS->Lambda(binding)->DDB batch update

### DDB create

Same as option 1

### sns_sqs_lambda create

```bash
$ aws cloudformation create-stack --stack-name some-sns-sqs-lambda \
--template-body file://./sns_sqs_lambda.yaml \
--profile <profile> --region <profile> --capabilities "CAPABILITY_IAM"
```
