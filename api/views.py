from rest_framework import status,exceptions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication,get_authorization_header

import jwt,json
from django.conf import settings
from .models import Manager,Employee
from .serializers import EmployeeSerializer,ManagerSignUpSerializer,ManagerLoginSerializer

# Manager SIGNUP API view
class ManagerSignupView(APIView):
    permission_classes = (AllowAny,)
    def post(self,request):
        serializer=ManagerSignUpSerializer(data=request.data,many=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "status":201,
            "message":"Successfully Registered",
        },status=status.HTTP_201_CREATED)

# Manager LOGIN API view
class ManagerLoginView(APIView):
    permission_classes = (AllowAny,)

    def post(self,request):
        serializer=ManagerLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({
            "status":200,
            "message":"Login Successful",
            "token":serializer.data['token']
        },status=status.HTTP_200_OK)

# Employee GetList API View
class EmployeeListView(APIView):
    #JWT Token Authentication Class
    permission_classes = (IsAuthenticated,)
    authentication_class =  JSONWebTokenAuthentication

    def get(self,request):
        try:
            # JWT Token Authentication
            token = get_authorization_header(request).decode('UTF-8').split('Bearer')[1]
            if token is None or token == "null" or token.strip() == "":
                raise exceptions.AuthenticationFailed('Authorization Header or Token is missing on Request Headers')
            decoded = jwt.decode(token.strip(), settings.JWT_AUTH['JWT_SECRET_KEY'])

            employee_detail=Employee.objects.filter(manager_id=decoded['user_id'])
            serializer=EmployeeSerializer(employee_detail,many=True)
            return Response({
                "status":200,
                "EmployeeData":serializer.data
            },status=status.HTTP_200_OK)
        except:
            return Response({
                "status": 404,
            }, status=status.HTTP_404_NOT_FOUND)

# Add Employee APIView
class AddEmployeeView(APIView):
    #JWT Token Authentication Class
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication

    def post(self,request):
        token=get_authorization_header(request).decode('UTF-8').split('Bearer')[1]
        if token is None or token == "null" or token.strip() == "":
            raise exceptions.AuthenticationFailed('Authorization Header or Token is missing on Request Headers')
        decoded=jwt.decode(token.strip(),settings.JWT_AUTH['JWT_SECRET_KEY'])
        manager_Obj=Manager.objects.get(id=decoded['user_id'])
        employee_detail={
            "manager":manager_Obj.id,
            "firstName":request.data['firstName'],
            "lastName": request.data['lastName'],
            "email": request.data['email'],
            "mobile": request.data['mobile'],
            "password":request.data['password'],
            "address":request.data['address'],
            "dob":request.data['dob'],
            "company":request.data['company'],
            "city":request.data['city'],
        }
        serializer=EmployeeSerializer(data=employee_detail,many=False)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({
            "status":201,
            "message":"Employee Created Successfully",
            "data":serializer.data
        },status=status.HTTP_201_CREATED)

# Update Employee APIView
class UpdateEmployeeView(APIView):
    #JWT Token Authentication Class
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication

    def patch(self,request):
        token = get_authorization_header(request).decode('UTF-8').split('Bearer')[1]
        if token is None or token == "null" or token.strip() == "":
            raise exceptions.AuthenticationFailed('Authorization Header or Token is missing on Request Headers')
        decoded = jwt.decode(token.strip(), settings.JWT_AUTH['JWT_SECRET_KEY'])
        updateData=json.loads(request.body)
        try:
            getEmployee=Employee.objects.get(manager_id=decoded['user_id'],id=updateData['id'])
            serializer=EmployeeSerializer(getEmployee,data=updateData,partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({
                    "status":200,
                    "message":"Updated Successfully"
                },status=status.HTTP_200_OK)
        except:
            return Response({"message":"Not Found"},status=status.HTTP_400_BAD_REQUEST)

#Delete Employee APIView
class DeleteEmployeeView(APIView):
    #JWT Token Authentication Class
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication
    def delete(self,request,pk,format=None):
        token = get_authorization_header(request).decode('UTF-8').split('Bearer')[1]
        if token is None or token == "null" or token.strip() == "":
            raise exceptions.AuthenticationFailed('Authorization Header or Token is missing on Request Headers')
        decoded = jwt.decode(token.strip(), settings.JWT_AUTH['JWT_SECRET_KEY'])
        try:
            employee=Employee.objects.get(manager_id=decoded['user_id'],pk=pk)
            employee.delete()
            return Response({'status':200},status=status.HTTP_200_OK)
        except:
            return Response({'status':404},status=status.HTTP_404_NOT_FOUND)
