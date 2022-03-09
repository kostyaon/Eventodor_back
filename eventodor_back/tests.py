from django.test import TestCase
from django.contrib.auth.models import User
from .models import Category, Coordinate, Organization, Organizer, Photo, Event, Review


# Create your tests here.
class PhotoTest(TestCase):

    @classmethod
    def setUpTestData(cls):
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

class EventTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        event_photo = Photo.objects.create(url="event_url")
        event_photo.save()    

        event_coordinate = Coordinate.objects.create(
            latitude="event_latitude",
            longitude="event_longitude",
            height="event_height"
            )
        event_coordinate.save()    

        org_photo = Photo.objects.create(url="org_url")
        org_photo.save()

        event_organization = Organization.objects.create(
            name="org_name",
            description="org_description",
            phone = "org_phone",
            email ="org_email",
            bankAccount ="org_bank_account"
            )
        event_organization.save()

        event_organizer = Organizer.objects.create(
            photo_id = org_photo,
            building_id = event_organization,
            name = "organiz_name",
            surname = "organiz_surname",
            patronymic = "organiz_patronymic",
            phone = "organiz_phone",
            email = "organiz_email",
            country = "organiz_country",
            city = "organiz_city",
            address = "organiz_address",
            bankAccount = "organiz_account",
            )
        event_organizer.save()

        event_category = Category.objects.create(name="event_category")
        event_category.save()

        test_event = Event.objects.create(
            photo = event_photo,
            coordinate = event_coordinate,
            category = event_category,
            organizer = event_organizer,
            address = "test_address",
            persons_amount = 100,
            register_persons_amount = 90,
            name = "test_name",
            description = "test_description",
            time = "2018-11-20T15:58:44.767594",
            price = 100.0,
            rank = 3.0
            )
        test_event.save()
    
    def test_event_content(self):
        event_photo = Photo.objects.get(id=1)
        event_coordinate = Coordinate.objects.get(id=1)
        event_organizer = Organizer.objects.get(id=1)
        event_category = Category.objects.get(id=1)
        event = Event.objects.get(id=1)
        test_event_photo = f'{event.photo}'
        test_event_coordinate = f'{event.coordinate}'
        test_event_category = f'{event.category}'
        test_event_organizer = f'{event.organizer}'
        address = f'{event.address}'
        persons_amount = f'{event.persons_amount}'
        register_persons_amount = f'{event.register_persons_amount}'
        name = f'{event.name}'
        description = f'{event.description}'
        time = f'{event.time}'
        price = f'{event.price}'
        rank = f'{event.rank}'
        self.assertEqual(test_event_photo, event_photo.url)
        self.assertEqual(test_event_coordinate, event_coordinate.longitude)
        self.assertEqual(test_event_category, event_category.name)
        self.assertEqual(test_event_organizer, event_organizer.name)
        self.assertEqual(address, "test_address")
        self.assertEqual(persons_amount, '100')
        self.assertEqual(register_persons_amount, '90')
        self.assertEqual(name, "test_name")
        self.assertEqual(description, "test_description")
        self.assertEqual(time, "2018-11-20 15:58:44.767594+00:00")
        self.assertEqual(price, '100.0')
        self.assertEqual(rank, '3.0')

# class ReviewTest(TestCase):

#     @classmethod
#     def setUpTestData(cls):
#         event_photo = Photo.objects.create(url="event_url")
#         event_photo.save()    

#         event_coordinate = Coordinate.objects.create(
#             latitude="event_latitude",
#             longitude="event_longitude",
#             height="event_height"
#             )
#         event_coordinate.save()    

#         org_photo = Photo.objects.create(url="org_url")
#         org_photo.save()

#         event_organization = Organization.objects.create(
#             name="org_name",
#             description="org_description",
#             phone = "org_phone",
#             email ="org_email",
#             bankAccount ="org_bank_account"
#             )
#         event_organization.save()

#         event_organizer = Organizer.objects.create(
#             photo_id = org_photo,
#             building_id = event_organization,
#             name = "organiz_name",
#             surname = "organiz_surname",
#             patronymic = "organiz_patronymic",
#             phone = "organiz_phone",
#             email = "organiz_email",
#             country = "organiz_country",
#             city = "organiz_city",
#             address = "organiz_address",
#             bankAccount = "organiz_account",
#             )
#         event_organizer.save()

#         event_category = Category.objects.create(name="event_category")
#         event_category.save()

#         test_event = Event.objects.create(
#             photo = event_photo,
#             coordinate = event_coordinate,
#             category = event_category,
#             organizer = event_organizer,
#             address = "test_address",
#             persons_amount = 100,
#             register_persons_amount = 90,
#             name = "test_name",
#             description = "test_description",
#             time = "2018-11-20T15:58:44.767594",
#             price = 100.0,
#             rank = 3.0
#             )
#         test_event.save()

#         user_photo = Photo.objects.create(url="user_url")
#         user_photo.save()

#         testuser1 = User.objects.create_user(
#             username = "testUser",
#             password = "abc123",
#             photo_id = user_photo,
#             name = "user_name",
#             surname = "user_surname",
#             patronymic = "user_patronymic",
#             phone = "user_phone",
#             email = "user_email",
#             country ="user_country",
#             city = "user_city",
#             address = "user_address",
#             bankAccount = "user_bank_account"
#         )
#         testuser1.save()

#         review = Review.objects.create(
#             user_id = testuser1,
#             event_id = test_event,
#             description = "test_description",
#             rank = 3.0
#         )
#         review.save()

    
#     def test_review_content(self):
#         review_event = Event.objects.get(id=1)
#         review_user = User.objects.get(id=1)
#         review = Review.objects.get(id=1)
#         test_event = f'{review.event_id}'
#         test_user = f'{review.user_id}'
#         description = f'{review.description}'
#         rank = f'{review.rank}'
#         self.assertEqual(test_event, review_event)
#         self.assertEqual(test_user, review_user)
#         self.assertEqual(description, "test_description")
#         self.assertEqual(rank, '3.0')
