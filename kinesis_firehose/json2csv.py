import csv, json, sys, io

x = """
{
	"recordid ": "easd-2412-sasd",
	"countrycode": 1,
	"groupcode": 107,
	"groupDescription": "group 1",
	"CatCode": "213",
	"state": "ACTIVE",
	"inactiveReasonCode": "",
	"userGroup": "",
	"assignee": "vlad",
	"Type": "PROD",
	"SpecialID": "r1",
	"lastUpdatedDate": "2019-05-01 22:36:57",
	"lastUpdatedBy": "mkd",
	"rvn": 12
}
"""

def plainjson2csv(json_string):
    input = json.loads(json_string)
    output = io.BytesIO()
    writer = csv.writer(output)
    writer.writerow(input.keys())
    return output.getvalue()

def lambda_handler(event, context):
    test = plainjson2csv(x)
    print("csv header=", test)
    return {
        'statusCode': 200,
        'body': 'Test is done'
    }

if __name__ =='__main__':
    lambda_handler('hello', 'world')
