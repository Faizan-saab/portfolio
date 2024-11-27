from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Blog, Project
from .serializers import BlogSerializer, ProjectSerializer

# Create your views here.

class ProjectList(APIView):
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
    
class BlogList(APIView):
    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)


