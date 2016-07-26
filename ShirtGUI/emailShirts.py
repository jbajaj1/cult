#!/usr/bin/env python
import email

email.setFileRead("shirts.txt")
email.setFileWrite("shirtForm.txt")
#email.setUrl(['https://lists.acm.jhu.edu/mailman/subscribe/acm', 'https://lists.acm.jhu.edu/mailman/subscribe/announce'])
email.run()
