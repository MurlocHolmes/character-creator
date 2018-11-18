import base64
token="V2rgOdwlOuqk9-hrOAGs-Yorv3_329DlCf-PUnp9SnlYTXhYKrzG0DMjajfTujRvWJOmxRzn3PA3G36yvEL9T1hfL-1ux6LdGjbDURqNwvd0PxhHcHJeAN1rjdoDOFfyGMfPGMPzX-Ngzh2v9Kz-SQ%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00"
print(len(token))
while len(token) % 4 != 0:
    token = token + '='
print(base64.urlsafe_b64decode(token))
