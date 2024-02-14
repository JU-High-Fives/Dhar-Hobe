from django.core.mail import send_mail

class EmailService:
    """
    A class to handle email notifications.

    Attributes:
        None
    """
    def send_email(self, renter_email, product_name, renter_name, subject_template, message_template):
        """
        Sends an email notification to renter.

        Parameters:
            renter_email (str): The email address of the renter.
            product_name (str): The name of the product.
            renter_name (str): The name of the renter.
            subject_template (str): The subject template for the email.
            message_template (str): The message template for the email.

        Returns:
            None
        """
        subject = subject_template.format(product_name=product_name,renter_name=renter_name)
        message = message_template.format(product_name=product_name,renter_name=renter_name)
        send_mail(subject, message, 'iffat.stu2018@juniv.edu', [renter_email])

class ProductService:
    """
    A class to handle product approval and disapproval actions.

    Attributes:
        None
    """
    def approve_product(self, renter_product):
        """
        Approves a product request and sends an email notification.

        Parameters:
            renter_product (RenterProduct): The renter product object representing the request to be approved.

        Returns:
            None
        """
        # Update the status or perform any other necessary actions
        EmailService().send_email(
            renter_product.renter.email,
            renter_product.product.name,
            renter_product.renter.username,
            'Product Approval Notification',
            'Dear {renter_name},\n\nYour request to add {product_name} for rent has been approved.\n\nThank you,\nAdmin,\nDhar Hobe'
        )

    def disapprove_product(self, renter_product):
        """
        Disapproves a product request and sends an email notification.

        Parameters:
            renter_product (RenterProduct): The renter product object representing the request to be disapproved.

        Returns:
            None
        """
        # Update the status or perform any other necessary actions
        EmailService().send_email(
            renter_product.renter.email,
            renter_product.product.name,
            renter_product.renter.username,
            'Product Disapproval Notification',
            'Dear {renter_name},\n\nYour request to add {product_name} for rent has been disapproved:(.\n\nThank you,\nAdmin,\nDhar Hobe'
        )
