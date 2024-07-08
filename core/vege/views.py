from django.shortcuts import *  # type: ignore
from vege.models import *
# Create your views here.
def receipes(request):
    if request.method == "POST":
        data = request.POST
        receipeName = data.get('receipe_name')
        receipeDes = data.get('receipe_description')
        receipeImage = request.FILES.get('receipe_image')
        
        Receipe.objects.create(receipe_name = receipeName,
                                receipe_description = receipeDes, 
                                receipe_image = receipeImage
                                )
        
        # after the data is saved we need to refresh the page so we need to do this
        return redirect('/receipes')
        
    return render(request, "receipe.html")
