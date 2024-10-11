from rest_framework import permissions

class ApplicantPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.method == 'GET':
                return request.user.has_perm('applicant.view_applicant')
            elif request.method == 'GET':
                return request.user.has_perm('company.view_applicant')
            elif request.method == 'POST':
                return request.user.has_perm('applicant.add_applicant')
            elif request.method == 'PUT':
                return request.user.has_perm('applicant.change_applicant')
            elif request.method == 'DELETE':
                return request.user.has_perm('applicant.delete_applicant')
        return False

    def has_object_permission(self, request, view, obj):
        # ตรวจสอบว่าเป็นเจ้าของโปรไฟล์เมื่อแก้ไขหรือลบ (PUT, DELETE)
        if request.method == 'PUT':
            return request.user.has_perm('applicant.change_applicant') and obj.user == request.user
        elif request.method == 'DELETE':
            return request.user.has_perm('applicant.delete_applicant') and obj.user == request.user
        return False
