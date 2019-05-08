## Goal

Check lambda, activities and Step Functions mechanism

## Deployment procedure

Using [AWS Cli](https://github.com/aws/aws-cli) for CFN deployment is easy:
```sh
# creating stack
$ aws cloudformation create-stack --stack-name sf-ingester --template-body file://ingester.yaml --parameters ParameterKey=activityName,ParameterValue=<activity_name> --profile <profile> --region <region> --capabilities CAPABILITY_IAM
$ aws cloudformation create-stack --stack-name sf-fallback --template-body file://fallback.yaml --profile <profile> --region <region> --capabilities CAPABILITY_IAM

# deleting stack
$ aws cloudformation delete-stack --stack-name sf-ingester --profile <profile> --region <region>
$ aws cloudformation delete-stack --stack-name sf-fallback --profile <profile> --region <region>
```

## FSM API

Using [AWS Cli](https://github.com/aws/aws-cli):

```sh
# start new execution of FSM instance with unique_name name of execution
$ aws stepfunctions start-execution --state-machine-arn "arn:aws:states:<region>:<account_id>:stateMachine:MyAwesomeFSM" --input "{\"ABS\":42}" --name unique_name

#obtain task activity hook
$ aws stepfunctions get-activity-task --activity-arn "arn:aws:states:<region>:<account_id>:activity:my-activity"
{
    "input": "{\"ABS\": 42}",
    "taskToken": "AAAA_restToken_=="
}

#return task result for further processing
$ aws stepfunctions send-task-success --task-token "AAAA_restToken_==" --task-output "{\"ABS\": 43}"
```
