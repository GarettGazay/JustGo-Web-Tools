from rides.models import FormBasic

def run():
    #test
    data = FormBasic.objects.all()
    data.delete()
    # Gather most recent database entry
