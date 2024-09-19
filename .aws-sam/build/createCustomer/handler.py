import json
import boto3
import uuid

def handler(event, context):
    # TODO implement
        
    #try:
        eventRequestBody = json.loads(event["body"])
        
        myuuid = uuid.uuid4()
        
        #eventRequestBody.append(myuuid)
        
        customer = {
            'nombre': eventRequestBody["nombre"]
            ,'id': str(myuuid)
        }
        
        client = boto3.client('dynamodb')
        dynamodb = boto3.resource("dynamodb")
        table = dynamodb.Table('customers')
        tableName = 'customers'

        table.put_item(
            Item = {
            'nombre': eventRequestBody["nombre"]
            ,'id': str(myuuid)
        })
    
        return {
            'statusCode': 200,
            'body': json.dumps(customer)
        }
    #except Exception as e:
     #   return {
      #      'statusCode': 400,
       #     'body': e
        #}