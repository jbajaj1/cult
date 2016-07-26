#!/usr/bin/env python
import email

email.setFileRead("cult.txt")
email.setFileOut("email_lists.txt")
email.setUrl(['https://lists.acm.jhu.edu/mailman/subscribe/acm','https://lists.acm.jhu.edu/mailman/subscribe/announce'])
email.run()
