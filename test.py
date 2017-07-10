def lambda_handler(event, context):
    # TODO implement
    import requests
        #global alist
        #prod url = 'http://infpwesch101.ad.unsw.edu.au/Scientia/Portal'
    url = 'http://taotesting.test.unsw.edu.au:89'

        #print "url is" + url
    try:
      
        r = requests.get(url)
        print r.status_code
        #print r

    except:

        print "error executing"
        import boto3
            
        client = boto3.client('ses', region_name='us-east-1')
        Source='itu.aws.lss.non-prod@unsw.edu.au',
        response = client.send_email(
        Source='v.koneru@unsw.edu.au',
        Destination={
            'ToAddresses': [
                'v.koneru@unsw.edu.au'
            ]
            },
            Message={
            'Subject': {
                'Data': 'URL Health Check'
            },
            'Body': {
                'Text': {
                    'Data': "Hi \n\n" + "URL http://taotesting.test.unsw.edu.au:89 is not reachable\n\n" + "Regards,\nSyllabus Plus Team"
                }
            }
            }
        )