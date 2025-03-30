import json
import random

def lambda_handler(event, context):
    try:
        body = json.loads(event.get('body', '{}'))
        min_val = int(body.get("min", 1))
        max_val = int(body.get("max", 100))
        random_number = random.randint(min_val, max_val)

        return {
            'statusCode': 200,
            'body': json.dumps({
                'random_number': random_number
            })
        }
    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps({
                'error': str(e)
            })
        }
# This is a simple AWS Lambda function that generates a random number between min and max values.
# It expects a JSON payload with "min" and "max" keys.
# The function returns a JSON response with the generated random number.