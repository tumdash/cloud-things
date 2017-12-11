## IAM permissions to run

```yaml
- 'elb:CreateLoadBalancer'
- 'elb:CreateTargetGroup'
- 'elb:RegisterTargets'
- 'elb:CreateListener'
- 'elb:DeleteLoadBalancer'
- 'elb:DeleteTargetGroup'
- 'ec2:StartInstances'
- 'ec2:RunInstances'
- 'ec2:StopInstances'
- 'ec2:TerminateInstances'
- 'ec2:CreateSecurityGroup'
- 'ec2:DeleteSecurityGroup'
- 'ec2:AuthorizeSecurityGroup*'
- 'ec2:RevokeSecurityGroup*'
- 'ec2:UpdateSecurityGroup*'
- 'ec2:AttachVolume'
- 'ec2:DetachVolume'
- 'ec2:CreateVolume'
- 'ec2:DeleteVolume'
- 'ec2:Describe*'
- 'cloudformation:*'
- 's3:*'
- 'rds:CreateDBInstance'
- 'rds:DeleteDbInstance'
```

## Deployment procedure

1. Download [AWS Cli](https://github.com/aws/aws-cli), setup it as per Getting started, check installation and configuration by ``aws ec2 describe-vpcs`` cmd

2. Create S3 bucket for deployment. Copy templates to deployment bucket
``aws s3 cp . s3://<bucket_name>/ --recursive``

3. Initiate CFN deployment
```sh
aws cloudformation create-stack --stack-name rd-stack --template-url https://s3.amazonaws.com/<bucket_name>/master.template --parameters ParameterKey=templateStorage,ParameterValue=<bucket_name> \
ParameterKey=targetVpc,ParameterValue=vpc-844c1ff4 ParameterKey=publicSubnetA,ParameterValue=subnet-00ff89e0 ParameterKey=publicSubnetB,ParameterValue=subnet-d16cf3bf \
ParameterKey=privateSubnetA,ParameterValue=subnet-96ff11f0 ParameterKey=privateSubnetB,ParameterValue=subnet-e87da2ff ParameterKey=credentials,ParameterValue=test \
ParameterKey=amiRD,ParameterValue=ami-1d2300ad ParameterKey=dbName,ParameterValue=Name ParameterKey=dbPassword,ParameterValue="passwd123675_9d" \
ParameterKey=amiFs,ParameterValue=ami-1d2356f1 ParameterKey=cidrVpc,ParameterValue="10.0.0.0/16" ParameterKey=amiNps,ParameterValue=ami-14df731
```
