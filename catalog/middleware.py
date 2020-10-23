from django.utils.deprecation import MiddlewareMixin


class GetSession(MiddlewareMixin):

    def process_request(self, request):
        if 'items' in request.session:
            item_list = request.session['items']
            request.item_list = item_list
