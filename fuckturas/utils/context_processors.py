# Paths where we want to display the sidebar menu
# component.
SIDEBAR_PATHS = ('/customer/add/',
                 '/account/dashboard/',)


def sidebar_context(request):
    return {'sidebar_paths': SIDEBAR_PATHS}