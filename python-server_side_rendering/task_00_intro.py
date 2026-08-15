import os

def generate_invitations(template, attendees):
    # 1. Check Input Types
    if not isinstance(template, str):
        print("Error: Template should be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees should be a list of dictionaries.")
        return

    # 2. Handle Empty Inputs
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # 3. Process Each Attendee
    for index, attendee in enumerate(attendees, start=1):
        # Create a copy of the template to modify for this specific attendee
        invitation = template

        # List of placeholders we expect in the template
        placeholders = ["name", "event_title", "event_date", "event_location"]

        for placeholder in placeholders:
            # Get the value from the dictionary
            value = attendee.get(placeholder)
            
            # If the value is missing or None, replace with "N/A"
            if value is None:
                value = "N/A"
            else:
                value = str(value)
            
            # Replace the placeholder in the template with the actual value
            invitation = invitation.replace(f"{{{placeholder}}}", value)

        # 4. Generate Output Files
        file_name = f"output_{index}.txt"
        try:
            with open(file_name, 'w') as file:
                file.write(invitation)
        except Exception as e:
            print(f"Error writing to {file_name}: {e}")