from rest_framework import permissions

class CompanyPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role == 'company':
            if request.method == 'GET':
                return request.user.has_perm('company.view_company')
            elif request.method == 'POST':
                return request.user.has_perm('company.add_company')
            elif request.method == 'PUT':
                return request.user.has_perm('company.change_company')
            elif request.method == 'DELETE':
                return request.user.has_perm('company.delete_company')
        return False

    def has_object_permission(self, request, view, obj):
        # ตรวจสอบว่าเป็นเจ้าของโปรไฟล์เมื่อแก้ไขหรือลบ (PUT, DELETE)
        if request.method == 'PUT':
            return request.user.has_perm('company.change_company') and obj.user == request.user
        elif request.method == 'DELETE':
            return request.user.has_perm('company.delete_company') and obj.user == request.user
        return False
