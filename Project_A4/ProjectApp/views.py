from django.shortcuts import render

# Create your views here.




def home(request):
    return render(request, 'home.html')


def project_pagina(request):
    todos = [
        {
            "name": "test123",
            "deadline": "20-04-2013 16:17",
            "subtodos": [{"description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis at felis vitae nunc euismod molestie non et ligula. Nullam tempus, tortor eu fringilla maximus, nibh augue vehicula erat, at condimentum sapien lorem non sem. Sed fermentum hendrerit pretium. Nullam faucibus risus ac elit interdum, vel rutrum turpis rhoncus. Curabitur eget nibh in arcu auctor gravida. Phasellus porta ante non dolor scelerisque porttitor. Integer at egestas tortor. Vivamus pellentesque vehicula sagittis."} for _ in range(6)]
        } for _ in range(10)
    ]
    
    return render(request, 'project.html',{"todos":todos})


def project_toevoegen(request):
    return render(request, 'project-toevoegen.html')



