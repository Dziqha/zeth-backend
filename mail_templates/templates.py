import os

class MailBuilder:
    def verify_email(self, recipient_name, activation_link):
        with open('mail_templates/verify_email.html', 'r') as file:
            html_content = file.read()
                
        html_content = html_content.replace('%NAME%', recipient_name)
        html_content = html_content.replace('%VERIFICATION_URL%', activation_link)
        
        return html_content

    def reset_password(self, recipient_name, reset_password_link):
        with open('mail_templates/reset_password_email.html', 'r') as file:
            html_content = file.read()
                
        html_content = html_content.replace('%NAME%', recipient_name)
        html_content = html_content.replace('%RESET_PASSWORD_URL%', reset_password_link)
        
        return html_content