from django.shortcuts import render, redirect
from .forms import WheelItemForm
from .models import WheelItem
from django.core.serializers import serialize

def wheel_view(request):
    if request.method == 'POST':
        form = WheelItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('wheel')  # Replace 'wheel' with the actual name of your URL pattern.
    else:
        form = WheelItemForm()

    items = WheelItem.objects.all()
    items_json = serialize('json', items)  # Serialize the queryset to JSON
    context = {
        'form': form,
        'items_json': items_json  # Pass the serialized JSON to the context
    }
    
    return render(request, 'spinning_wheel/wheel.html', context)
