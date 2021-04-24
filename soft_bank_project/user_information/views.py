from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserInformation



class DataUsingClass(APIView):
    def post(self,request):
        print('requestt', request.data)
        user = UserInformation()
        user.Full_Name = request.data['Full_Name']
        user.Address = request.data['Address']
        user.Owner_info = request.data['Owner_info']
        user.Employee_size = request.data['Employee_size']
        user.save()
        return Response("Successfuuly data saved")


class DataUpdate(APIView):
    def post(self,request):
        UserInformation.objects.filter(id = request.data["id"]).update(
            Full_Name = request.data["Full_Name"],
            Address = request.data["Address"],
            Owner_info = request.data["Owner_info"],
            Employee_size = request.data["Employee_size"]

        )
        return Response("Data Successfully updated")




class DataDelete(APIView):
    def post(self,request):
        UserInformation.objects.filter(id = request.data["id"]).delete()
        return Response ("Data successfully deleted")




