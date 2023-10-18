#Call Required Libraries
import os
import csv
import pandas as pd
from kivymd.app import MDApp
from kivy.lang import Builder

#Call KivyMD Function and load widgets
class MainApp(MDApp):
    def build(self):
        self.title = "Daily Issues Status Report"
        self.icon = "Report_icon.png"
        return Builder.load_string('''
GridLayout:
   cols:2
   spacing: dp(1)
   padding: dp(100)
   MDLabel:
      id: l_1
      text: "Ticket ID :"
   MDTextField:
      id: t_1
      hint_text: "Ticket ID"                          
   MDLabel:
      id: l_3
      text: "Employee Name :"
   MDTextField:
      id: t_2
      hint_text: "Username or Empolyee Name"  
   MDLabel:
      id: l_3
      text: "Email ID :"
   MDTextField:
      id: t_3
      hint_text: "Email ID"
   MDLabel:
      id: l_4
      text: "Issue :"
   MDTextField:
      id: t_4
      hint_text: "Issue"
   MDLabel:
      id: l_5
      text: "Status :"
   MDTextField:
      id: t_5
      hint_text: "Status"
   MDRaisedButton:
      text: "Submit"
      on_release: app.save_to_csv()
   MDRaisedButton:
      text: "Clear"
      on_release: app.Clearance()

''') 

#Create function for save as CSV
    def save_to_csv(self, *args):
       data = {
        'TicketID': self.root.ids.t_1.text,
        'EmployeeName': self.root.ids.t_2.text,
        'Emailid': self.root.ids.t_3.text,
        'Issue': self.root.ids.t_4.text,
        'Status': self.root.ids.t_5.text,
    }
       df = pd.DataFrame(data, index=[0])
       if not os.path.isfile('Daily_Individual_Report_Gen.csv'):
            df.to_csv('Daily_Individual_Report_Gen.csv', index=False)
       else:
            df.to_csv('Daily_Individual_Report_Gen.csv', mode='a', header=False, index=False)

    def Clearance(self, *args):
               data = {
               't_1': self.root.ids.t_1.text,
               't_2': self.root.ids.t_2.text,
               't_3': self.root.ids.t_3.text,
               't_4': self.root.ids.t_4.text,
               't_5': self.root.ids.t_5.text,
            }       
               # Clear all text fields
               for key in data.keys():
                  id_key = key
                  if id_key in self.root.ids:
                     self.root.ids[id_key].text = ''

#create Main function
if __name__ == "__main__":
    MainApp().run()
