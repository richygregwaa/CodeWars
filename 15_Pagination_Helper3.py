# Alternative Solution 2

class PaginationHelper:
    def __init__(self, collection, items_per_page):
        self._item_count = len(collection)
        self.items_per_page = items_per_page
        self.collection = collection # RG added this

    def item_count(self):
        return self._item_count

    def page_count(self):
        return -(self._item_count // -self.items_per_page)

    def page_item_count(self, page_index):
        return min(self.items_per_page, self._item_count - page_index * self.items_per_page) \
            if 0 <= page_index < self.page_count() else -1

    def page_index(self, item_index):
        return item_index // self.items_per_page \
            if 0 <= item_index < self._item_count else -1


helper = PaginationHelper(['a', 'b', 'c', 'd', 'e','f'], 4)
print("Collection:                       " + str(helper.collection))
print("Items per page:                   " + str(helper.items_per_page))
print("Number of items:                  " + str(helper.item_count()))
print("Number of pages:                  " + str(helper.page_count()))
print("Number of Items on selected page: " + str(helper.page_item_count(1)))
print("The index selected is on page:    " + str(helper.page_index(4))) # should == 1 (zero based index)
