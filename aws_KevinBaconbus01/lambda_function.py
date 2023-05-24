from six_degrees_of_kevin_bacon import KevinBacon #noqa: 501 pylint: disable=wrong-import-position. import-error.line-too-long 

def lambda_handler(event, context):
    my_sd = KevinBacon('/wiki/Six_Degrees_of_Kevin_Bacon')
    my_sd.six_degrees()
    return {
        'statusCode': 200,
        'body': my_sd.as_json()
    }
