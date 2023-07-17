
from django.contrib.auth.models import AbstractUser, BaseUserManager


class CustomerManager(BaseUserManager):
    def create_customer(self, username, email, address, phone_number, password, **extra_fields):
        if self.filter(username=username).exists():
            # Handle case when username already exists
            return None

        customer = self.model(username=username, email=email, address=address, phone_number=phone_number, **extra_fields)
        customer.set_password(password)
        customer.save()
        return customer
  

    def get_by_natural_key(self, username):
        return self.get(username=username)


class Customer(AbstractUser):
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)

    objects = CustomerManager()

    def __str__(self):
        return self.username




















def register(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            # Save the name field
            name = form.cleaned_data['name']
            user.customer.name = name
            user.customer.save()
            return redirect('login')
    else:
        form = CustomerRegistrationForm()

    return render(request, 'main/register.html', {'form': form})