# -*- coding: UTF-8 -*-
from django.shortcuts import render

# Create your views here.
from core.ajax import *

from django.views.generic import View
from django.http import Http404, JsonResponse, HttpResponse
from django.shortcuts import render, render_to_response, get_object_or_404, redirect

from models import *
from mixins import *
from forms import *
from ajaxTables import *

class Index(RestauranteMixin, View):
    template = "restaurante/index.html"
    def get(self, request):
        return render(request, self.template, {})