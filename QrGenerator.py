#requirements: qrcode
#bash: pip install qrcode[pil] or python -m pip install qrcode

import qrcode

# Link to your event or invitation
event_link = "https://your-event-link.com"

# Generate QR code
qr = qrcode.make(event_link)
qr.save("event_invitation_qr.png")

print("QR code created successfully!")
# The QR code image is saved as 'event_invitation_qr.png'