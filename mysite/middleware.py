from mysite.models import Counter

class IncrementMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Increment the variable in the database here
        #counter, _ = Counter.objects.get_or_create(name='mycounter')
        #counter.value += 1
        #counter.save()

        response = self.get_response(request)

        return response


