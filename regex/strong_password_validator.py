# https://regex101.com/r/W4kRV2/2/
# https://en.wikipedia.org/wiki/List_of_Unicode_characters
# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[ -\/:-@[-`{-~]).{12,}?"

test_str = ("VÁLIDAS\n"
            "v2Ts7<o9T~}Y\n"
            "j25TTbjJ:6{<\n"
            "s`Mu6T;4M1!y\n"
            "Li`hk6:3WX>3\n"
            "d.D09}^dI2Vn\n"
            "LuizOtavio1@\n"
            "P@ssw0rd1235\n\n"
            "SEM MINÚSCULAS\n"
            "I7^Y3RS^ 9]7\n"
            "[P6W\"83L5V{[\n"
            "B7=;K8D6_}W5\n"
            "1B_RT`93R%>1\n"
            "EZU{7;2&D:64\n\n"
            "SEM MINÚSCULAS E NÚMEROS\n"
            "E}LV`C?X_G:{\n"
            "AJH[@HD*V~=<\n"
            "\\A~AC{_V~MG \n"
            "W<-T}W:QAF'{\n"
            "~YJ}|FILN>~)\n\n"
            "SEM NÚMEROS CARACTERES E MINÚSCULAS\n"
            "PBDZDPECUDNN\n"
            "EJQWFWFFDEHY\n"
            "XRCNLNRHYOZJ\n"
            "TWIYPLWUDMNN\n"
            "JMDTJSEPKVON\n\n"
            "QUANTIDADE INVÁLIDA (6)\n"
            "Iu4<1j\n"
            "1x`P6g\n"
            "@9t3Ry\n"
            "qf9_6H\n"
            "0o`9fO")

matches = re.finditer(regex, test_str, re.MULTILINE | re.UNICODE)

for matchNum, match in enumerate(matches, start=1):

    print("Match {matchNum} was found at {start}-{end}: {match}".format(
        matchNum=matchNum, start=match.start(), end=match.end(), match=match.group()))

    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1

        print("Group {groupNum} found at {start}-{end}: {group}".format(groupNum=groupNum,
              start=match.start(groupNum), end=match.end(groupNum), group=match.group(groupNum)))

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.
n
