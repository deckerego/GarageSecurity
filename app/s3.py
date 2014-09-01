from boto.s3.connection import S3Connection
from boto.s3.key import Key
from config import configuration
import logging

logger = logging.getLogger('garagesec')

class S3(object):

    def __init__(self):
        self.instance_name = configuration.get('instance_name')
        self.s3conn = S3Connection(configuration.get('aws_key'), configuration.get('aws_secret'))
        self.bucket = self.s3conn.get_bucket(configuration.get('s3_bucket'))

    def upload(self, image):
        entry = Key(self.bucket)
        entry.key = "%s.jpg" % self.instance_name
        entry.set_contents_from_string(image)

        url = entry.generate_url(configuration.get('s3_url_expiry'))
        entry.copy(entry.bucket.name, entry.name, {'Content-Type':'image/jpeg'}, preserve_acl=True)
        return url
