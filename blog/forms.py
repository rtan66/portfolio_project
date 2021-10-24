

from django import forms

class CommentForm(forms.Form):

    """"
    Django forms are very similar to models. 
    A form consists of a class where the class 
    attributes are form fields. Django comes 
    with some built-in form fields that you 
    can use to quickly create the form you need.

    For this form, the only fields you’ll need 
    are author, which should be a CharField, 
    and body, which can also be a CharField.

    Note: If the CharField of your form 
    corresponds to a model CharField, make 
    sure both have the same max_length value.


    forms.TextInput widget This tells  Django to 
    load this field as an HTML text input element 
    in the templates. 
    
    The body field uses a forms.TextArea widget 
    instead, so that the field is rendered as 
    an HTML text area element.
    
    These widgets also take an argument attrs, 
    which is a dictionary and allows us to 
    specify some CSS classes, which will help 
    with formatting the template for this 
    view later. It also allows us to add some 
    placeholder text.
    
    When a form is posted, a POST request is 
    sent to the server. So, in the view function, 
    we need to check if a POST request has been 
    received. We can then create a comment from 
    the form fields. Django comes with a handy 
    is_valid() on its forms, so we can check 
    that all the fields have been entered 
    correctly.
    
    Once you’ve created the comment from the 
    form, you’ll need to save it using save() 
    and then query the database for all the 
    comments assigned to the given post. 
    
        blog/views.py 
        should contain: 
        form = CommentForm() .....
    
    """


    # argument widget The author field has the 
    # "forms.TextInput" widget. 
    # This tells Django to load this field as an 
    # HTML text input element in the templates.
    author = forms.CharField(
        max_length=60, 
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your Name"
        })
    )
    # Using "forms.TextArea" widget
    #argument attrs is a dictionary that allow us to
    # to specify CSS classes, this allow us to add 
    # placeholder text
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a comment!"
        })
    )

 