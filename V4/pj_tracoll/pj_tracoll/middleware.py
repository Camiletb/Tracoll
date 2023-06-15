from django.utils.deprecation import MiddlewareMixin

class VisitCounterMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Obtener la URL de la página actual
        current_url = request.path

        # Realizar el seguimiento de las visitas en alguna forma de almacenamiento (por ejemplo, en una base de datos)
        # Aquí, se utiliza un simple diccionario para mantener un contador por página
        visit_counter = getattr(request, 'visit_counter', {})
        visit_counter[current_url] = visit_counter.get(current_url, 0) + 1
        request.visit_counter = visit_counter
        print("Middleware is running!")
        print(f"Visits: {visit_counter}" )
