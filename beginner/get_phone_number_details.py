# Get phone number details
#!pip install phonenumbers
import phonenumbers as pn
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone

# Parse phone number details
z = pn.parse("+442083661177", None)
print(z)

z= pn.parse("020 8366 1177", "GB")
print(z)

z = pn.parse("00 1 650 253 2222", "GB") # as dialled from GB, not a GB number
print(z)

# Test for valid phone numbers
z = pn.parse("+120012301", None)
print(pn.is_possible_number(z))  # Too few digits for USA
print(pn.is_valid_number(z))

# Format phone numbers
z = pn.parse("020 8366 1177", "GB")
z_national = pn.format_number(x, phonenumbers.PhoneNumberFormat.NATIONAL)
z_international = pn.format_number(z, ph.PhoneNumberFormat.INTERNATIONAL)
z_e164 = pn.format_number(z, ph.PhoneNumberFormat.E164)
print(f"NATIONAL: {z_national}")
print(f"INTERNATIONAL: {z_international}")
print(f"E164: {z_e164}")

# Extract phone numbers from text
text = "Call me at 510-748-8230 if it's before 9:30, or on 703-4800500 after 10am. 510-870-5022"
for match in pn.PhoneNumberMatcher(text, "US"):
    p_num = pn.format_number(match.number, ph.PhoneNumberFormat.E164)
    t_zone = timezone.time_zones_for_number(match.number)
    print(f"| {p_num} | {t_zone} |")

# Get carrier info
ro_number = phonenumbers.parse("+40721234567", "RO")
c_name = carrier.name_for_number(ro_number, "en")
print(f"Carrier: {c_name}")

# Get geo location
ch_number = pn.parse("0431234567", "CH")
loc = geocoder.description_for_number(ch_number, "en")
print(f"Location: {loc}")

# Get timezone
gb_number =pn.parse("+447986123456", "GB")
t_zone = timezone.time_zones_for_number(gb_number)
print(f"Timezone: {t_zone}")

