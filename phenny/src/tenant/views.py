from django.http import HttpResponse
from tenant.models import Member

def index(request):
    return HttpResponse("You're looking at member")

def detail(request, member_id):
    member_detail = Member.objects.get(id=member_id)
    return HttpResponse("You're looking at member %s." % member_detail.name)
