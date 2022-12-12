import io
import json
from datetime import datetime
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


class Comment:
    def __init__(self, email, content):
        self.email = email
        self.content = content
        self.create = datetime.now()


comment = Comment(email='a2@gmail.com', content='some text')


class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    create = serializers.DateTimeField()


serializer = CommentSerializer(comment)
print(serializer.data)

json_comment = JSONRenderer().render((serializer.data))
# print(json_comment)`

stream = io.BytesIO(json_comment)

data = JSONParser().parse(stream)

serializer = CommentSerializer(data=data)

if serializer.is_valid():
    print(serializer.validated_data)




# dict_1 = {
#     'email':comment.email,
#     'content': comment.content,
#     'create': comment.create.strftime("%d-%m-%Y")
# }
#
# obj = json.dumps(dict_1)
#
# print(obj)
