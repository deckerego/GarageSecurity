import os, inspect, subprocess
import logging
import re
import time, datetime
import thread
from PIL import Image
from config import configuration

logger = logging.getLogger('media')
date_pattern = re.compile('^[0-9]{4}-[0-9]{2}-[0-9]{2}$')
image_pattern = re.compile('.*\.thumb\.jpg$')
video_pattern = re.compile('.*\.mp4$')

class Media(object):
    name = 'media'
    keyword = 'media'

    # This is invoked when installed as a Bottle plugin
    def setup(self, app):
        self.routes = app

        for other in app.plugins:
            if not isinstance(other, Media):
                continue
            if other.keyword == self.keyword:
                raise PluginError("Found another instance of Media running!")

    # This is invoked within Bottle as part of each route when installed
    def apply(self, callback, route):
        args = inspect.getargspec(callback)[0]
        if self.keyword not in args:
            return callback

        def wrapper(*args, **kwargs):
            kwargs[self.keyword] = self
            rv = callback(*args, **kwargs)
            return rv
        return wrapper

    # De-installation from Bottle as a plugin
    def close(self):
        logger.info("Closing Media Connection")

    def get_files(self, archive_date):
    	if not date_pattern.match(archive_date):
    		raise ValueError('Archive dates must be in ISO format yyyy-mm-dd')

    	archive_dir = "%s/%s" % (configuration.get('webcam_archive'), archive_date)
    	dirpath, dirnames, filenames = next(os.walk(archive_dir))

    	image_files = filter(lambda f: image_pattern.match(f), filenames)
        image_files = sorted(image_files, key=lambda f: f[7:10])

    	video_files = filter(lambda f: video_pattern.match(f), filenames)
        video_files = sorted(video_files, key=lambda f: f[7:10])

        # FIXME Undefined behavior if we don't have matching video files for each image file
        return zip(image_files, video_files)

    def get_dates(self):
    	archive_dir = configuration.get('webcam_archive')
    	dirpath, dirnames, filenames = next(os.walk(archive_dir))
        archive_dates = filter(lambda f: date_pattern.match(f), dirnames)
        return sorted(archive_dates, reverse=True)

    def save_thumbnail(self, file_path):
        filename = os.path.basename(file_path)[:-4]
        dirname = os.path.dirname(file_path)

        image = Image.open(file_path)
        image.thumbnail((640,360), Image.NEAREST)
        image.save("%s/%s.thumb.jpg" % (dirname, filename))

    def __threaded_transcode(self, file_path):
        filename = os.path.basename(file_path)[:-4]
        dirname = os.path.dirname(file_path)
        dest_file = "%s/%s.mp4" % (dirname, filename)

        subprocess.check_call(["avconv", "-i", file_path, "-vcodec", "h264", "-acodec", "aac", "-strict", "-2", dest_file])
        os.remove(file_path)

    def transcode(self, file_path):
        thread.start_new_thread(self.__threaded_transcode, (file_path, ))

class PluginError(Exception):
    pass

Plugin = Media
