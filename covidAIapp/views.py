from django.shortcuts import render
import requests
import json

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "18fefe92ffmshb7cdd1058c970c5p1f50a4jsn5f8d46e36e0f",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()

#print(response.text)
# Create your views here.
def helloworldview(request):
    if request.method=="POST":
        countries = []
        noofresults = int(response['results'])
        for i in range(0,noofresults):
            a = response['response'][i]['country']
            countries.append(a)
        selectedcountry = request.POST['selectedcountry']
        for i in range(0,noofresults):
            if selectedcountry==response['response'][i]['country']:
                new = response['response'][i]['cases']['new']
                active = response['response'][i]['cases']['active']
                recovered = response['response'][i]['cases']['recovered']
                critical = response['response'][i]['cases']['critical']

                total = response['response'][i]['cases']['total']
                deaths = int(total) - int(active) - int(recovered)
        context = {'countries':countries, 'selectedcountry':selectedcountry, 'new_cases':new, 'active_cases':active, 'recovered_cases':recovered, 'critical_cases': critical, "total_cases":total, "deaths":deaths}
        return render(request, 'helloworld.html',context)
    
    #context = {'response': response['response'][0]}
    noofresults = int(response['results'])
    countries = []
    for i in range(0,noofresults):
        a = response['response'][i]['country']
        countries.append(a)
    context = {'countries':countries}
    #string ='Nik'
    #mylistitems = ['item1','item2','item3']
    #context = {'string':string, 'mylistitems':mylistitems}
    return render(request, 'helloworld.html',context)