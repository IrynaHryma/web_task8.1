import json
from mongoengine import *


connect(host ="mongodb+srv://IrynaHryma:2213@cluster7.oesajgi.mongodb.net/web13?retryWrites=true&w=majority",ssl= True)



class Author(Document):
    fullname = StringField(required=True)
    born_date = DateField()
    born_location = StringField(max_length=50)
    description = SequenceField(max_length=50)




class Quote(Document):
    author = ReferenceField(Author,reverse_delete_rule=CASCADE)
    tags = ListField(StringField(max_length=30))
    quote= StringField(required=True)
    
    meta = {'allow_inheritance': True} 


class TextPost(Quote):
    content = StringField()



if __name__ == "__main":
    with open("author.json", "r") as author_file:
        author_data = json.load(author_file)

    
    with open("quotes.json", "r") as quotes_file:
        quotes_data = json.load(quotes_file)

    
    for author_entry in author_data:
        author_name = author_entry["fullname"]

        
        author = Author.objects(fullname=author_name).first()
        if not author:
            author = Author(**author_entry)
            author.save()

    
    for quote_entry in quotes_data:
        author_name = quote_entry["author"]

        
        author = Author.objects(fullname=author_name).first()
        if author:
            post = TextPost(author=author, **quote_entry)
            post.save()
