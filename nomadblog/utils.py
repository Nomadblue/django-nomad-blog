from django.conf import settings


def get_post_model():
    POST_MODEL_IMPORT = getattr(settings, 'POST_MODEL', 'nomadblog.models.Post')
    POST_MODULE, dummy, POST_MODEL_NAME = POST_MODEL_IMPORT.rpartition('.')
    return getattr(__import__(POST_MODULE, fromlist=[POST_MODULE]), POST_MODEL_NAME)

