from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext

def index(request):
	return render_to_response("blogapp/index.html")



	