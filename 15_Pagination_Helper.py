# TODO: complete this class
# FIXME: is also a cool way to comment :) RG
import math

class PaginationHelper:

    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page


    # returns the number of items within the entire collection
    def item_count(self):
        self.items_count = len(self.collection)
        return self.items_count


    # returns the number of pages
    def page_count(self):
        self.page_counted=math.ceil(self.item_count()/self.items_per_page)
        return self.page_counted


    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        queried_page = page_index + 1
        remaining_items = self.items_count % self.items_per_page

        if queried_page > self.page_counted:
            return -1

        if queried_page < self.page_counted:
            return self.items_per_page

        if queried_page == self.page_counted and remaining_items == 0:
            return self.items_per_page

        if queried_page == self.page_counted and remaining_items > 0:
                return remaining_items


    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        self.item_index = item_index
        if self.item_index < 0 or self.item_index >= self.item_count():
            return -1
        else:
            res_page = math.floor((int(self.item_index))/self.items_per_page)
            return res_page


helper = PaginationHelper(['a', 'b', 'c', 'd', 'e','f'], 4)
print("Collection:                       " + str(helper.collection))
print("Items per page:                   " + str(helper.items_per_page))
print("Number of items:                  " + str(helper.item_count()))
print("Number of pages:                  " + str(helper.page_count()))
print("Number of Items on selected page: " + str(helper.page_item_count(1)))
print("The index selected is on page:    " + str(helper.page_index(4))) # should == 1 (zero based index)

# page_index takes an item index and returns the page that it belongs on
# helper.page_index(5)  # should == 1 (zero based index)
# helper.page_index(2)  # should == 0
# helper.page_index(20)  # should == -1
# helper.page_index(-10)  # should == -1 because negative indexes are invalid
# helper.page_count  # should == 2
# helper.item_count  # should == 6
# helper.page_item_count(0)  # should == 4
# helper.page_item_count(1)  # last page - should == 2
# helper.page_item_count(2)  # should == -1 since the page is invalid

