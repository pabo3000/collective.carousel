from collective.carousel.tests.base import TestCase

class FieldTestCase(TestCase):
        
    def test_field_available(self):
        # Test that we have a field on objects
        self.folder.invokeFactory('Document', 'my-page')
        new_obj = getattr(self.folder, 'my-page')
        # first test newly created document
        self.failUnless(new_obj.Schema().has_key('carouselprovider'))
        # now test the personal folder
        self.failUnless(self.folder.Schema().has_key('carouselprovider'))        

    def test_field_stored(self):
        # Whether we can change the field and the value of it is getting stored
        self.setRoles('Manager',)
        self.folder.invokeFactory("Document", "test-collection")
        carouselable_col = getattr(self.folder, 'test-collection')
        new_obj = self.folder.invokeFactory('Document', 'my-page', carouselprovider=(carouselable_col,))
        new_obj = getattr(self.folder, 'my-page')
        field = new_obj.Schema().getField('carouselprovider')
        self.assertEqual(field.get(new_obj), carouselable_col)

    # def test_value_stored_in_catalog(self):
    #     self.folder.invokeFactory('Document', 'my-page', flaggedobject=True)
    #     catalog = getToolByName(self.portal, 'portal_catalog')
    #     results = catalog.searchResults(flaggedobject = True)
    #     self.assertEqual(len(results), 1)
    #     self.assertEqual(results[0].id, 'my-page')

def test_suite():
    from unittest import defaultTestLoader
    return defaultTestLoader.loadTestsFromName(__name__)