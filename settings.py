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
    "issue_mail":"contact@57north.org.uk",
    "phone":"+49221569191057",
    "sip":"sip:1057@hg.eventphone.de"
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

common_msgs = ["alrighty then", "Ummm...","Welcome to the internet of things.", "I can haz hax?",
               "I need to put something here", "Hacky hack hack",
               "I don't want to interrupt, but did you hear about my weapons-grade plutonium?"]

open_msgs = common_msgs + ["Commence hacking",  "Man your hackstations", "Hackurday", "Happy New Hack",
                           "TODO: open message", "Open? Open!", 
                           "WARN: closed has been deprecated.", "let the blinkenlights blink",
                           "Space is very open. Now so is the space.", "Openness detected",
                           "Frankly, we're very open.", "So open"]
             
close_msgs = common_msgs + ["Cease hacking", "Stand down from hackstations", "Ex-hack",
                            "exit pursued by bear", "TODO: close message", "Closed? Closed.",
                            "A state of closedness has been detected.", "Dim the blinkenlights",
                            "Done."]
