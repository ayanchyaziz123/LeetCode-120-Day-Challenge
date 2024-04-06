def generate_landlord_letter(landlord_name, tenant_name, property_address, start_date, end_date, contact_info):
    letter = f"""
{landlord_name}
Property Manager
{contact_info['address']}
{contact_info['city']}, {contact_info['state']}, {contact_info['zip']}
Phone: {contact_info['phone']}
Date: {contact_info['date']}

To Whom It May Concern,

I am writing this letter to verify the tenancy of {tenant_name}. They have been residing at {property_address}, which is owned and managed by our property management, from {start_date} to {end_date}.

During the period of their tenancy, {tenant_name} has consistently met the obligations of the rental agreement, including the timely payment of rent and maintenance of the property in a satisfactory condition. We have found them to be a responsible and respectful tenant.

Should you require any further information or verification, please feel free to contact me at {contact_info['phone']}.

Sincerely,

[Your Signature]
{landlord_name}
Property Manager
"""

    return letter

# Example usage
contact_info = {
    'address': '8017 101st avenue',
    'city': 'New York',
    'state': 'New York',
    'zip': '11416',
    'phone': '(347) 669-6071',
    'date': 'April 4, 2024'
}

landlord_name = 'Aziz Chowdhury'
tenant_name = 'Md Mahbubur Rahman, Fahima Uddin and Maha Rahman'
property_address = '9308 101st avenue ozone park, new york 11416'
starting = 'January 1, 2022'
ending = 'present'



print(generate_landlord_letter(landlord_name, tenant_name, property_address, starting, ending, contact_info))
