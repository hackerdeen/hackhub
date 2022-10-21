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
    "address":"57North Hacklab, c/o Aberdeen Action on Disability, Suite H, Kettock Lodge, Innovation Park, Campus Two, Bridge of Don, Aberdeen AB22 8GU",
    "lat":57.179470,
    "lon":-2.110614
  },
  "contact":{
    "twitter":"@57NorthHacklab",
    "ml":"57north-discuss@lists.57north.org.uk",
    "irc":"irc://irc.libera.chat/#57N",
    "issue_mail":"contact@57north.org.uk",
    "phone":"+443304450576",
    "phone_gb_local":"+441224900457",
    "phone_de":"+49221569191057",
    "sip":"sip:1057@hg.eventphone.de"
  },
  "issue_report_channels":[
    "issue_mail"
  ],
  "feeds":{
    "calendar":{
      "type":"ical",
      "url":"http://opentechcalendar.co.uk/api1/group/151/events.ical"
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
