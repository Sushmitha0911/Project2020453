from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.card import MDCard
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.core.window import Window
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import NumericProperty
from kivymd.uix.card import MDCard
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.list import OneLineListItem
from kivy.uix.scrollview import ScrollView
from kivymd.uix.list import MDList, OneLineListItem
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton
from pdf2image import convert_from_path
from kivy.uix.image import Image
import os
import json
from kivy.properties import NumericProperty, StringProperty, ListProperty
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRaisedButton, MDIconButton
import subprocess
import sys






Window.size = (360, 640)

class BaseScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_background_image("Background.png")  # Default image, replace with your desired image

    def set_background_image(self, image_path):
        """Sets the background image for the screen."""
        self.background_image = Image(
            source=image_path,
            allow_stretch=True,
            keep_ratio=False,
            size_hint=(1, 1),
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        self.add_widget(self.background_image)

class WelcomeScreen(BaseScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Add custom widgets or labels for WelcomeScreen
        self.welcome_label = MDLabel(
            text="Petty Pro",
            halign="center",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            font_size="50sp",
            size_hint=(1, None),
            height="60dp",
            pos_hint={"center_x": 0.5, "top": 0.75}
        )
        self.add_widget(self.welcome_label)
        

        self.easier_label = MDLabel(
            text="Make It Easier",
            halign="center",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            font_size="80sp",  # Increased font size
            size_hint=(1, None),
            height="500dp",  # Adjust height for larger font
            pos_hint={"center_x": 0.5, "center_y": 0.5},  # Centered
            
        )
        self.add_widget(self.easier_label)

class RoleSelectionScreen(BaseScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_background_image("Background.png")  # Update to your image


        
        
        self.role_selection_label = MDLabel(
            text="Welcome to Petty Pro!",
            halign="center",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            font_size="20sp",
            size_hint=(1, None),
            height="40dp",
            pos_hint={"center_x": 0.5, "y": 0.8}
            
        )
        self.add_widget(self.role_selection_label)

        self.role_selection_label = MDLabel(
            text="Choose Your Role",
            halign="center",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            font_size="20sp",
            size_hint=(1, None),
            height="40dp",
            pos_hint={"center_x": 0.5, "y": 0.75}
        )
        self.add_widget(self.role_selection_label)

        

        self.applicant_button = MDRaisedButton(
            text="Petty Cash Applicant",
            pos_hint={"center_x": 0.5, "center_y": 0.6},
            on_release=self.select_applicant,
            size_hint=(0.8, None),
            height="50dp",
            md_bg_color=(0, 0, 0, 0),  # Transparent button background
            line_color=(1, 1, 1, 1),  # White border color
            line_width=2,  # Set border width
        )
        self.applicant_button.radius = [100]
        self.add_widget(self.applicant_button)
        

        self.authorized_button = MDRaisedButton(
            text="Authorized Person",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            on_release=self.select_authorized,
            size_hint=(0.8, None),
            height="50dp",
            md_bg_color=(0, 0, 0, 0),  # Transparent button background
            line_color=(1, 1, 1, 1),  # White border color
            line_width=2,  # Set border width
        )
        self.authorized_button.radius = [10]
        self.add_widget(self.authorized_button)

        self.cashier_button = MDRaisedButton(
            text="Cashier",
            pos_hint={"center_x": 0.5, "center_y": 0.4},
            on_release=self.select_cashier,
            size_hint=(0.8, None),
            height="50dp",
            md_bg_color=(0, 0, 0, 0),  # Transparent button background
            line_color=(1, 1, 1, 1),  # White border color
            line_width=2,  # Set border width
        )
        self.cashier_button.radius = [10]
        self.add_widget(self.cashier_button)

        

        

    def select_applicant(self, instance):
        self.manager.current = "login_screen"

    def select_authorized(self, instance):
        self.manager.current = "login_screen"

    def select_cashier(self, instance):
        self.manager.current = "login_screen"


class LoginScreen(BaseScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
# Define role-specific credentials here
        
        # Initialize other components like labels, input fields, buttons...

        # Set background image (replace with your actual image path)
        self.set_background_image("Background.png")
        
        # Login Text Label
        self.login_text_label = MDLabel(
            text="Login", 
            halign="center", 
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),  
            font_size="24sp", 
            font_style="H5",  
            pos_hint={"center_x": 0.5, "center_y": 0.75},  
        )
        self.add_widget(self.login_text_label)

        # Sign in Text Label
        self.signin_text_label = MDLabel(
            text="Sign in to continue.",  
            halign="center", 
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),  
            font_size="24sp",  
            pos_hint={"center_x": 0.5, "center_y": 0.70},  
        )
        self.add_widget(self.signin_text_label)

        # Email Label and Field inside a card
        self.email_label = MDLabel(
            text="EMAIL ADDRESS", 
            halign="left", 
            theme_text_color="Custom", 
            text_color=(1, 1, 1, 1),
            font_size="14sp", 
            pos_hint={"center_x": 0.6, "center_y": 0.65},
        )
        self.add_widget(self.email_label)

        email_card = MDCard(
            size_hint=(0.8, None),
            height="50dp",
            pos_hint={"center_x": 0.5, "center_y": 0.58},
            md_bg_color=(0.5, 0.5, 0.5, 1),  
            radius=[10],  
            padding=10
        )
        self.email_field = MDTextField(
            foreground_color=(1, 1, 1, 1),  
            background_color=(0, 0, 0, 0),  
            size_hint_y=None,
            height="30dp"
        )
        email_card.add_widget(self.email_field)
        self.add_widget(email_card)

        # Password Label and Field inside a card
        self.password_label = MDLabel(
            text="PASSWORD", 
            halign="left", 
            theme_text_color="Custom", 
            text_color=(1, 1, 1, 1),
            font_size="14sp", 
            pos_hint={"center_x": 0.6, "center_y": 0.51},
        )
        self.add_widget(self.password_label)

        password_card = MDCard(
            size_hint=(0.8, None),
            height="50dp",
            pos_hint={"center_x": 0.5, "center_y": 0.45},
            md_bg_color=(0.5, 0.5, 0.5, 1),  
            radius=[10],  
            padding=10
        )
        self.password_field = MDTextField(
            password=True,
            foreground_color=(1, 1, 1, 1),  
            background_color=(0, 0, 0, 0),  
            size_hint_y=None,
            height="0dp"
        )
        password_card.add_widget(self.password_field)
        self.add_widget(password_card)

        # Sign Up Button
        self.signup_button = MDRaisedButton(
            text="Sign Up",
            pos_hint={"center_x": 0.5, "center_y": 0.35},
            on_release=self.signup,
            size_hint=(0.8, None),
            height="50dp"
        )
        self.signup_button.md_bg_color = (0, 0, 0, 0)  
        self.signup_button.line_color = (1, 1, 1, 1)  
        self.signup_button.line_width = 2  
        self.signup_button.radius = [30]  
        self.add_widget(self.signup_button)

        # Back Button
        self.back_button = MDRaisedButton(
            text="Back",
            pos_hint={"center_x": 0.5, "center_y": 0.25},
            on_release=self.back,
            size_hint=(0.8, None),
            height="50dp"
        )
        self.back_button.md_bg_color = (0, 0, 0, 0)  
        self.back_button.line_color = (1, 1, 1, 1)  
        self.back_button.line_width = 2  
        self.back_button.radius = [30]  
        self.add_widget(self.back_button)

        # Error Message Label (Initially hidden)
        self.error_message = MDLabel(
            text="Invalid email or password.",
            halign="center",
            theme_text_color="Custom",
            text_color=(1, 0, 0, 1),  
            font_size="14sp",
            size_hint=(1, None),
            height="40dp",
            pos_hint={"center_x": 0.5, "y": 0.2},
            opacity=0  
        )
        self.add_widget(self.error_message)


        


    def validate_login(self, instance):
        email = self.email_field.text.strip()
        password = self.password_field.text.strip()

        # Get the selected role from the Role Selection screen
        role = self.manager.get_screen("role_selection_screen").selected_role



    def signup(self, instance):
        email = self.email_field.text.strip()
        password = self.password_field.text.strip()

        self.credentials = {
            "Petty Cash Applicant": {"email": "applicant@example.com", "password": "applicant123"},
            "Petty Cash Applicant1": {"email": "applicant1@example.com", "password": "applicant1123"},
            "Authorized Person": {"email": "authorized@example.com", "password": "authorized123"},
            "Cashier": {"email": "cashier@example.com", "password": "cashier123"},
        }

        # Check the credentials and redirect to the appropriate dashboard
        for role, credentials in self.credentials.items():
            if credentials["email"] == email and credentials["password"] == password:
                print(f"Redirecting to {role} dashboard...")

                # Navigate to the appropriate dashboard based on role
                if role == "Petty Cash Applicant":
                    self.manager.current = "dashboard_screen"  # Redirect to Petty Cash Dashboard
                elif role == "Petty Cash Applicant1":
                    self.manager.current = "dashboard_screen"  # Redirect to Petty Cash Dashboard
                elif role == "Authorized Person":
                    self.manager.current = "authorized _dashboard_screen"  # Redirect to Authorized Person Dashboard
                elif role == "Cashier":
                    self.manager.current = "cashier_dashboard_screen"  # Redirect to Cashier Dashboard
                return  # Exit after successful navigation

        # If no credentials match, show an error message
        print("Invalid email or password.")
        self.show_error_message()

    def show_error_message(self):
        self.error_message.opacity = 1  # Show the error message

    def back(self, instance):
        # Logic for the Back button
        print("Going back to previous screen...")
        self.manager.current = "role_selection_screen"  # Go back to Role Selection screen



# File to save pending requests
REQUESTS_FILE = "petty_cash_requests.json"

class DashboardScreen(Screen):
    balance = NumericProperty(0)  # Initial balance set to 1000

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_background_image("Background.png")  # Replace with your background image

        # Top App Bar displaying the balance dynamically
        self.top_bar = MDTopAppBar(
            title=f"Balance: LKR{self.balance}",
            pos_hint={"top": 1},
            elevation=10,
        )
        self.add_widget(self.top_bar)

        # Add the content label in the center of the screen
        self.content_label = MDLabel(
            text="Dashboard Content",
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )
        self.add_widget(self.content_label)

        # Create a BoxLayout for the buttons
        layout = BoxLayout(orientation='vertical', spacing=20, size_hint=(None, None))
        layout.size = (200, 150)  # Set the size of the BoxLayout
        layout.pos_hint = {'center_x': 0.5, 'center_y': 0.5}  # Center the BoxLayout

        # Create the "Request Petty Cash" button
        request_button = MDRaisedButton(
            text="Request Petty Cash",
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={"center_x": 0.5, "center_y": 0.9},
            on_release=self.request_petty_cash,
            md_bg_color=(0, 0, 0, 0),  # Transparent background
            line_color=(1, 1, 1, 1),  # White border
            line_width=2,  # Border width
        )
        request_button.radius = [25]  # Rounded corners
        layout.add_widget(request_button)

        # Create the "View Petty Cash History" button
        history_button = MDRaisedButton(
            text="View Petty Cash History",
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={"center_x": 0.5, "center_y": 0.8},
            on_release=self.view_petty_cash_history,
            md_bg_color=(0, 0, 0, 0),  # Transparent background
            line_color=(1, 1, 1, 1),  # White border
            line_width=2,  # Border width
        )
        history_button.radius = [25]  # Rounded corners
        layout.add_widget(history_button)

        # Create the "Track the Progress" button
        track_button = MDRaisedButton(
            text="Track the Progress",
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={"center_x": 0.5, "center_y": 0.7},
            on_release=self.track_progress,
            md_bg_color=(0, 0, 0, 0),  # Transparent background
            line_color=(1, 1, 1, 1),  # White border
            line_width=2,  # Border width
        )
        track_button.radius = [25]  # Rounded corners
        layout.add_widget(track_button)

        # Create the "Back to Login Screen" button
        back_button = MDRaisedButton(
            text="Back",
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={"center_x": 0.5, "center_y": 0.6},
            on_release=self.back_to_login,
            md_bg_color=(0, 0, 0, 0),  # Transparent background
            line_color=(1, 1, 1, 1),  # White border
            line_width=2,  # Border width
        )
        back_button.radius = [25]  # Rounded corners
        layout.add_widget(back_button)

        self.add_widget(layout)

    def set_background_image(self, image_path):
        """Sets the background image for the screen."""
        background = Image(
            source=image_path,
            allow_stretch=True,
            keep_ratio=False,
            size_hint=(1, 1),
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        self.add_widget(background)

    def request_petty_cash(self, instance):
     
        self.manager.current = 'request_screen'

    def add_request_to_history(self, amount):
        """Save the petty cash request to a file or list."""
        request_data = {
            "requester": "Applicant1",  # Use the actual applicant's identifier
            "amount": amount,
            "status": "pending"
        }

        # Load existing requests, add new one, and save back
        requests = self.load_petty_cash_requests()
        requests.append(request_data)
        self.save_petty_cash_requests(requests)

    def load_petty_cash_requests(self):
        """Load petty cash requests from a file."""
        if os.path.exists(REQUESTS_FILE):
            with open(REQUESTS_FILE, 'r') as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    return []
        return []

    def save_petty_cash_requests(self, requests):
        """Save petty cash requests to a file."""
        with open(REQUESTS_FILE, 'w') as file:
            json.dump(requests, file)

    def view_petty_cash_history(self, instance):
        """Handles the 'View Petty Cash History' button press."""
        print("Viewing petty cash history...")
        self.manager.current = 'history_screen'
        
    def track_progress(self, instance):
        """Handles the 'Track the Progress' button press."""
        print("Tracking progress...")
        self.manager.current = 'track_screen'

    def back_to_login(self, instance):
        """Handles the 'Back to Login' button press."""
        print("Going back to the login screen...")
        self.manager.current = 'role_selection_screen'  # Change this based on your screen structure

    def update_balance_from_request(self, amount):
        """Increases the balance based on the request."""
        self.balance += amount  # Increase balance after request
        self.update_balance_display()

    def update_balance_display(self):
        """Updates the balance display on the top bar."""
        self.top_bar.title = f"Balance: LKR{self.balance}"

    
    def get_current_amount(self):
        """Retrieve the current amount from the label."""
        try:
            return float(self.amount_label.text.split(":")[1].strip())
        except ValueError:
            return 0.0  # In case there's an issue with the amount format

    def update_amount(self, new_amount):
        """Update the amount on the Dashboard."""
        self.amount_label.text = f"Total Amount: {new_amount:.2f}"  # Update with formatted amount



class RequestScreen(BaseScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        layout = MDBoxLayout(orientation='vertical', spacing=20, padding=20)
     # Initialize balance (you can get this from a database or shared data later)
        self.balance = 0.0
        # Title Label
        title_label = MDLabel(
            text="CASH REQUISITION",
            halign="center",
            font_style="H5",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),  # White text
            size_hint_y=None,
            height=50
        )
        layout.add_widget(title_label)

        def create_text_field(hint):
            """Helper function to create a text field inside a gray card."""
            card = MDCard(
                size_hint=(0.8, None),
                height="50dp",
                pos_hint={"center_x": 0.5},
                radius=[10],  # Rounded corners
                padding=[10, 5]  # Proper padding
            )

            text_field = MDTextField(
                hint_text=hint,
                mode="fill",
                size_hint=(1, 1),  # Fills the card
                line_color_focus=(1, 1, 1, 1),  # White line when focused
                line_color_normal=(0.5, 0.5, 0.5, 0),  # Hide line when not focused
                background_color=(0, 0, 0, 0)  # Make the text field background transparent
            )

            card.add_widget(text_field)
            return card, text_field  # Return both MDCard and MDTextField

        # Create and store both the card and text field separately
        self.branch_card, self.branch_field = create_text_field("Branch")
        self.department_card, self.department_field = create_text_field("Department")
        self.date_card, self.date_field = create_text_field("Date")
        self.requirement_card, self.requirement_field = create_text_field("Requirement")
        self.rupees_card, self.rupees_field = create_text_field("Rupees")

        # Add only the cards to the layout
        layout.add_widget(self.branch_card)
        layout.add_widget(self.department_card)
        layout.add_widget(self.date_card)
        layout.add_widget(self.requirement_card)
        layout.add_widget(self.rupees_card)

        # File Manager for Petty Cash Bill Upload
        self.file_manager = MDFileManager(
            exit_manager=self.exit_file_manager,
            select_path=self.select_file
        )

        # Attachment Button
        self.attachment_button = MDRaisedButton(
            text="Attach Petty Cash Bill",
            on_release=self.attach_bill
        )
        layout.add_widget(self.attachment_button)

        # Submit Button
        submit_button = MDRaisedButton(
            text="Submit",
            pos_hint={"center_x": 0.5},
            size_hint=(None, None),
            text_color=(1, 1, 1, 1),  # White text
            line_color=(1, 1, 1, 1),  # White outline
            md_bg_color=(0, 0, 0, 0),  # Transparent background
            line_width=2,  # Border width
            on_release=self.submit_request
        )
        layout.add_widget(submit_button)
        self.add_widget(layout)

    def submit_request(self, instance):
        """Handles submission of the petty cash request."""
        missing_fields = []
        if not self.branch_field.text:
            missing_fields.append("Branch")
        if not self.department_field.text:
            missing_fields.append("Department")
        if not self.date_field.text:
            missing_fields.append("Date")
        if not self.requirement_field.text:
            missing_fields.append("Requirement")
        if not self.rupees_field.text:
            missing_fields.append("Rupees")

        if missing_fields:
            error_message = f"The following fields are required: {', '.join(missing_fields)}"
            self.show_error_message(error_message)
            return
        try:
            amount = float(self.rupees_field.text)
        except ValueError:
            self.show_error_message("Invalid amount entered.")
            return
            

        dashboard_screen = self.manager.get_screen("dashboard_screen")
        dashboard_screen.update_balance_from_request(amount)

        self.manager.current = 'success_screen'


        # ✅ Capture user input from fields
        request_id = "REQ" + str(hash(self.branch_field.text))[:4]  # Unique request ID
        branch = self.branch_field.text
        department = self.department_field.text
        date = self.date_field.text
        requirement = self.requirement_field.text
        amount = self.rupees_field.text


        

        # ✅ Pass data to SuccessScreen
        if "success_screen" in self.manager.screen_names:
            success_screen = self.manager.get_screen('success_screen')
            success_screen.display_invoice(request_id, branch, department, date, requirement, amount)
            self.manager.current = 'success_screen'
        else:
            print("❌ Error: Success screen not found!")

         # Update the balance on the dashboard after submission

        print("✅ Invoice generated successfully.")

        
  
    def submit(self, instance):
        self.manager.current = 'success_screen'

    print("Submitting petty cash request... Successfully switched to success screen.")

    
    

    def show_error_message(self, message):
        """Show the error message dialog."""
        error_popup = MDDialog(
            title="Error",
            text=message,
            size_hint=(0.8, None),
            height="200dp",
            buttons=[
                MDRaisedButton(
                    text="OK", 
                    on_release=lambda x: error_popup.dismiss()
                )
            ]
        )
        error_popup.open()

    def attach_bill(self, instance):
        print("Opening file manager to attach bill...")
        self.file_manager.show('/')  # Open file manager at root directory

    def select_file(self, path):
        print(f"Selected file: {path}")
        self.attachment_button.text = f"Attached: {path.split('/')[-1]}"
        self.exit_file_manager()

    def exit_file_manager(self, *args):
        self.file_manager.close()


     
class SuccessScreen(BaseScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.layout = MDBoxLayout(orientation="vertical", spacing=20, padding=20)

        # Title Label
        self.title_label = MDLabel(
            text="Invoice",
            halign="center",
            font_style="H4",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1)
        )
        self.layout.add_widget(self.title_label)

        # Success message label
        self.success_message_label = MDLabel(
            text="Your request has been successfully submitted!",
            halign="center",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            size_hint_y=None,
            height=50
        )
        self.layout.add_widget(self.success_message_label)

        # Invoice details label
        self.invoice_label = MDLabel(
            text="Invoice details will appear here.",
            halign="left",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            size_hint_y=None,
            height=200
        )
        self.layout.add_widget(self.invoice_label)

        # PDF clickable link
        self.pdf_link_label = MDLabel(
            text="[ref=open_invoice]Click here to open the invoice[/ref]",
            halign="center",
            text_color=(1, 1, 1, 1),
            theme_text_color="Secondary",  # Looks like a link
            markup=True
        )
        self.pdf_link_label.bind(on_ref_press=self.open_pdf_from_link)
        self.layout.add_widget(self.pdf_link_label)

        # Back Button
        self.back_button = MDRaisedButton(
            text="Back",
            pos_hint={"center_x": 0.5},
            size_hint=(None, None),
            width="200dp",
            height="50dp",
            text_color=(1, 1, 1, 1),  # White text color
            line_color=(1, 1, 1, 1),  # White border
            md_bg_color=(0, 0, 0, 0),  # Transparent background
            line_width=2,  # Border width
            on_release=self.go_to_dashboard  # Define the callback function
        )
        self.layout.add_widget(self.back_button)

        # Add layout to the screen
        self.add_widget(self.layout)

        # Store PDF path for opening
        self.pdf_path = None

    def display_success_message(self, request_id):
        """Display success message with request ID."""
        self.success_message_label.text = f"Request {request_id} has been successfully sent to the authorized person."

    def display_invoice(self, request_id, branch, department, date, requirement, amount, pdf_path=r'C:\invoices\invoice123.pdf'):
        """Generate the invoice based on request data."""
        self.pdf_path = pdf_path  # Store PDF path

        invoice_text = f"""
Invoice ID: {request_id}
Branch: {branch}
Department: {department}
Date: {date}
Requirement: {requirement}
Amount: {amount}
PDF Path: {pdf_path if pdf_path else 'Not Provided'}
"""
        self.invoice_label.text = invoice_text

        # Make the PDF link clickable
        if pdf_path:
            self.pdf_link_label.text = f"[ref=open_invoice]Click here to open the invoice[/ref]"

        # Store the submitted request for later retrieval
        if not hasattr(self.manager, "pending_requests"):
            self.manager.pending_requests = []

        self.manager.pending_requests.append({
            "requester": "Petty Cash Applicant",
            "invoice_id": request_id,
            "branch": branch,
            "department": department,
            "date": date,
            "requirement": requirement,
            "amount": amount,
        })

    def open_pdf_from_link(self, instance, ref):
        """Open the stored PDF file when the link is clicked."""
        if self.pdf_path and os.path.exists(self.pdf_path):
            self.open_pdf(self.pdf_path)
        else:
            print(f"Error: PDF file not found at {self.pdf_path}")

    def open_pdf(self, pdf_path):
        """Open the PDF file with the system's default PDF viewer."""
        try:
            if sys.platform == "win32":
                os.startfile(pdf_path)  # Windows
            elif sys.platform == "darwin":
                subprocess.run(["open", pdf_path], check=True)  # macOS
            else:
                subprocess.run(["xdg-open", pdf_path], check=True)  # Linux
        except Exception as e:
            print(f"Error opening PDF: {e}")


    def go_to_dashboard(self, instance):
        """Navigate back to the Dashboard screen."""
        self.manager.current = 'dashboard_screen'  # Switch to dashboard screen

    def go_to_invoice_details(self, dt):
        """Navigate to InvoiceDetailsScreen and pass request data."""
        # Assuming you're passing the first request, adjust if necessary
        if self.manager.pending_requests:
            request = self.manager.pending_requests[-1]  # Get the latest request
            
            # Ensure the data is passed to the InvoiceDetailsScreen
            invoice_screen = self.manager.get_screen('invoice_details_screen')
            invoice_screen.display_invoice_details(request)

        # Switch to Invoice Details screen
        self.manager.current = 'invoice_details_screen'
    

class HistoryScreen(BaseScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
   

   
        layout = MDBoxLayout(orientation='vertical', spacing=20, padding=20)
        layout.add_widget(MDLabel(text="View Petty Cash History", halign="auto"))

        title_container = MDBoxLayout(size_hint_y=None, height=50) 
        title_label = MDLabel(
            text="View Petty Cash History",
            halign="center",
            font_style="H5",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1)  # White text
        )
        title_container.add_widget(title_label)
        layout.add_widget(title_container)  # Add the container first so it stays at the top
        
        # Add buttons for filtering the requests
        button_layout = MDBoxLayout(size_hint_y=None, height=50, spacing=10)
        
        completed_button = MDRaisedButton(
            text="Completed Requests",
            size_hint=(None, None),
            size=("200dp", "50dp"),
            text_color=(1, 1, 1, 1),  # White text
            line_color=(1, 1, 1, 1),  # White outline
            md_bg_color=(0, 0, 0, 0),  # Transparent background
            line_width=2,  # Border width
            on_release=self.filter_history_completed
        )
        rejected_button = MDRaisedButton(
            text="Rejected Requests",
            size_hint=(None, None),
            size=("200dp", "50dp"),
            text_color=(1, 1, 1, 1),  # White text
            line_color=(1, 1, 1, 1),  # White outline
            md_bg_color=(0, 0, 0, 0),  # Transparent background
            line_width=2,  # Border width
            on_release=self.filter_history_rejected
        )
        
        button_layout.add_widget(completed_button)
        button_layout.add_widget(rejected_button)
        layout.add_widget(button_layout)

        # Scrollable List
        scroll = ScrollView()
        self.list_view = MDList()
        scroll.add_widget(self.list_view)

        # Add ScrollView to layout
        layout.add_widget(scroll)

        back_button = MDRaisedButton(
            text="Back",
            pos_hint={"center_x": 0.5},
            size_hint=(None, None),
            text_color=(1, 1, 1, 1),  # White text
            line_color=(1, 1, 1, 1),  # White outline
            md_bg_color=(0, 0, 0, 0),  # Transparent background
            line_width=2,  # Border width
            on_release=self.go_to_dashboard  # Correct function reference
        )

        layout.add_widget(back_button)
        self.add_widget(layout)


        # Initially load all data
        self.petty_cash_data = [
            {"status": "completed", "request": "Meal Expenses - 1090.45 - Completed"},
            {"status": "rejected", "request": "Travelling Expenses - 1233.67 - Rejected"},
            
        ]
        self.load_history()  # Load all records initially

    def filter_history_completed(self, instance):
        """Filter and show only completed requests."""
        filtered_data = [record for record in self.petty_cash_data if record['status'] == 'completed']
        self.load_history(filtered_data)

    def filter_history_rejected(self, instance):
        """Filter and show only rejected requests."""
        filtered_data = [record for record in self.petty_cash_data if record['status'] == 'rejected']
        self.load_history(filtered_data)

    def load_history(self, filtered_data=None):
        """Load petty cash requests into the list."""
        self.list_view.clear_widgets()  # Clear old data

        # Use filtered data if provided, else show all records
        data_to_load = filtered_data if filtered_data else self.petty_cash_data

        if not data_to_load:
            self.list_view.add_widget(OneLineListItem(
            text="No records found",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1)  # White text color
        ))
        else:
            for record in data_to_load:
                item = OneLineListItem(
                text=f"{record['request']}",
                theme_text_color="Custom",
                text_color=(1, 1, 1, 1)  # White text color
            )
            self.list_view.add_widget(item)

    def update_history(self, new_data):
        """Update petty cash history dynamically."""
        self.petty_cash_data.append(new_data)
        self.load_history()

    def go_to_dashboard(self, instance):
        """Handles back button press and navigates to Dashboard."""
        print("Navigating to Dashboard Screen...")
        self.manager.current = "dashboard_screen"  # Ensure dashboard_screen is added in ScreenManager


class TrackingScreen(BaseScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = MDBoxLayout(orientation="vertical", spacing=10, padding=20)
        
        self.title = MDLabel(
            text="Tracking Requests",
            halign="center",
            font_style="H4",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1)
        )
        self.layout.add_widget(self.title)
        
        self.tracking_label = MDLabel(
            text="No requests tracked yet.",
            halign="center",
            font_style="H6",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1)
        )
        self.layout.add_widget(self.tracking_label)
        
        self.add_widget(self.layout)

    def update_tracking(self, record_text):
        """Update tracking with the new request details."""
        self.tracking_label.text = record_text


class AuthorizedDashboardScreen(BaseScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Main Layout (Vertical)
        self.main_layout = MDBoxLayout(
            orientation="vertical",
            spacing=20,
            padding=20,
            size_hint=(1, 1),  
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        self.add_widget(self.main_layout)

        # Title Label
        self.dashboard_label = MDLabel(
            text="NOTIFICATION",
            halign="center",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),  
            font_size="24sp",
        )
        self.main_layout.add_widget(self.dashboard_label)

        # Scrollable Notification Layout
        self.scroll_view = ScrollView(
            size_hint=(1, None),
            height="400dp",
            bar_width=5,
            scroll_type=['bars', 'content']
        )
        
        self.notification_layout = MDBoxLayout(
            orientation="vertical",
            spacing=10,
            padding=20,
            size_hint_y=None,
        )
        self.notification_layout.bind(minimum_height=self.notification_layout.setter('height'))
        
        self.scroll_view.add_widget(self.notification_layout)
        self.main_layout.add_widget(self.scroll_view)

        # Back Button
        self.back_button = MDRaisedButton(
            text="Back",
            size_hint=(None, None),
            text_color=(1, 1, 1, 1),
            line_color=(1, 1, 1, 1),
            md_bg_color=(0, 0, 0, 0),
            line_width=2,
            height="50dp",
            pos_hint={"center_x": 0.5},
            on_release=self.back_to_role_selection
        )
        self.main_layout.add_widget(self.back_button)

    def back_to_role_selection(self, instance):
        """Navigate back to the Role Selection Screen."""
        self.manager.current = "role_selection_screen"

    def on_enter(self):
        """Refresh notifications when the screen is entered."""
        self.load_notifications()

    def load_notifications(self):
        """Load and display pending requests as notifications."""
        self.notification_layout.clear_widgets()

        if hasattr(self.manager, "pending_requests"):
            for request in self.manager.pending_requests:
                self.create_notification_box(request)

    def create_notification_box(self, request):
        """Create a notification box for each request."""
        if not request or "requester" not in request or "invoice_id" not in request:
            return  

        # Box for Notification
        notification_box = MDBoxLayout(
            orientation="vertical",
            spacing=10,
            size_hint=(None, None),
            width="300dp",
            height="200dp",
            pos_hint={"center_x": 0.5},
        )

        # Notification Text Button
        notification_text = f"New Request: {request['requester']}\nInvoice ID: {request['invoice_id']}"
        notification_button = MDRaisedButton(
            text=notification_text,
            size_hint=(None, None),
            height="50dp",
            width="250dp",
            pos_hint={"center_x": 0.5},
            on_release=lambda instance: self.view_invoice_details(request),
            md_bg_color=(0, 0, 0, 0),
            line_color=(1, 1, 1, 1),
            line_width=2,
            text_color=(1, 1, 1, 1),
        )

        # Layout for Approve & Reject buttons
        button_layout = MDBoxLayout(
            orientation="horizontal",
            spacing=10,
            size_hint=(None, None),
            width="250dp",
            height="50dp",
            pos_hint={"center_x": 0.5},
        )

        approve_button = MDRaisedButton(
            text="Approve",
            size_hint=(None, None),
            height="40dp",
            width="100dp",
            text_color=(1, 1, 1, 1),
            line_color=(1, 1, 1, 1),
            md_bg_color=(0, 0, 0, 0),
            line_width=2,
            pos_hint={"center_x": 0.5},
            on_release=lambda instance: self.approve_request(request),
        )
        
        reject_button = MDRaisedButton(
            text="Reject",
            size_hint=(None, None),
            height="40dp",
            width="100dp",
            text_color=(1, 1, 1, 1),
            line_color=(1, 1, 1, 1),
            md_bg_color=(0, 0, 0, 0),
            line_width=2,
             pos_hint={"center_x": 0.5},
            on_release=lambda instance: self.reject_request(request),
        )

        # Add buttons to horizontal layout
        button_layout.add_widget(approve_button)
        button_layout.add_widget(reject_button)

        # Add widgets to the notification box
        notification_box.add_widget(notification_button)
        notification_box.add_widget(button_layout)

        # Add notification box to the layout
        self.notification_layout.add_widget(notification_box)

    def approve_request(self, request):
        """Approve the request and remove the notification."""
        print(f"Approved Invoice ID: {request['invoice_id']}")
        self.remove_notification(request)

    def reject_request(self, request):
        """Reject the request and remove the notification."""
        print(f"Rejected Invoice ID: {request['invoice_id']}")
        self.remove_notification(request)

    def remove_notification(self, request):
        """Remove the notification and update the screen."""
        self.manager.pending_requests.remove(request)
        self.load_notifications()  

    def view_invoice_details(self, request):
        """Navigate to Invoice Details Screen."""
        print(f"Viewing details for Invoice ID: {request['invoice_id']}")
        if "invoice_details_screen" in self.manager.screen_names:
            invoice_screen = self.manager.get_screen("invoice_details_screen")
            invoice_screen.display_invoice_details(request)
            self.manager.current = "invoice_details_screen"
            
class PettyProApp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(DashboardScreen(name="dashboard_screen"))
        # Add other screens as needed
        return sm
    
    
STATUS_FILE = "status.json"  # File to store approval/rejection status

def save_status(status):
    """Save the approval/rejection status to a file."""
    data = {"status": status}
    with open(STATUS_FILE, "w") as f:
        json.dump(data, f)
    print(f"Status saved: {status}")

def load_status():
    """Load the approval/rejection status from the file."""
    if os.path.exists(STATUS_FILE):
        with open(STATUS_FILE, "r") as f:
            data = json.load(f)
            print(f"Loaded status: {data}")
            return data.get("status", None)
    print("No status file found.")
    return None      

STATUS_FILE = "status_file.txt"  # Path to store the status (approved/rejected)


class InvoiceDetailsScreen(BaseScreen): 
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Layout
        self.layout = MDBoxLayout(orientation="vertical", spacing=20, padding=20)

        # Title Label
        self.title_label = MDLabel(
            text="Invoice Details",
            halign="center",
            font_style="H4",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
        )
        self.layout.add_widget(self.title_label)

        # Invoice Details Label
        self.details_label = MDLabel(
            text="Invoice details will appear here.",
            halign="left",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            size_hint_y=None,
            height=100,
            markup=True,
        )
        self.layout.add_widget(self.details_label)

        # Scrollable PDF Image Container
        self.scroll = ScrollView()
        self.pdf_container = BoxLayout(orientation="vertical", size_hint_y=None)
        self.scroll.add_widget(self.pdf_container)
        self.layout.add_widget(self.scroll)

        # Add layout to screen
        self.add_widget(self.layout)


        # PDF clickable link
        self.pdf_link_label = MDLabel(
            text="[ref=open_invoice]Click here to open the invoice[/ref]",
            halign="center",
            text_color=(1, 1, 1, 1),
            theme_text_color="Secondary",  # Looks like a link
            markup=True
        )
        self.pdf_link_label.bind(on_ref_press=self.open_pdf_from_link)
        self.layout.add_widget(self.pdf_link_label)


        
        self.back_button = MDRaisedButton(
            text="Back",
            size_hint=(None, None),
            text_color=(1, 1, 1, 1),  # White text
            line_color=(1, 1, 1, 1),  # White outline
            md_bg_color=(0, 0, 0, 0),  # Transparent background
            line_width=2,  # Border width
            height="50dp",
            on_release=self.back_to_dashboard
        )
        self.layout.add_widget(self.back_button)

    def display_invoice_details(self, request):
        """Display invoice details on the screen."""
        invoice_id = request.get("invoice_id", "N/A")
        branch = request.get("branch", "N/A")
        department = request.get("department", "N/A")
        date = request.get("date", "N/A")
        requirement = request.get("requirement", "N/A")
        amount = request.get("amount", "N/A")
        pdf_path = request.get("pdf_path", r'C:\invoices\invoice123.pdf')  # Default path if not provided

        # Store the PDF path as an instance attribute
        self.pdf_path = pdf_path

        # Update Invoice Details
        self.details_label.text = (
            f"[b]Invoice ID:[/b] {invoice_id}\n"
            f"[b]Branch:[/b] {branch}\n"
            f"[b]Department:[/b] {department}\n"
            f"[b]Date:[/b] {date}\n"
            f"[b]Requirement:[/b] {requirement}\n"
            f"[b]Amount:[/b] {amount}\n"
            f"[b]PDF Path:[/b] {pdf_path}"
        )

        # Make the PDF link clickable
        if pdf_path:
            self.pdf_link_label.text = f"[ref=open_invoice]Click here to open the invoice[/ref]"

    def open_pdf_from_link(self, instance, ref):
        """Open the stored PDF file when the link is clicked."""
        if self.pdf_path and os.path.exists(self.pdf_path):
            self.open_pdf(self.pdf_path)
        else:
            print(f"Error: PDF file not found at {self.pdf_path}")

    def open_pdf(self, pdf_path):
        """Open the PDF file with the system's default PDF viewer."""
        try:
            if sys.platform == "win32":
                os.startfile(pdf_path)  # Windows
            elif sys.platform == "darwin":
                subprocess.run(["open", pdf_path], check=True)  # macOS
            else:
                subprocess.run(["xdg-open", pdf_path], check=True)  # Linux
        except Exception as e:
            print(f"Error opening PDF: {e}")


    def show_notification(self, message):
        """Display a notification on the screen."""
        notification_label = MDLabel(
            text=message,
            halign="center",
            theme_text_color="Custom",
            text_color=(1, 0, 0, 1),  # Red text for the notification
        )
        self.layout.add_widget(notification_label)
        # Optionally, remove the notification after a few seconds
        Clock.schedule_once(lambda dt: self.layout.remove_widget(notification_label), 5)

    def load_notification(self):
        """Load the notification when user logs in."""
        status = load_status()
        if status == "approved":
            self.show_notification("Request Approved")
        elif status == "rejected":
            self.show_notification("Request Rejected")

    def logout(self):
        """Clear the status on logout."""
        if os.path.exists(STATUS_FILE):
            os.remove(STATUS_FILE)
        self.manager.current = "login_screen"  # Go to the login screen

    def clear_notification_from_authorized_dashboard(self):
        """Clear notification from the Authorized Dashboard when action is taken."""
        # Assuming the Authorized Dashboard has a method to remove notifications
        if self.manager.has_screen("authorized_dashboard_screen"):
            auth_dashboard = self.manager.get_screen("authorized_dashboard_screen")
            auth_dashboard.clear_notifications()

    def send_notification_to_applicant(self, message):
        """Send a notification to the Applicant's Dashboard when approved or rejected."""
        if self.manager.has_screen("applicant_dashboard_screen"):
            applicant_dashboard = self.manager.get_screen("applicant_dashboard_screen")
            applicant_dashboard.display_notification(message)

    def approve_request(self, instance):
        """Approve the request and update notifications."""
        save_status("approved")  # Save the approval status
        self.clear_notification_from_authorized_dashboard()  # Remove from Authorized Dashboard
        self.manager.current = "approved_screen"  # Go to Approved Screen

        # Optionally send notification to the Applicant's Dashboard
        self.send_notification_to_applicant("Your request has been approved!")

    def reject_request(self, instance):
        """Reject the request and update notifications."""
        save_status("rejected")  # Save the rejection status
        self.clear_notification_from_authorized_dashboard()  # Remove from Authorized Dashboard
        self.manager.current = "rejected_screen"  # Go to Rejected Screen

        # Send notification to the Applicant's Dashboard
        self.send_notification_to_applicant("Your request has been rejected!")

    def back_to_dashboard(self, instance):
            """Navigate back to the Authorized Dashboard Screen."""
            self.manager.current = "authorized _dashboard_screen"  # Ensure this matches your ScreenManager name


class ApprovedScreen(BaseScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Create a vertical layout
        layout = MDBoxLayout(orientation="vertical", spacing=20, padding=20)
        
        # Add a label showing that the request is approved
        approved_label = MDLabel(
            text="Request Approved!",
            halign="center",
            font_style="H4",
            theme_text_color="Custom",
            text_color=(0, 1, 0, 1)  # Green text
        )
        layout.add_widget(approved_label)
        
        # Add a Back button to return to the previous screen
        back_button = MDRaisedButton(
            text="Back",
            size_hint=(None, None),
            width="300dp",
            height="50dp",
            on_release=self.go_back,
            md_bg_color=(0, 0, 0, 0),   # Transparent background
            text_color=(1, 1, 1, 1),     # White text
            line_color=(1, 1, 1, 1),     # White outline
            line_width=2                # Border width
        )
        layout.add_widget(back_button)
        
        # Add the layout to the screen
        self.add_widget(layout)

    def go_back(self, instance):
        """Navigate back to the Invoice Details Screen (or any designated screen)."""
        self.manager.current = "invoice_details_screen"

class RejectedScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Create a vertical layout
        layout = MDBoxLayout(orientation="vertical", spacing=20, padding=20)
        
        # Add a label indicating the request was rejected
        rejected_label = MDLabel(
            text="Request Rejected!",
            halign="center",
            font_style="H4",
            theme_text_color="Custom",
            text_color=(1, 0, 0, 1)  # Red text for rejection
        )
        layout.add_widget(rejected_label)
        
        # Add a Back button to return to the Invoice Details screen
        back_button = MDRaisedButton(
            text="Back",
            size_hint=(None, None),
            width="300dp",
            height="50dp",
            on_release=self.go_back,
            md_bg_color=(0, 0, 0, 0),   # Transparent background
            text_color=(1, 1, 1, 1),     # White text
            line_color=(1, 1, 1, 1),     # White border
            line_width=2                # Border width
        )
        layout.add_widget(back_button)
        
        # Add the layout to the screen
        self.add_widget(layout)
    
    def go_back(self, instance):
        """Navigate back to the Invoice Details Screen (or another screen)."""
        self.manager.current = "invoice_details_screen"  # Update this name as needed

APPROVED_REQUESTS_FILE = "approved_requests.json"

class CashierDashboardScreen(BaseScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Main Layout (Vertical)
        self.main_layout = MDBoxLayout(
            orientation="vertical",
            spacing=20,
            padding=20,
            size_hint=(1, 1),  
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        self.add_widget(self.main_layout)

        # Title Label
        self.dashboard_label = MDLabel(
            text="NOTIFICATION",
            halign="center",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),  
            font_size="24sp",
        )
        self.main_layout.add_widget(self.dashboard_label)

        # Scrollable Notification Layout
        self.scroll_view = ScrollView(
            size_hint=(1, None),
            height="400dp",
            bar_width=5,
            scroll_type=['bars', 'content']
        )
        
        self.notification_layout = MDBoxLayout(
            orientation="vertical",
            spacing=10,
            padding=20,
            size_hint_y=None,
        )
        self.notification_layout.bind(minimum_height=self.notification_layout.setter('height'))
        
        self.scroll_view.add_widget(self.notification_layout)
        self.main_layout.add_widget(self.scroll_view)

        # Back Button
        self.back_button = MDRaisedButton(
            text="Back",
            size_hint=(None, None),
            text_color=(1, 1, 1, 1),
            line_color=(1, 1, 1, 1),
            md_bg_color=(0, 0, 0, 0),
            line_width=2,
            height="50dp",
            pos_hint={"center_x": 0.5},
            on_release=self.back_to_role_selection
        )
        self.main_layout.add_widget(self.back_button)

    def back_to_role_selection(self, instance):
        """Navigate back to the Role Selection Screen."""
        self.manager.current = "role_selection_screen"

    def on_enter(self):
        """Refresh notifications when the screen is entered."""
        self.load_notifications()

    def load_notifications(self):
        """Load and display pending requests as notifications."""
        self.notification_layout.clear_widgets()

        if hasattr(self.manager, "pending_requests"):
            for request in self.manager.pending_requests:
                self.create_notification_box(request)

    def create_notification_box(self, request):
        """Create a notification box for each request."""
        if not request or "requester" not in request or "invoice_id" not in request:
            return  

        # Box for Notification
        notification_box = MDBoxLayout(
            orientation="vertical",
            spacing=10,
            size_hint=(None, None),
            width="300dp",
            height="200dp",
            pos_hint={"center_x": 0.5},
        )

        # Notification Text Button
        notification_text = f"New Request: {request['requester']}\nInvoice ID: {request['invoice_id']}"
        notification_button = MDRaisedButton(
            text=notification_text,
            size_hint=(None, None),
            height="50dp",
            width="250dp",
            pos_hint={"center_x": 0.5},
            on_release=lambda instance: self.view_invoice_details(request),
            md_bg_color=(0, 0, 0, 0),
            line_color=(1, 1, 1, 1),
            line_width=2,
            text_color=(1, 1, 1, 1),
        )

        # Layout for Approve & Reject buttons
        button_layout = MDBoxLayout(
            orientation="horizontal",
            spacing=10,
            size_hint=(None, None),
            width="250dp",
            height="50dp",
            pos_hint={"center_x": 0.5},
        )

        approve_button = MDRaisedButton(
            text="Approve",
            size_hint=(None, None),
            height="40dp",
            width="100dp",
            text_color=(1, 1, 1, 1),
            line_color=(1, 1, 1, 1),
            md_bg_color=(0, 0, 0, 0),
            line_width=2,
            pos_hint={"center_x": 0.5},
            on_release=lambda instance: self.approve_request(request),
        )
        
        reject_button = MDRaisedButton(
            text="Reject",
            size_hint=(None, None),
            height="40dp",
            width="100dp",
            text_color=(1, 1, 1, 1),
            line_color=(1, 1, 1, 1),
            md_bg_color=(0, 0, 0, 0),
            line_width=2,
             pos_hint={"center_x": 0.5},
            on_release=lambda instance: self.reject_request(request),
        )

        # Add buttons to horizontal layout
        button_layout.add_widget(approve_button)
        button_layout.add_widget(reject_button)

        # Add widgets to the notification box
        notification_box.add_widget(notification_button)
        notification_box.add_widget(button_layout)

        # Add notification box to the layout
        self.notification_layout.add_widget(notification_box)

    def approve_request(self, request):
        """Approve the request and remove the notification."""
        print(f"Approved Invoice ID: {request['invoice_id']}")
        self.remove_notification(request)

    def reject_request(self, request):
        """Reject the request and remove the notification."""
        print(f"Rejected Invoice ID: {request['invoice_id']}")
        self.remove_notification(request)

    def remove_notification(self, request):
        """Remove the notification and update the screen."""
        self.manager.pending_requests.remove(request)
        self.load_notifications()  

    def view_invoice_details(self, request):
        """Navigate to Invoice Details Screen."""
        print(f"Viewing details for Invoice ID: {request['invoice_id']}")
        if "invoice_details_screen" in self.manager.screen_names:
            invoice_screen = self.manager.get_screen("cashier_invoice_details_screen")
            invoice_screen.display_invoice_details(request)
            self.manager.current = "cashier_invoice_details_screen"


class CashierInvoiceDetailsScreen(BaseScreen): 
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Layout
        self.layout = MDBoxLayout(orientation="vertical", spacing=20, padding=20)

        # Title Label
        self.title_label = MDLabel(
            text="Invoice Details",
            halign="center",
            font_style="H4",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
        )
        self.layout.add_widget(self.title_label)

        # Invoice Details Label
        self.details_label = MDLabel(
            text="Invoice details will appear here.",
            halign="left",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            size_hint_y=None,
            height=100,
            markup=True,
        )
        self.layout.add_widget(self.details_label)

        # Scrollable PDF Image Container
        self.scroll = ScrollView()
        self.pdf_container = BoxLayout(orientation="vertical", size_hint_y=None)
        self.scroll.add_widget(self.pdf_container)
        self.layout.add_widget(self.scroll)

        # Add layout to screen
        self.add_widget(self.layout)


         # PDF clickable link
        self.pdf_link_label = MDLabel(
            text="[ref=open_invoice]Click here to open the invoice[/ref]",
            halign="center",
            text_color=(1, 1, 1, 1),
            theme_text_color="Secondary",  # Looks like a link
            markup=True
        )
        self.pdf_link_label.bind(on_ref_press=self.open_pdf_from_link)
        self.layout.add_widget(self.pdf_link_label)

        

        
        self.back_button = MDRaisedButton(
            text="Back",
            size_hint=(None, None),
            text_color=(1, 1, 1, 1),  # White text
            line_color=(1, 1, 1, 1),  # White outline
            md_bg_color=(0, 0, 0, 0),  # Transparent background
            line_width=2,  # Border width
            height="50dp",
            on_release=self.back_to_dashboard
        )
        self.layout.add_widget(self.back_button)

        

    def display_invoice_details(self, request):
        """Display invoice details on the screen."""
        invoice_id = request.get("invoice_id", "N/A")
        branch = request.get("branch", "N/A")
        department = request.get("department", "N/A")
        date = request.get("date", "N/A")
        requirement = request.get("requirement", "N/A")
        amount = request.get("amount", "N/A")
        pdf_path = request.get("pdf_path", r'C:\invoices\invoice123.pdf')  # Default path if not provided
        approval_status = request.get("approval_status", "Approved")  # Status: Approved, Rejected, or Pending

        # Store the PDF path as an instance attribute
        self.pdf_path = pdf_path

        # Update Invoice Details
        self.details_label.text = (
            f"[b]Invoice ID:[/b] {invoice_id}\n"
            f"[b]Branch:[/b] {branch}\n"
            f"[b]Department:[/b] {department}\n"
            f"[b]Date:[/b] {date}\n"
            f"[b]Requirement:[/b] {requirement}\n"
            f"[b]Amount:[/b] {amount}\n"
            f"[b]PDF Path:[/b] {pdf_path}\n"
            f"[b]Approval Status:[/b] {approval_status}"  # Display Approval Status
        )

        # Make the PDF link clickable
        if pdf_path:
            self.pdf_link_label.text = f"[ref=open_invoice]Click here to open the invoice[/ref]"

    def open_pdf_from_link(self, instance, ref):
        """Open the stored PDF file when the link is clicked."""
        if self.pdf_path and os.path.exists(self.pdf_path):
            self.open_pdf(self.pdf_path)
        else:
            print(f"Error: PDF file not found at {self.pdf_path}")

    def open_pdf(self, pdf_path):
        """Open the PDF file with the system's default PDF viewer."""
        try:
            if sys.platform == "win32":
                os.startfile(pdf_path)  # Windows
            elif sys.platform == "darwin":
                subprocess.run(["open", pdf_path], check=True)  # macOS
            else:
                subprocess.run(["xdg-open", pdf_path], check=True)  # Linux
        except Exception as e:
            print(f"Error opening PDF: {e}")

    def show_notification(self, message):
        """Display a notification on the screen."""
        notification_label = MDLabel(
            text=message,
            halign="center",
            theme_text_color="Custom",
            text_color=(1, 0, 0, 1),  # Red text for the notification
        )
        self.layout.add_widget(notification_label)
        # Optionally, remove the notification after a few seconds
        Clock.schedule_once(lambda dt: self.layout.remove_widget(notification_label), 5)

    def load_notification(self):
        """Load the notification when user logs in."""
        status = load_status()
        if status == "approved":
            self.show_notification("Request Approved")
        elif status == "rejected":
            self.show_notification("Request Rejected")

    def logout(self):
        """Clear the status on logout."""
        if os.path.exists(STATUS_FILE):
            os.remove(STATUS_FILE)
        self.manager.current = "login_screen"  # Go to the login screen

    def clear_notification_from_cashier_dashboard(self):
        """Clear notification from the Cashier Dashboard when action is taken."""
        # Assuming the Authorized Dashboard has a method to remove notifications
        if self.manager.has_screen("cashier_dashboard_screen"):
            auth_dashboard = self.manager.get_screen("cashier_dashboard_screen")
            auth_dashboard.clear_notifications()

    def send_notification_to_applicant(self, message):
        """Send a notification to the Applicant's Dashboard when approved or rejected."""
        if self.manager.has_screen("applicant_dashboard_screen"):
            applicant_dashboard = self.manager.get_screen("applicant_dashboard_screen")
            applicant_dashboard.display_notification(message)

    def approve_request(self, instance):
        """Approve the request and update notifications."""
        # Update the status
        save_status("approved")  # Save the approval status
        
        # Update the amount in the Dashboard screen
        self.update_dashboard_amount()
        
        # Clear notifications and navigate to the approved screen
        self.clear_notification_from_cashier_dashboard()  # Remove from Authorized Dashboard
        self.manager.current = "approved_screen"  # Go to Approved Screen

        # Optionally send notification to the Applicant's Dashboard
        self.send_notification_to_applicant("Your request has been approved!")

    def update_dashboard_amount(self):
        """Reduce the amount in the Dashboard when request is approved."""
        if self.manager.has_screen("dashboard_screen"):
            dashboard_screen = self.manager.get_screen("dashboard_screen")
            
            # Retrieve the current total amount in the dashboard
            current_amount = dashboard_screen.get_current_amount()  # Assuming this method exists
            amount_to_deduct = float(self.details_label.text.split("Amount:")[1].split("\n")[0].strip())  # Extract amount
            
            # Deduct the amount
            new_amount = current_amount - amount_to_deduct
            
            # Update the Dashboard screen with the new amount
            dashboard_screen.update_amount(new_amount)  # Assuming this method exists to update the displayed amount

    def reject_request(self, instance):
        """Reject the request and update notifications."""
        save_status("rejected")  # Save the rejection status
        self.clear_notification_from_authorized_dashboard()  # Remove from Authorized Dashboard
        self.manager.current = "rejected_screen"  # Go to Rejected Screen

        # Send notification to the Applicant's Dashboard
        self.send_notification_to_applicant("Your request has been rejected!")

    def back_to_dashboard(self, instance):
            """Navigate back to the Authorized Dashboard Screen."""
            self.manager.current = "cashier_dashboard_screen"  # Ensure this matches your ScreenManager name


class NotificationScreen(BaseScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Layout
        self.layout = MDBoxLayout(orientation="vertical", spacing=20, padding=20)

        # Title Label
        self.title_label = MDLabel(
            text="Notifications",
            halign="center",
            font_style="H4",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
        )
        self.layout.add_widget(self.title_label)

        # Notification Label (Initially Hidden)
        self.notification_label = MDLabel(
            text="",
            halign="center",
            theme_text_color="Custom",
            text_color=(1, 0, 0, 1),  # Red text for rejection notification
            size_hint_y=None,
            height=50,
            opacity=0  # Hidden initially
        )
        self.layout.add_widget(self.notification_label)

        # Acknowledge Button to remove notification
        self.acknowledge_button = MDRaisedButton(
            text="Acknowledge Notification",
            size_hint=(None, None),
            text_color=(1, 1, 1, 1),
            line_color=(1, 1, 1, 1),
            md_bg_color=(0, 0, 0, 0),
            line_width=2,
            height="50dp",
            on_release=self.clear_notification
        )
        self.layout.add_widget(self.acknowledge_button)

        # Back Button
        self.back_button = MDRaisedButton(
            text="Back",
            size_hint=(None, None),
            text_color=(1, 1, 1, 1),
            line_color=(1, 1, 1, 1),
            md_bg_color=(0, 0, 0, 0),
            line_width=2,
            height="50dp",
            on_release=self.back_to_dashboard
        )
        self.layout.add_widget(self.back_button)

        # Add layout to screen
        self.add_widget(self.layout)

        # Load notification when screen is opened
        self.load_notification()

    def load_notification(self):
        """Load notification for the applicant when a request is rejected."""
        status = load_status()
        if status == "rejected":
            self.notification_label.text = "Your request has been rejected"
            self.notification_label.opacity = 1  # Show notification

    def clear_notification(self, instance):
        """Clear the notification when acknowledged."""
        self.notification_label.text = ""
        self.notification_label.opacity = 0  # Hide notification
        save_status("")  # Reset status

    def back_to_dashboard(self, instance):
        """Navigate back to the applicant dashboard."""
        self.manager.current = "dashboard_screen"  # Update as needed


class TrackingScreen(BaseScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Layout setup
        self.layout = MDBoxLayout(orientation="vertical", spacing=20, padding=20)

        # Title Label
        self.title_label = MDLabel(
            text="Request Tracking",
            halign="center",
            font_style="H4",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
        )
        self.layout.add_widget(self.title_label)

        # Step 1: Authorized Person Approval
        self.step1_label = MDLabel(
            text="Step 1: Request - Submitted",  # Default text
            halign="left",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
        )
        self.layout.add_widget(self.step1_label)


        # Step 1: Authorized Person Approval
        self.step2_label = MDLabel(
            text="Step 2: Authorized Approval - Approved",  # Default text
            halign="left",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
        )
        self.layout.add_widget(self.step2_label)

        # Step 2: Cashier Approval
        self.step3_label = MDLabel(
            text="Step 3: Cashier Approval - Approved",  # Default text
            halign="left",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
        )
        self.layout.add_widget(self.step3_label)

        # Additional Request Information
        self.details_scroll = ScrollView()
        self.details_container = BoxLayout(orientation="vertical", size_hint_y=None)
        self.details_scroll.add_widget(self.details_container)
        self.layout.add_widget(self.details_scroll)

        # Back button
        self.back_button = MDRaisedButton(
            text="Back",
            size_hint=(None, None),
            text_color=(1, 1, 1, 1),  # White text
            line_color=(1, 1, 1, 1),  # White outline
            md_bg_color=(0, 0, 0, 0),  # Transparent background
            line_width=2,  # Border width
            height="50dp",
            halign="center",
            on_release=self.back_to_dashboard  # Handle the back action
        )
        self.layout.add_widget(self.back_button)

        # Add layout to screen
        self.add_widget(self.layout)

    def update_request_status(self, step, status):
        """Update the status of the request for the given step."""
        if step == 1:
            self.step1_label.text = f"Step 1: Authorized Person Approval - {status}"
        elif step == 2:
            self.step2_label.text = f"Step 2: Cashier Approval - {status}"

    def back_to_dashboard(self, instance):
        """Navigate back to the previous screen (e.g., dashboard)."""
        self.manager.current = "dashboard_screen"  # Adjust this to your actual screen name




class MyScreenManager(ScreenManager):
    pass

class PettyPro(MDApp):
    def build(self):
        screen_manager = ScreenManager()
        
        # Add screens
        screen_manager.add_widget(WelcomeScreen(name="welcome_screen"))
        screen_manager.add_widget(RoleSelectionScreen(name="role_selection_screen"))
        screen_manager.add_widget(LoginScreen(name="login_screen"))
        screen_manager.add_widget(DashboardScreen(name="dashboard_screen"))
        screen_manager.add_widget(RequestScreen(name="request_screen"))
        screen_manager.add_widget(HistoryScreen(name="history_screen"))
        screen_manager.add_widget(TrackingScreen(name="track_screen"))
        screen_manager.add_widget(SuccessScreen(name="success_screen"))
        screen_manager.add_widget(AuthorizedDashboardScreen(name="authorized _dashboard_screen"))
        screen_manager.add_widget(InvoiceDetailsScreen(name="invoice_details_screen"))
        screen_manager.add_widget(ApprovedScreen(name="approved_screen"))
        screen_manager.add_widget(RejectedScreen(name="rejected_screen"))
        screen_manager.add_widget(CashierDashboardScreen(name="cashier_dashboard_screen"))
        screen_manager.add_widget(CashierInvoiceDetailsScreen(name="cashier_invoice_details_screen"))
        screen_manager.add_widget(NotificationScreen(name="notification_screen"))

        
        Clock.schedule_once(self.switch_to_role_selection, 2)
        return screen_manager

    def switch_to_role_selection(self, dt):
        self.root.current = "role_selection_screen"




PettyPro().run()
