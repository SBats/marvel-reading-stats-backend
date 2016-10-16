from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser, User
from users.permissions import IsAccountAdminOrReadOnly, IsSelfOrReadOnly


class IsAccountAdminOrReadOnlyTests(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.isAccountAdminOrReadOnly = IsAccountAdminOrReadOnly()
        self.normalUser = User.objects.create_user(
            username='test',
            email='test@test.fr',
            password='password')
        self.adminUser = User.objects.create_superuser(
            username='admin',
            email='admin@test.fr',
            password='password')

    def test_with_safe_method_unlogged(self):
        """
        If IsAccountAdminOrReadOnly is caled with a safe method
        it should return True to non logged users
        """
        request = self.factory.get('/')
        request.user = AnonymousUser()
        result = self.isAccountAdminOrReadOnly.has_permission(request, False)
        self.assertIs(result, True)

    def test_with_unsafe_method_unlogged(self):
        """
        If IsAccountAdminOrReadOnly is caled with an unsafe method
        it should return False to non logged users
        """
        request = self.factory.post('/')
        request.user = AnonymousUser()
        result = self.isAccountAdminOrReadOnly.has_permission(request, False)
        self.assertIs(result, False)

    def test_with_safe_method_as_normal_user(self):
        """
        If IsAccountAdminOrReadOnly is caled with a safe method
        it should return True to normal logged users
        """
        request = self.factory.get('/')
        request.user = self.normalUser
        result = self.isAccountAdminOrReadOnly.has_permission(request, False)
        self.assertIs(result, True)

    def test_with_unsafe_method_as_normal_user(self):
        """
        If IsAccountAdminOrReadOnly is caled with an unsafe method
        it should return False to normal logged users
        """
        request = self.factory.post('/')
        request.user = self.normalUser
        result = self.isAccountAdminOrReadOnly.has_permission(request, False)
        self.assertIs(result, False)

    def test_with_safe_method_as_admin_user(self):
        """
        If IsAccountAdminOrReadOnly is caled with a safe method
        it should return True to admin logged users
        """
        request = self.factory.get('/')
        request.user = self.adminUser
        result = self.isAccountAdminOrReadOnly.has_permission(request, False)
        self.assertIs(result, True)

    def test_with_unsafe_method_as_admin_user(self):
        """
        If IsAccountAdminOrReadOnly is caled with an unsafe method
        it should return True to admin logged users
        """
        request = self.factory.post('/')
        request.user = self.adminUser
        result = self.isAccountAdminOrReadOnly.has_permission(request, False)
        self.assertIs(result, True)


class IsSelfOrReadOnlyTests(TestCase):

    class RequestedObject():
        def __init__(self, user):
            self.user = user

    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.isSelfOrReadOnly = IsSelfOrReadOnly()
        self.normalUser = User.objects.create_user(
            username='test',
            email='test@test.fr',
            password='password')
        self.ownerUser = User.objects.create_user(
            username='owner',
            email='owner@test.fr',
            password='password')
        self.adminUser = User.objects.create_superuser(
            username='admin',
            email='admin@test.fr',
            password='password')
        self.requestedObj = self.RequestedObject(self.ownerUser)

    def test_with_safe_method_unlogged(self):
        """
        If IsSelfOrReadOnly is caled with a safe method
        it should return True to non logged users
        """
        request = self.factory.get('/')
        request.user = AnonymousUser()
        result = self.isSelfOrReadOnly.has_object_permission(
            request,
            False,
            self.requestedObj
        )
        self.assertIs(result, True)

    def test_with_unsafe_method_unlogged(self):
        """
        If IsSelfOrReadOnly is caled with an unsafe method
        it should return False to non logged users
        """
        request = self.factory.post('/')
        request.user = AnonymousUser()
        result = self.isSelfOrReadOnly.has_object_permission(
            request,
            False,
            self.requestedObj
        )
        self.assertIs(result, False)

    def test_with_safe_method_as_normal_user(self):
        """
        If IsSelfOrReadOnly is caled with a safe method
        it should return True to normal logged users
        """
        request = self.factory.get('/')
        request.user = self.normalUser
        result = self.isSelfOrReadOnly.has_object_permission(
            request,
            False,
            self.requestedObj
        )
        self.assertIs(result, True)

    def test_with_unsafe_method_as_normal_user(self):
        """
        If IsSelfOrReadOnly is caled with an unsafe method
        it should return False to normal logged users
        """
        request = self.factory.post('/')
        request.user = self.normalUser
        result = self.isSelfOrReadOnly.has_object_permission(
            request,
            False,
            self.requestedObj
        )
        self.assertIs(result, False)

    def test_with_safe_method_as_owner_user(self):
        """
        If IsSelfOrReadOnly is caled with a safe method
        it should return True to owner logged users
        """
        request = self.factory.get('/')
        request.user = self.ownerUser
        result = self.isSelfOrReadOnly.has_object_permission(
            request,
            False,
            self.requestedObj
        )
        self.assertIs(result, True)

    def test_with_unsafe_method_as_owner_user(self):
        """
        If IsSelfOrReadOnly is caled with an unsafe method
        it should return True to owner logged users
        """
        request = self.factory.post('/')
        request.user = self.ownerUser
        result = self.isSelfOrReadOnly.has_object_permission(
            request,
            False,
            self.requestedObj
        )
        self.assertIs(result, True)

    def test_with_safe_method_as_admin_user(self):
        """
        If IsSelfOrReadOnly is caled with a safe method
        it should return True to admin logged users
        """
        request = self.factory.get('/')
        request.user = self.adminUser
        result = self.isSelfOrReadOnly.has_object_permission(
            request,
            False,
            self.requestedObj
        )
        self.assertIs(result, True)

    def test_with_unsafe_method_as_admin_user(self):
        """
        If IsSelfOrReadOnly is caled with an unsafe method
        it should return True to admin logged users
        """
        request = self.factory.post('/')
        request.user = self.adminUser
        result = self.isSelfOrReadOnly.has_object_permission(
            request,
            False,
            self.requestedObj
        )
        self.assertIs(result, True)
