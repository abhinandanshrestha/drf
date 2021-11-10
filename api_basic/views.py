from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
# from django.http import JsonResponse
# from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from rest_framework import generics,mixins

class GenericAPIView(mixins.DestroyModelMixin,generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin):
    serializer_class = ArticleSerializer
    queryset=Article.objects.all()

    lookup_field = 'id'

    def get(self,request,id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self,request):
        return self.create(request)

    def put(self,request,id):
        return self.update(request,id)

    def delete(self,request,id):
        self.destroy(request,id)

# Create your views here.

#classbased API View
# class ArticleAPIView(APIView):
#     def get(self,request):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)

#     def post(self,request):
#         serializer = ArticleSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)






#for specific article details
# class ArticleDetailAPIView(APIView):
#     def get_object(self,id):
#         try:
#              return Article.objects.get(id=id)
#         except Article.DoesNotExist:
#             return HttpResponse(status=status.HTTP_404_NOT_FOUND)

#     def get(self,request,id):
#         article = self.get_object(id)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)
    
#     def put(self,request,id):
#         article=self.get_object(id)
#         serializer=ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

#     def delete(self,request,id):
#         article = self.get_object(id)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)









# @api_view(['GET','POST'])
# def article_list(request):

#     if request.method == 'GET':
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         # return JsonResponse(serializer.data, safe=False)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         # data = JSONParser().parse(request)
#         serializer = ArticleSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             # return JsonResponse(serializer.data,status=201)
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         # return JsonResponse(serializer.errors,status=400)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# localhost:8000/article/<id>
# @csrf_exempt
# @api_view(['GET','POST','DELETE'])
# def specificArticle(request,pk):
#     try:
#         article = Article.objects.get(pk=pk)
#     except Article.DoesNotExist:
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)


#     elif request.method == 'POST':
#         serializer=ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)


#     elif request.method == 'DELETE':
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)