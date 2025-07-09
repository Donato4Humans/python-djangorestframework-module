REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PAGINATION_CLASS': 'core.pagination.PagePagination',# implemented custom DB pagination class
    # 'PAGE_SIZE': 2
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend', # implemented lib for DB filter
    ),
}