from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
import os
import PIL
import google.generativeai as genai

# Set up your API key
API_KEY = "AIzaSyDxIPj7B-ShgQd1OgtyDWBUQUXykigBS7c"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

def index(request):
    return render(request, "base.html")

def send_text(request):
    if request.method == "POST":
        # text_data = request.POST['val']
        image_file = request.FILES['image']

        
        fs = FileSystemStorage() 
        image_path = fs.save(image_file.name, image_file)
        full_image_path = os.path.join(fs.location, image_path)
        
     
        
        try:
            image = PIL.Image.open(full_image_path)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

        # print(text_data)
        response = model.generate_content(["this is front side of package, analyize this package and give information about product and what its advertising. ", image])
        generated_content = response.text  
        print(response)

        return JsonResponse({ 
            'status': 'success',
            # 'received_text': text_data,
            'generated_content': generated_content,
            'image_url': fs.url(image_path)
        })

    return HttpResponse("Method not allowed", status=405)


def new(request):
    return HttpResponse("Testing i am working 😂")