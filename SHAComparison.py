## SHA 256 comparison tool

a = "F483D6E182F1F8813491327FEB3FBCC1445E782418BDB2E4297127BA8DD77968"
B = "f483d6e182f1f8813491327feb3fbcc1445e782418bdb2e4297127ba8dd77968"

if a.lower() == B.lower():
    print("This software is safe to install")
else:
    print("STOP! This program is not safe to install")


c = "c75a8520756cf5b0dc1fde4d09eb71afe8ed711c60b332f2763a423bdc546b2c"
d = "c75a8520756cf5b0dc1fde4d09eb71afe8ed711c60b332f2763a423bdc546b2c"

if a.lower() == B.lower():
    print("This software is Also safe to install")
else:
    print("STOP! This program is Also not safe to install")
