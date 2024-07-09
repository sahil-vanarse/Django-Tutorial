from django.shortcuts import *  # type: ignore
from django.http import * #type: ignore
from vege.models import *
# Create your views here.
def receipes(request):
    if request.method == "POST":
        data = request.POST
        receipeName = data.get('receipe_name')
        receipeDes = data.get('receipe_description')
        receipeImage = request.FILES.get('receipe_image')
        
        # Receipe.objects.create(receipe_name = receipeName,
        #                         receipe_description = receipeDes, 
        #                         receipe_image = receipeImage
        #                         )
        receipe = Receipe(
            receipe_name = receipeName,
            receipe_description = receipeDes, 
            receipe_image = receipeImage
        )
        receipe.save()
        
        # after the data is saved we need to refresh the page so we need to do this
        return redirect('/receipes')
    
    querySet = Receipe.objects.all()

        
    if request.GET.get('search_receipe'):
        querySet = querySet.filter(receipe_name__icontains = request.GET.get('search_receipe')
                                   )

    context = {'receipes' : querySet}
        
    return render(request, "receipe.html", context)

def delete_receipe(request, id):
    querySet = Receipe.objects.get(id = id)
    querySet.delete()
    return redirect('/receipes')

def update_receipe(request, id):
    querySet = Receipe.objects.get(id = id)
    if request.method == "POST":
        updated_receipe_name = request.POST.get('receipe_name')
        updated_receipe_description = request.POST.get('receipe_description')
        updated_receipe_image = request.FILES.get('receipe_image')

        querySet.receipe_name = updated_receipe_name
        querySet.receipe_description = updated_receipe_description

        if updated_receipe_image:
            querySet.receipe_image = updated_receipe_image

        querySet.save()
        return redirect('/receipes')


    context = {'receipe' : querySet}


    return render(request, "update_receipe.html", context)
