from django.test import TestCase
from django.contrib.auth import get_user_model

class CustomUserTests(TestCase):
     def test_new_superuser(self):
        db = get_user_model()
        super_user = db.objects.create_superuser('testuser@gmail.com','username',7843046748,'password')
        self.assertEqual(super_user.email,'testuser@gmail.com')
        self.assertEqual(super_user.user_name,'username')
        self.assertEqual(super_user.contact_number,7843046748)
        self.assertEqual(super_user.is_superuser)
        self.assertEqual(super_user.is_staff)
        self.assertEqual(super_user.is_active)
        self.assertEqual(str(super_user),'username')


        


