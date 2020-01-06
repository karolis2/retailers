from django.http import HttpResponseRedirect
import pymongo

# Create your views here.
from django.urls import reverse
from django.views.generic import TemplateView

class MainView(TemplateView):
    template_name = "main.html"

    def post(self, request, *args, **kwargs):
        if self.request.POST.get('restricted_retailers'):
            country = request.POST.get("country", None)
            myclient = pymongo.MongoClient("mongodb://localhost:27017/")
            mydb = myclient["kp_db"]
            mycol = mydb["merchants"]
            return HttpResponseRedirect(f"/edit_property?country={country}")

        if self.request.POST.get('show_countries'):
            retailer = request.POST.get("retailer", None)
            myclient = pymongo.MongoClient("mongodb://localhost:27017/")
            mydb = myclient["kp_db"]
            mycol = mydb["merchants"]
            return HttpResponseRedirect(f"/countries?retailer={retailer}")


    def get_context_data(self, room_id=None, **kwargs):
        my_client = pymongo.MongoClient("mongodb://localhost:27017/")
        my_db = my_client["kp_db"]
        my_col = my_db["merchants"]

        restricted_cities_list = my_col.distinct('restricted')
        retailers = my_col.distinct('retailer')
        context = {'restricted_cities': restricted_cities_list,
                   'retailers': retailers
                   }

        return context

class RetailersView(TemplateView):
    template_name = "retailers.html"

    def post(self, request, *args, **kwargs):
        if self.request.POST.get('main'):
            return HttpResponseRedirect(reverse('main'))

    def get_context_data(self, property_id=None, **kwargs):
        country = self.request.GET['country']
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["kp_db"]
        mycol = mydb["merchants"]

        retailers_list = []
        for retailers in mycol.find({"restricted": country}):
            retailers_list.append(retailers["retailer"])

        context = {'retailers': retailers_list}
        return context


class RestrictedCountriesView(TemplateView):
    template_name = "restricted_countries.html"

    def post(self, request, *args, **kwargs):
        if self.request.POST.get('main'):
            return HttpResponseRedirect(reverse('main'))

    def get_context_data(self, property_id=None, **kwargs):
        retailer = self.request.GET['retailer']
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["kp_db"]
        mycol = mydb["merchants"]

        restricted_countries = mycol.find({"retailer": retailer}).distinct('restricted')

        context = {'countries': restricted_countries}
        return context
