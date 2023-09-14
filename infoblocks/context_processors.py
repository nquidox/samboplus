from infoblocks.models import InfoBlock


def extras(request):
    infoblocks = InfoBlock.objects.all()
    return {'infoblocks': infoblocks}