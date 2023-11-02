from mongoengine import connect
from models import Quote, Author  

def search_quotes():
    while True:
        command = input("Enter a command (name: author_name, tag: tag_name, tags: tag1,tag2, exit): ")
        
        if command == 'exit':
            break
        
        if command.startswith('name:'):
            author_name = command.split(': ')[1]
            author = Author.objects(fullname=author_name).first()
            if author:
                quotes = Quote.objects(author=author)
                for quote in quotes:
                    print(quote.quote)
            else:
                print(f"No author found with the name: {author_name}")
        
        elif command.startswith('tag:'):
            tag = command.split(': ')[1].strip('"')
            quotes = Quote.objects(tags=tag)
            for quote in quotes:
                print(quote.quote)
        
        elif command.startswith('tags:'):
            tags = command.split(': ')[1].split(',')
            quotes = Quote.objects(tags__in=tags)
            for quote in quotes:
                print(quote.quote)
        
        else:
            print("Invalid command. Please use name:, tag:, tags:, or exit.")

if __name__ == "__main":
   connect(host ="mongodb+srv://IrynaHryma:2213@cluster7.oesajgi.mongodb.net/web13?retryWrites=true&w=majority",ssl= True)
   
search_quotes()
