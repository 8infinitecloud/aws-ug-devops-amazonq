# Crea un codigo que realice la conversion de dolares a soles.
# Luego con Amazon Q realice el refactor del codigo para que sea mas facil de leer.
import boto3

def lambda_handler(event, context):

    amount_in_dollars = event['amount']

    lambda_client = boto3.client('lambda')

    response = lambda_client.invoke(
        FunctionName='conversion_lambda_function',
        Payload={'amount': amount_in_dollars}
    )

    amount_in_soles = response['Payload'].read().decode()

    print(f'{amount_in_dollars} dólares equivale a {amount_in_soles} soles')

# Write a new function that converts a value of money in soles to dollars