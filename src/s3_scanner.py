import boto3
from typing import List

def find_public_buckets() -> List[str]:
    """Detect S3 buckets with public access enabled."""
    s3 = boto3.client('s3')
    public_buckets = []
    
    for bucket in s3.list_buckets()['Buckets']:
        try:
            acl = s3.get_bucket_acl(Bucket=bucket['Name'])
            if any('AllUsers' in grant['Grantee'].get('URI', '') for grant in acl['Grants']):
                public_buckets.append(bucket['Name'])
        except Exception as e:
            print(f"Error checking {bucket['Name']}: {str(e)}")
    
    return public_buckets

if __name__ == "__main__":
    print("Public buckets:", find_public_buckets())
