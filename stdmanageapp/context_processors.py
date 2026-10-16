def UserDetail(request):
    if request.user.is_authenticated:
        full_name=f"{request.user.first_name} {request.user.last_name}"
    else:
        full_name=" "
    return dict(username=full_name)