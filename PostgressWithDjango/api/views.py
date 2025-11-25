from rest_framework import viewsets, status
from django.http import StreamingHttpResponse
from .models import Post
from .serializers import PostSerializer
from .utils import stream_groq_response

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.order_by('-created_at')
    serializer_class = PostSerializer

    def create(self, request, *args, **kwargs):
        # Validate input
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Create post (initially no content)
        post = serializer.save()

        # Streaming generator
        def generate():
            full_text = ""

            # send tokens AS THEY COME
            for token in stream_groq_response(post.title):
                yield token
                full_text += token

            # Save final content
            post.content = full_text
            post.save()

        return StreamingHttpResponse(generate(), content_type="text/plain", status=201)
