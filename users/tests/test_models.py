from django.test import TestCase
from users.models import User, Startup, Investor, Person, Industry, Sector, Status, Job, Type, Pub_or_priv, Field
from PIL import Image
import os


class StartupModelTest(TestCase):

    def setUp(self):
        Startup.objects.create(name="Andreas")


    def test_name(self):
        """
        Tests whether the object can be created with a name and keeps it.
        Tests the label of the name field.
        Tests the maximum length of the name.
        """
        andreas = Startup.objects.get(name="Andreas")
        self.assertEqual(andreas.name, "Andreas")
        field_label = andreas._meta.get_field('name').verbose_name
        self.assertEqual(field_label, "Navn")
        max_length = andreas._meta.get_field('name').max_length
        self.assertEqual(max_length, 50)

    def test_save_large_picture(self):
        """
        Tests that the save-method resizes a picture above 300x300 pixels.
        """
        large_image = Image.open("media/test_pictures/large_picture_chicken.jpg")
        original_dimensions = {"width": large_image.width, "height": large_image.height}
        # print("Testing saving large image. Should resize.")
        # print("The original small image has the dimensions width: "
        #       "{width} and height: {height}.".format(**original_dimensions))
        large_image.save("media/test_pictures/large_picture_chicken_proxy.jpg")
        large_image.close()
        Startup.objects.create(name="Large",
                                image="test_pictures/large_picture_chicken_proxy.jpg")
        small_picture_startup = Startup.objects.get(name="Large")
        saved_dimensions = {"width": small_picture_startup.image.width,
                            "height": small_picture_startup.image.height}
        # print("The small picture was saved with dimensions width: "
        #       "{width} and height: {height}.".format(**saved_dimensions))
        self.assertGreater(original_dimensions["width"], 300)
        self.assertLess(original_dimensions["height"], original_dimensions["width"])
        self.assertEqual(saved_dimensions["width"], 300)
        self.assertLess(saved_dimensions["height"], 300)

    def test_save_small_picture(self):
        """
        Tests that the save-method doesn't resize a picture within 300x300 pixels.
        """
        small_image = Image.open("media/test_pictures/small_picture_galaxy.jpg")
        original_dimensions = {"width": small_image.width, "height": small_image.height}
        # print("Testing saving small image.")
        # print("The original small image has the dimensions width: "
        #       "{width} and height: {height}.".format(**original_dimensions))
        small_image.save("media/test_pictures/small_picture_galaxy_proxy.jpg")
        small_image.close()
        Startup.objects.create(name="Small",
                                image="test_pictures/small_picture_galaxy_proxy.jpg")
        small_picture_startup = Startup.objects.get(name="Small")
        saved_dimensions = {"width": small_picture_startup.image.width,
                            "height": small_picture_startup.image.height}
        # print("The small picture was saved with dimensions width: "
        #       "{width} and height: {height}.".format(**saved_dimensions))
        self.assertEqual(original_dimensions["width"], saved_dimensions["width"])
        self.assertEqual(original_dimensions["height"], saved_dimensions["height"])

    # def test___str__(self):
    #     """
    #     Tests that __str__ returns the name field.
    #     """
    #     andreas = Startup.objects.get(name="Andreas")
    #     self.assertEqual(str(andreas), "Andreas")


class InvestorModelTest(TestCase):

    def setUp(self):
        Investor.objects.create(name="Andreas")


    def test_name(self):
        """
        Tests whether the object can be created with a name and keeps it.
        Tests the label of the name field.
        Tests the maximum length of the name.
        """
        andreas = Investor.objects.get(name="Andreas")
        self.assertEqual(andreas.name, "Andreas")
        field_label = andreas._meta.get_field('name').verbose_name
        self.assertEqual(field_label, "Navn")
        max_length = andreas._meta.get_field('name').max_length
        self.assertEqual(max_length, 50)

    def test_save_large_picture(self):
        """
        Tests that the save-method resizes a picture above 300x300 pixels.
        """
        large_image = Image.open("media/test_pictures/large_picture_chicken.jpg")
        original_dimensions = {"width": large_image.width, "height": large_image.height}
        # print("Testing saving large image. Should resize.")
        # print("The original small image has the dimensions width: "
        #       "{width} and height: {height}.".format(**original_dimensions))
        large_image.save("media/test_pictures/large_picture_chicken_proxy.jpg")
        large_image.close()
        Investor.objects.create(name="Large",
                                image="test_pictures/large_picture_chicken_proxy.jpg")
        small_picture_investor = Investor.objects.get(name="Large")
        saved_dimensions = {"width": small_picture_investor.image.width,
                            "height": small_picture_investor.image.height}
        # print("The small picture was saved with dimensions width: "
        #       "{width} and height: {height}.".format(**saved_dimensions))
        self.assertGreater(original_dimensions["width"], 300)
        self.assertLess(original_dimensions["height"], original_dimensions["width"])
        self.assertEqual(saved_dimensions["width"], 300)
        self.assertLess(saved_dimensions["height"], 300)

    def test_save_small_picture(self):
        """
        Tests that the save-method doesn't resize a picture within 300x300 pixels.
        """
        small_image = Image.open("media/test_pictures/small_picture_galaxy.jpg")
        original_dimensions = {"width": small_image.width, "height": small_image.height}
        # print("Testing saving small image.")
        # print("The original small image has the dimensions width: "
        #       "{width} and height: {height}.".format(**original_dimensions))
        small_image.save("media/test_pictures/small_picture_galaxy_proxy.jpg")
        small_image.close()
        Investor.objects.create(name="Small",
                                image="test_pictures/small_picture_galaxy_proxy.jpg")
        small_picture_investor = Investor.objects.get(name="Small")
        saved_dimensions = {"width": small_picture_investor.image.width,
                            "height": small_picture_investor.image.height}
        # print("The small picture was saved with dimensions width: "
        #       "{width} and height: {height}.".format(**saved_dimensions))
        self.assertEqual(original_dimensions["width"], saved_dimensions["width"])
        self.assertEqual(original_dimensions["height"], saved_dimensions["height"])

    # def test___str__(self):
    #     """
    #     Tests that __str__ returns the name field.
    #     """
    #     andreas = Investor.objects.get(name="Andreas")
    #     self.assertEqual(str(andreas), "Andreas")


class PersonModelTest(TestCase):

    def setUp(self):
        Person.objects.create(name="Andreas")


    def test_name(self):
        """
        Tests whether the object can be created with a name and keeps it.
        Tests the label of the name field.
        Tests the maximum length of the name.
        """
        andreas = Person.objects.get(name="Andreas")
        self.assertEqual(andreas.name, "Andreas")
        field_label = andreas._meta.get_field('name').verbose_name
        self.assertEqual(field_label, "Navn")
        max_length = andreas._meta.get_field('name').max_length
        self.assertEqual(max_length, 50)

    def test_save_large_picture(self):
        """
        Tests that the save-method resizes a picture above 300x300 pixels.
        """
        large_image = Image.open("media/test_pictures/large_picture_chicken.jpg")
        original_dimensions = {"width": large_image.width, "height": large_image.height}
        # print("Testing saving large image. Should resize.")
        # print("The original small image has the dimensions width: "
        #       "{width} and height: {height}.".format(**original_dimensions))
        large_image.save("media/test_pictures/large_picture_chicken_proxy.jpg")
        large_image.close()
        Person.objects.create(name="Large",
                                image="test_pictures/large_picture_chicken_proxy.jpg")
        small_picture_person = Person.objects.get(name="Large")
        saved_dimensions = {"width": small_picture_person.image.width,
                            "height": small_picture_person.image.height}
        # print("The small picture was saved with dimensions width: "
        #       "{width} and height: {height}.".format(**saved_dimensions))
        self.assertGreater(original_dimensions["width"], 300)
        self.assertLess(original_dimensions["height"], original_dimensions["width"])
        self.assertEqual(saved_dimensions["width"], 300)
        self.assertLess(saved_dimensions["height"], 300)

    def test_save_small_picture(self):
        """
        Tests that the save-method doesn't resize a picture within 300x300 pixels.
        """
        small_image = Image.open("media/test_pictures/small_picture_galaxy.jpg")
        original_dimensions = {"width": small_image.width, "height": small_image.height}
        # print("Testing saving small image.")
        # print("The original small image has the dimensions width: "
        #       "{width} and height: {height}.".format(**original_dimensions))
        small_image.save("media/test_pictures/small_picture_galaxy_proxy.jpg")
        small_image.close()
        Person.objects.create(name="Small",
                                image="test_pictures/small_picture_galaxy_proxy.jpg")
        small_picture_person = Person.objects.get(name="Small")
        saved_dimensions = {"width": small_picture_person.image.width,
                            "height": small_picture_person.image.height}
        # print("The small picture was saved with dimensions width: "
        #       "{width} and height: {height}.".format(**saved_dimensions))
        self.assertEqual(original_dimensions["width"], saved_dimensions["width"])
        self.assertEqual(original_dimensions["height"], saved_dimensions["height"])

    # def test___str__(self):
    #     """
    #     Tests that __str__ returns the name field.
    #     """
    #     andreas = Person.objects.get(name="Andreas")
    #     self.assertEqual(str(andreas), "Andreas")


class IndustryModelTest(TestCase):

    def test___str__(self):
        """
        Tests that __str__ returns the tag field.
        """
        Industry.objects.create(tag="Ex.-tag")
        foo = Industry.objects.get(tag="Ex.-tag")
        self.assertEqual(str(foo), "Ex.-tag")

class SectorModelTest(TestCase):

    def test___str__(self):
        """
        Tests that __str__ returns the tag field.
        """
        Sector.objects.create(tag="Ex.-tag")
        foo = Sector.objects.get(tag="Ex.-tag")
        self.assertEqual(str(foo), "Ex.-tag")

class StatusModelTest(TestCase):

    def test___str__(self):
        """
        Tests that __str__ returns the tag field.
        """
        Status.objects.create(tag="Ex.-tag")
        foo = Status.objects.get(tag="Ex.-tag")
        self.assertEqual(str(foo), "Ex.-tag")

# Relies on other classes to a too high degree, not suited for unit tests.
# class JobModelTest(TestCase):
#
#     def setUp(self):
#         User.objects.create(username="momentum")
#         Job.objects.create(employer=User.objects.get(username="momentum"), position="SCRUM Master")
#
#     def test___str__(self):
#         foo = Job.objects.get(position="SCRUM Master")
#         self.assertEqual(str(foo), "SCRUM Master")
#
#     def test_get_absolute_url(self):
#         foo = Job.objects.get(position="SCRUM Master")
#         print(foo.get_absolute_url)


class TypeModelTest(TestCase):

    def test___str__(self):
        """
        Tests that __str__ returns the tag field.
        """
        Type.objects.create(tag="Ex.-tag")
        foo = Type.objects.get(tag="Ex.-tag")
        self.assertEqual(str(foo), "Ex.-tag")

class Pub_or_privModelTest(TestCase):

    def test___str__(self):
        """
        Tests that __str__ returns the tag field.
        """
        Pub_or_priv.objects.create(tag="Ex.-tag")
        foo = Pub_or_priv.objects.get(tag="Ex.-tag")
        self.assertEqual(str(foo), "Ex.-tag")

class FieldModelTest(TestCase):

    def test___str__(self):
        """
        Tests that __str__ returns the tag field.
        """
        Field.objects.create(tag="Ex.-tag")
        foo = Field.objects.get(tag="Ex.-tag")
        self.assertEqual(str(foo), "Ex.-tag")
