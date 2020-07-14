import gettext

# Set up message catalog access
t: gettext.NullTranslations = gettext.translation(
    "example", "locale", fallback=True,
)
_ = t.gettext

# Fallback mode is enabled - in-lined message is printed if message catalog is not
# available.
print(_("This message is in the script."))

num = 1
message1: str = t.ngettext(
    "There is {number} file here", "There are {number} files here", num
)
print(message1.format(number=num))

num = 2
message2: str = t.ngettext(
    "There is {number} file here", "There are {number} files here", num
)
print(message2.format(number=num))
