from local_settings import *

# Settings
SQLITE_DB = "/home/hackhub/hackhub.db"
CAS_SERVICE_URL = "https://hub.57north.org.uk/hub/login/ticket"
CAS_SERVER_URL = "https://guest.id.57north.org.uk"
LDAP_URI = "ldap://localhost"
LDAP_BIND_DN = "uid=id-admin,ou=special-users,dc=57north,dc=org,dc=uk"
LDAP_MEMBERS_GROUP_DN = "cn=members,ou=groups,dc=57north,dc=org,dc=uk"
LDAP_USERS_DN = "ou=users,dc=57north,dc=org,dc=uk"

# This is used as the basis for the SpaceAPI
spaceapi = {
  "api":"0.13",
  "space":"Not 57North Hacklab",
  "url":"https://57north.org.uk/",
  "location":{
    "address":"35a Union Street, Aberdeen, United Kingdom",
    "lat":57.147310,
    "lon":-2.095607
  },
  "contact":{
    "twitter":"@57NorthHacklab",
    "ml":"57north-discuss@57north.co",
    "irc":"irc://irc.freenode.net/#57N",
    "phone":"+441224583491",
    "issue_mail":"contact@57north.co"
  },
  "issue_report_channels":[
    "issue_mail"
  ],
  "logo":"https://57north.org.uk/wiki_logo.png"
}

