try: 
    import google.api_core.exceptions
    import google.auth.exceptions
    from google.cloud import storage
except Exception as e:
    print("google cloud storage unavailable")
    print(str(e))


class Storage(object):
    def init(self, batch):
        self.cache_bucket_name = batch.cache_bucket_name
        self.output_bucket_name = batch.output_bucket_name

    def connect(self):
        pass

    def upload_cache(self, cache_filepath):
        """
        Uploads the file cached at cache_filepath to storage.

        Should raise an exception if the file at cache_filepath does not exist.

        Should return public_url to the file in storage if successful.
        """
        cache_filename = cache_filepath.name
        return self._upload_cache(cache_filename, cache_filepath)

    def _upload_cache(self, cache_filename, cache_filepath):
        """
        Implement this method in subclass
        """
        pass

    def download_cache(self, cache_filepath):
        """
        Download the file from storage to local file system at cache_filepath 

        Should return true if sucessful, false if file does not exist remotely
        """
        cache_filename = cache_filepath.name
        try:
            self._download_cache(cache_filename, cache_filepath)
            return True
        except Exception as e:
            print(e)
            return False

    def _download_cache(self, cache_filename, cache_filepath):
        """
        Implement this method in subclass
        """
        pass

class GoogleCloudStorage(Storage):
    def find_or_create_bucket(self, bucket_name):
        try:
            return self.storage_client.get_bucket(bucket_name)
        except google.api_core.exceptions.NotFound:
            return self.storage_client.create_bucket(bucket_name)

    def connect(self):
        self.storage_client = storage.Client()
        self.cache_storage_bucket = self.find_or_create_bucket(self.cache_bucket_name)
        self.output_storage_bucket = self.find_or_create_bucket(self.output_bucket_name)

    def _upload_cache(self, cache_filename, cache_filepath):
        blob = self.cache_storage_bucket.blob(cache_filename)
        blob.upload_from_filename(str(cache_filepath))
        return blob.public_url

    def _download_cache(self, cache_filename, cache_filepath):
        blob = self.cache_storage_bucket.blob(cache_filename)
        blob.download_to_filename(cache_filepath)