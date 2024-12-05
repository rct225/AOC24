# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re
# import math



# # test_str = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

with open('aoc3.data.txt') as file:
    s = file.read()

def inner(rs):
    regex = r"mul\((\d+),(\d+)\)"
    matches = re.finditer(regex, rs, re.MULTILINE)

    total = 0
    for match in matches:
        # print(match)
        # print(match.group(1), match.group(2))
        total += int(match.group(1)) * int(match.group(2))
    # print(total)
    return total

def outer(rs):
    regex1 = r".+?(?=don't\(\))"
    matches1 = re.findall(regex1, rs, re.DOTALL)
    part1 = matches1[0]
    regex2 = "(?<=do\\(\\))(.+?)(?=don't\\(\\)|$)"
    matches2 = re.findall(regex2, rs[len(part1):], re.DOTALL)
    part1_total = inner(part1)
    part2_total = sum(inner(match) for match in matches2)
    return part1_total + part2_total


# test = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


# # test = "do select()} <*mul(843,597)!~mul(717,524)&?}'mul(928,721)>mul(194,52)'why()]-*select()what(898,458):#*mul(31,582)mul(209,470)'-mul(834,167)>}mul(188,914)where(344,689)select(90,321)where()-when()[{]mul(133,940)#-mul(732,657)why()$when()-how()?!>who(208,16)mul(332,604)?do()^:how():: mul(613,614)@);mul(458,93)@# @$~+#select(234,120)mul(184,924)~ why()^$' #{mul(882,83)~<&mul(878,13)select()who()?mul(947,828)select()select())?>^where()how()'*mul(837,672)-select():from())[^$^mul(325,979)}what()[select()mul(226,766)?where()'what():mul(964,728)/)~$~how()&]%]mul(420,781)$how()/]! ~]?mul(624,205)-how()<(*where()where()mul(33,801)mul(614,925)/mul(660,91)}/mul(205,753)$- }mul(136,460)where(671,425)from()@mul(316,262)*?'%(mul(290,988)why()<+[%from()/@>mul(694,616)what()from()what()#$where()mul(666,785)mul(668,125)!%/&*(~*mul(728,226)why() %/{'>how(615,392):mul(478,823)>do()mul(166,999)%~!!mul(368,199)how()!who()/<-[mul(43,454)how(673,426))do()when()$from()why()^mul(228,279)how():select()mul(413,456)where(){$-[where()who()mul(769,535)mul(290,859)!#do();who()&+%mul(734,882)mul(346,904)/mul(319,21)<mul(548,912)mul(776,306)/'when() -^-!/mul(805,224)who(),~{when()[mul(641,941)+*why()mul(880,39)!mul(367,322)+{;why())<where():+ do():who()who(){mul(297,155){>/@!}[(: mul(582,935);mul(924,453)where():]*]mul(962,327):?<where(583,199)/[{)how()don't()where()^mul(493,697)'%+#[!mul(64,397)*^;)how()}!mul(133,628):-&@%?&;when()(mul(245,450){who()*mul(8,731)!([&mul(862,150)who()why()who()'mul(129,583)@:why()[ mul(557,879)why()%,@mul(969,31)^*mul(243,857)#]'?^~mul(418,611)@who()[-mul(381,404)#? who()}}how(),$mul(992,433)#[~from()%mul(823,119)who();when()from()mul(436,64)when()<{when()how(141,705)$<{select(673,665)@mul(776,698)mul(859,821)where(733,36)}>$who()who()<~don't"
# print(inner(test))

print(outer(s))