from ._anvil_designer import singleTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class single(singleTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.drop_down_1.items = {
      rooms['sroom'] for rooms in app_tables.rooms.search()
    }


    # Any code you write here will run before the form opens.

  def link_1_click(self, **event_args):
    open_form('menu')

  def button_1_click(self, **event_args):
    open_form('booking')
    anvil.server.call(
      'add_info2', 
      self.drop_down_1.selected_value,
      self.drop_down_2.selected_value
    )
    

  def drop_down_2_change(self, **event_args):
    """This method is called when an item is selected"""
    pass

