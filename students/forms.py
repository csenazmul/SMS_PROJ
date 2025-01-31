from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'phone', 'course', 'address']
        labels = {
            'name': 'Full Name',
            'email': 'Email Address',
            'phone': 'Phone Number',
            'course': 'Course',
            'address': 'Address'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'course': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'})
        }
# The StudentForm class is a Django form class that inherits from forms.ModelForm.  
# It has a nested Meta class that defines the model and fields of the form.
# The model attribute is set to Student, which is the model we created earlier.
# The fields attribute is set to a list of fields that we want to include in the form.
# The labels attribute is a dictionary that maps field names to their display names.
# The widgets attribute is a dictionary that maps field names to their corresponding form widgets.
# The form widgets are used to render the form fields in the HTML template.
# In this case, we are using TextInput for text input fields and Textarea for text area fields.
# The attrs attribute of the form widgets is used to add CSS classes to the form fields.
# This allows us to style the form fields using CSS.
# The StudentForm class is used to create a form for adding and editing student records in the database.
# We will use this form in the views to handle form submission and validation.
# Next, we will create a template to render the form in the browser.
# Create a new file called student_form.html in the templates/students directory and add the following code:
#   
