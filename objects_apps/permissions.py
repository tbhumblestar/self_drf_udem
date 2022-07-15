from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self,request,view):
        
        admin_permission = bool(request.user and request.user.is_staff)
        return request.method == 'GET' or admin_permission

class ReviewUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self,request,view,obj):
        print("hi! from has_object_permission")
        is_reviewuser = bool(request.user == obj.review_user)
        return request.method == 'GET' or is_reviewuser