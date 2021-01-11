from rest_framework import permissions

class IsCustomer(permissions.BasePermission):
    def has_permission(self,request,view):
        if request.user.__class__.__name__.lower() == 'customer':
            return True
        return False    
        
class IsStaff(permissions.BasePermission):
    def has_permission(self,request,view):
        staff=request.user.staff
        if staff.is_active:
            return True
        return False



   



