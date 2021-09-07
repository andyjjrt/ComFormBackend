from django.http.response import JsonResponse

class APIResponse():
    def success(data=None):
        return JsonResponse({"error": None, "data": data})
    def error(msg="error"):
        return JsonResponse({"error": "error", "data": msg})