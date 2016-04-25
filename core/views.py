#coding: utf-8

from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from braces.views import GroupRequiredMixin, PermissionRequiredMixin


class LoginRequiredMixin(object):
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args,
                                                        **kwargs)

class PermissionRequired(PermissionRequiredMixin):
    
    def dispatch(self, request, *args, **kwargs):
        return super(PermissionRequired, self).dispatch(request, *args, **kwargs)

def group_required(*group_names):
    """Requires user membership in at least one of the groups passed in."""
    def in_groups(u):
        if u.is_authenticated():
            if bool(u.groups.filter(name__in=group_names)) | u.is_superuser:
                return True
        return False
    return user_passes_test(in_groups)