from django.test import TestCase
from django.contrib.auth.models import User
from .models import Category, Coordinate, Organization, Organizer, Photo


# Create your tests here.
class PhotoTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Create a user
        testuser1 = User.objects.create_user(username='testuser1', password='abc123')
        testuser1.save()

        test_photo = Photo.objects.create(url="test_url")
        test_photo.save()
    
    def test_photo_content(self):
        photo = Photo.objects.get(id=1)
        url = f'{photo.url}'
        self.assertEqual(url, 'test_url')

class OrganizationTest(TestCase):

    @classmethod
    def setUpTestData(cls):      
        test_organization = Organization.objects.create(
            name="test_name",
            description="test_description",
            phone = "test_phone",
            email ="test_email",
            bankAccount ="test_bank_account"
            )
        test_organization.save()
    
    def test_organization_content(self):
        organization = Organization.objects.get(id=1)
        name = f'{organization.name}'
        description = f'{organization.description}'
        phone = f'{organization.phone}'
        email = f'{organization.email}'
        bankAccount = f'{organization.bankAccount}'
        self.assertEqual(name, 'test_name')
        self.assertEqual(description, 'test_description')
        self.assertEqual(phone, 'test_phone')
        self.assertEqual(email, 'test_email')
        self.assertEqual(bankAccount, 'test_bank_account')

class OrganizerTest(TestCase):

    @classmethod
    def setUpTestData(cls):  
        test_photo = Photo.objects.create(url="photo_url")
        test_photo.save()

        test_organization = Organization.objects.create(
            name="org_name",
            description="org_description",
            phone = "org_phone",
            email ="org_email",
            bankAccount ="org_bank_account"
            )
        test_organization.save()

        test_organizer = Organizer.objects.create(
            photo_id = test_photo,
            building_id = test_organization,
            name = "test_name",
            surname = "test_surname",
            patronymic = "test_patronymic",
            phone = "test_phone",
            email = "test_email",
            country = "test_country",
            city = "test_city",
            address = "test_address",
            bankAccount = "test_bank_account",
            )
        test_organizer.save()
    
    def test_organizer_content(self):
        organizer = Organizer.objects.get(id=1)
        photo = Photo.objects.get(id=1)
        organization = Organization.objects.get(id=1)
        photo_url = f'{photo.url}'
        building_name = f'{organization.name}'
        building_description = f'{organization.description}'
        building_phone = f'{organization.phone}'
        building_email = f'{organization.email}'
        building_bankAccount = f'{organization.bankAccount}'
        name = f'{organizer.name}'
        surname = f'{organizer.surname}'
        patronymic = f'{organizer.patronymic}'
        phone = f'{organizer.phone}'
        email = f'{organizer.email}'
        country = f'{organizer.country}'
        city = f'{organizer.city}'
        address = f'{organizer.address}'
        bankAccount = f'{organizer.bankAccount}'
        self.assertEqual(photo_url, "photo_url")
        self.assertEqual(building_name, "org_name")
        self.assertEqual(building_description, "org_description")
        self.assertEqual(building_phone, "org_phone")
        self.assertEqual(building_email, "org_email")
        self.assertEqual(building_bankAccount, "org_bank_account")
        self.assertEqual(name, 'test_name')
        self.assertEqual(surname, 'test_surname')
        self.assertEqual(patronymic, 'test_patronymic')
        self.assertEqual(phone, 'test_phone')
        self.assertEqual(email, 'test_email')
        self.assertEqual(country, 'test_country')
        self.assertEqual(city, 'test_city')
        self.assertEqual(address, 'test_address')
        self.assertEqual(bankAccount, 'test_bank_account')

class CategoryTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name="test_category")
        test_category.save()
    
    def test_category_content(self):
        category = Category.objects.get(id=1)
        name = f'{category.name}'
        self.assertEqual(name, 'test_category')

class CoordinateTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_coordinate = Coordinate.objects.create(
            latitude="test_latitude",
            longitude="test_longitude",
            height="test_height"
            )
        test_coordinate.save()
    
    def test_coordinate_content(self):
        coordinate = Coordinate.objects.get(id=1)
        latitude = f'{coordinate.latitude}'
        longitude = f'{coordinate.longitude}'
        height = f'{coordinate.height}'
        self.assertEqual(height, 'test_height')