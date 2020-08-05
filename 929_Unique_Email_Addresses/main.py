# Every email consists of a local name and a domain name, 
# separated by the @ sign.
# 
# For example, alice@leetcode.com:
# - local name: "alice"
# - domain name: "leetcode.com"
# 
# Besides lowercase letters, these emails may contain '.'s or '+'s.
# 
# If you add periods ('.') between some characters in the 'local 
# name' part of an email address, mail sent there will be forwarded 
# to the same address without dots in the local name.  
#
# For example, "alice.z@leetcode.com" and "alicez@leetcode.com" 
# forward to the same email address.
#
# This rule does not apply for domain names.
# 
# If you add a plus ('+') in the local name, everything after 
# the first plus sign will be ignored. This allows certain emails 
# to be filtered, for example m.y+name@email.com will be forwarded 
# to my@email.com.
#
# Again, this rule does not apply for domain names.
# 
# It is possible to use both of these rules at the same time.
# 
# Given a list of emails, we send one email to each address in the list. 
# Determine the number of addresses that will actually receive mails.

import re

class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        realemails = set()
        regex_w_plus = re.compile(r'(.+?)\+.*@(.+)')
        regex_no_plus = re.compile(r'(.+)@(.+)')
        for email in emails:
            regex = regex_w_plus if ('+' in email) else regex_no_plus
            match = regex.match(email)
            localname = match.group(1).replace('.','')
            domain = match.group(2)
            realemails.add(localname + "@" + domain)
        return len(realemails)

sln = Solution()
print(sln.numUniqueEmails(["fg.r.u.uzj+o.pw@kziczvh.com","r.cyo.g+d.h+b.ja@tgsg.z.com","fg.r.u.uzj+o.f.d@kziczvh.com","r.cyo.g+ng.r.iq@tgsg.z.com","fg.r.u.uzj+lp.k@kziczvh.com","r.cyo.g+n.h.e+n.g@tgsg.z.com","fg.r.u.uzj+k+p.j@kziczvh.com","fg.r.u.uzj+w.y+b@kziczvh.com","r.cyo.g+x+d.c+f.t@tgsg.z.com","r.cyo.g+x+t.y.l.i@tgsg.z.com","r.cyo.g+brxxi@tgsg.z.com","r.cyo.g+z+dr.k.u@tgsg.z.com","r.cyo.g+d+l.c.n+g@tgsg.z.com","fg.r.u.uzj+vq.o@kziczvh.com","fg.r.u.uzj+uzq@kziczvh.com","fg.r.u.uzj+mvz@kziczvh.com","fg.r.u.uzj+taj@kziczvh.com","fg.r.u.uzj+fek@kziczvh.com"]))
