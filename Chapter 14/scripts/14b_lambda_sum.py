import json

def lambda_handler(event, context):
    body_raw = event.get('body', event if isinstance(event, dict) else '{}')
    if isinstance(body_raw, (bytes, bytearray)):
        body_raw = body_raw.decode('utf-8')
    if isinstance(body_raw, str):
        try:
            body = json.loads(body_raw) if body_raw else {}
        except json.JSONDecodeError:
            body = {}
    elif isinstance(body_raw, dict):
        body = body_raw
    else:
        body = {}
    n1 = float(body.get('num1', 0)); n2 = float(body.get('num2', 0))
    return {'statusCode': 200, 'headers': {'Content-Type':'application/json'}, 'body': json.dumps({'sum': n1+n2})}
