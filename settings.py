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
  "space":"57North Hacklab",
  "url":"https://57north.org.uk/",
  "state":{
    "icon":{
      "open": "https://57north.org.uk/57_North_CLL_open.png",
      "closed": "https://57north.org.uk/57_North_CLL_closed.png"
    }
  },
  "location":{
    "address":"Engage Gaming, at 26 North Silver Street, AB10 1RL",
    "lat":57.147295,
    "lon":-2.106229
  },
  "contact":{
    "twitter":"@57NorthHacklab",
    "ml":"57north-discuss@lists.57north.co",
    "irc":"irc://irc.freenode.net/#57N",
    "issue_mail":"contact@57north.org.uk"
  },
  "issue_report_channels":[
    "issue_mail"
  ],
  "feeds":{
    "calendar":{
      "type":"ical",
      "url":"http://opentechcalendar.co.uk/api1/group/151/events.ical"
    },
    "wiki":{
      "type":"atom",
      "url":"https://wiki.57north.org.uk/api.php?hidebots=1&urlversion=1&days=7&limit=50&action=feedrecentchanges&feedformat=atom"
    }
  },
  "logo":"https://57north.org.uk/wiki_logo.png"
}

